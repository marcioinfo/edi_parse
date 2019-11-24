import unidecode
import re
from decimal import Decimal
from collections import namedtuple

Table = namedtuple('Table', 'code title table')


def clean(s):
    # Remove invalid characters
    s = re.sub('[^0-9a-zA-Z_]', '', s)
    # Remove leading characters until we find a letter or underscore
    s = re.sub('^[^a-zA-Z_]+', '', s)

    return s


to_int = lambda n: int(Decimal(n))


def to_class(T):
    tipos = {'Num(HHMMSS)': 'hour_factory',
             '9(13)V999': 'monetary_factory',
             '9(13)V99': 'monetary_factory',
             'Num(DDMMAAAA)': 'date_factory',
             'Alfa(DDMMAAAA)': 'date_factory',
             'Num(MMAAAA)': 'month_year_factory',
             'Alfa': 'str',
             'Alpha': 'str',
             'Num': 'int'}

    print(f'class {clean(unidecode.unidecode(T.title))}(LineParser):')
    print(f"    codigo = '{T.code}'")
    for row in T.table.split('\n'):
        inicio, fim, tam, tipo, *nome = row.split()
        tipo = tipo.replace('Num.', 'Num')

        nome = ''.join(nome)
        nome = unidecode.unidecode(nome)
        try:
            fmt = next(re.finditer(r'\([A-Z]*\)', nome)).group()
        except StopIteration:
            fmt = ''
        nome = re.sub(r'\(.*\)', '', nome)
        nome = clean(nome)

        inicio, fim, tam = to_int(inicio), to_int(fim), to_int(tam)

        print(f'    {nome} = Field({inicio}, {fim}, {tam}, {tipos[tipo + fmt]})')