from edi.rede.mappers.factories import *
from edi.rede.mappers.utils import LineParser, Field


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