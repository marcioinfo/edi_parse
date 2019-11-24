from dataclasses import dataclass
from typing import Callable, Any
from datetime import date, datetime, time
from decimal import Decimal


@dataclass
class Field:
    inicio: int
    fim: int
    tam: int
    factory: Callable
    default: Any = None


class LineParserMeta(type):
    def __new__(meta, name, bases, dct):
        def init(self, line):
            self.line = line

        def repr(self):
            attrs =  ''.join([f'{f}={v}, ' for f, v in self.__dict__.items() if f != 'line'])[:-2]
            return f'{name}({attrs})'
        dct.update({'__init__': init, '__repr__': repr})
        return super(LineParserMeta, meta).__new__(meta, name, bases, dct)
    
    def __call__(cls, *args, **kwds):
        line = args[0] if args else kwds['line']
        instance = type.__call__(cls, *args, **kwds)
        for name, attr in cls.__dict__.items():
            if isinstance(attr, Field):
                if attr.default is None:
                    try:
                        input = line[attr.inicio-1: attr.fim]
                        value = attr.factory(input)
                    except Exception:
                        raise Exception(f"\tLine error {line}.\n\t\tIn parser {cls.__name__} required '{name}' field not found or value '{input}' is invalid for factory '{attr.factory}'.")
                else:
                    try:
                        value = attr.factory(line[attr.offset: attr.length])
                    except Exception:
                        value = attr.factory(attr.default)
                setattr(instance, name, value)
        return instance


class LineParser(metaclass=LineParserMeta):
    @classmethod
    def headers(cls):
        exclude = ('line', 'codigo')
        return [_ for _ in dir(cls) if _ not in exclude and not _.startswith('_') and not callable(getattr(cls, _))]

    def values(self):
        return [getattr(self, _) for _ in self.headers()]

    def values_as_str(self):
        return [str(_) for _ in self.values()]

    def _filter(self, _type):
        return [_ for _ in self.values() if isinstance(_, _type)]

    def dates(self):
        return self._filter((date, datetime, time))

    def monetary(self):
        return self._filter(Decimal)
