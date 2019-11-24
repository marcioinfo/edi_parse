from datetime import datetime
from decimal import Decimal

from parse_utils import LineParser, Field
from dataclasses import dataclass


def date_factory(s):
    return datetime.strptime(s, '%d%m%Y').date()


def monetary_factory(s):
    return Decimal(s) / 100

hour_factory = lambda s: datetime.strptime(s, '%H%M%S').time()

#  EEVD
class DetalhamentoComprovanteVendas(LineParser):
    _type = Field(inicio=1, fim=3, tam=3, factory=str)
    ponto_venda = Field(4, 13, 10, str)
    resumo_venda = Field(14, 22, 10, int)
    data_cv = Field(24, 31, 9, date_factory)
    valor_bruto = Field(33, 47, 16, monetary_factory)
    valor_desconto = Field(49, 63, 16, monetary_factory)
    valor_liquido = Field(65, 79, 16, monetary_factory)
    numero_cartao = Field(81, 99, 20, str)
    tipo_transacao = Field(101, 101, 2, str)
    numero_cv = Field(103, 114, 13, str)
    data_credito = Field(116, 123, 9, date_factory)
    status = Field(125, 126, 3, int)
    hora_transacao = Field(128, 133, 7, hour_factory)
    numero_terminal = Field(135, 142, 9, str)
    tipo_captura = Field(144, 145, 3, int)
    reservado = Field(147, 151, 6, int)
    valor_compra = Field(153, 167, 16, monetary_factory)
    valor_saque = Field(169, 183, 16, monetary_factory)
    bandeira = Field(185, 186, 1, str)


#  EEVC
class ComprovanteVendaCvNsuRotativo(LineParser):
    _type = Field(inicio=1, fim=3, tam=3, factory=str)
    numero_pv = Field(4, 12, 9, int)
    numero_rv = Field(13, 21, 9, int)
    data_cv = Field(22, 29, 8, date_factory)
    zeros = Field(30, 37, 8, int)
    valor_cv = Field(38, 52, 15, monetary_factory)
    valor_gorjeta = Field(53, 67, 15, monetary_factory)
    numero_cartao = Field(68, 83, 16, str)
    status = Field(84, 86, 3, int)
    numero_cv = Field(87, 98, 12, int)
    numero_referencia = Field(99, 111, 13, str)
    valor_desconto = Field(112, 126, 15, monetary_factory)
    numero_autorizacao = Field(127, 132, 6, str)
    hora_transacao = Field(133, 138, 6, hour_factory)
    tipo_captura = Field(203, 203, 1, str)
    valor_liquido = Field(204, 218, 15, monetary_factory)
    numero_terminal = Field(219, 226, 8, str)
    sigla_pais = Field(227, 229, 3, str)
    bandeira = Field(230, 230, 1, str)

if __name__ == '__main__':

    with open('Rede-SACOLAO/teste_eevd.txt') as eevd:
        transacoes = []
        for line in eevd.read().split('\n'):
            if line:
                dcv = DetalhamentoComprovanteVendas(line)
                print(dcv)
                transacoes.append(dcv)

        for tsc in sorted(transacoes, key=lambda t: (t.data_cv, t.hora_transacao)):
            print(','.join([str(_) for _ in [tsc.data_cv, tsc.hora_transacao, tsc.valor_bruto, tsc.valor_compra, tsc.valor_desconto, tsc.valor_liquido,
                                                tsc.valor_saque]]))

    with open('Rede-SACOLAO/teste_eevc.txt') as eevc:
        transacoes = []
        for line in eevc.read().split('\n'):
            if line:
                transacoes.append(ComprovanteVendaCvNsuRotativo(line))

        for tsc in sorted(transacoes, key=lambda t: (t.data_cv, t.hora_transacao)):
            print(','.join([str(_) for _ in [tsc.data_cv, tsc.hora_transacao, tsc.valor_cv, tsc.valor_gorjeta, tsc.valor_desconto,
                                             tsc.valor_liquido]]))
