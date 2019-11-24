from edi.rede.mappers.factories import *
from edi.rede.mappers.utils import Field, LineParser


class Registro35CVNSUParceladosjurosecommerce(LineParser):
    codigo = '035'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodoRV = Field(13, 21, 9, int)
    DatadoCVNSU = Field(22, 29, 8, date_factory)
    ValordoCVNSU = Field(30, 44, 15, monetary_factory)
    Numerodocartao = Field(45, 60, 16, str)
    NumerodoCVNSU = Field(61, 72, 12, int)
    NoAutorizacao = Field(73, 78, 6, str)
    TID = Field(79, 98, 20, str)
    NumeroPedido = Field(99, 128, 30, str)


class Registro12CVNSUparceladosjuros(LineParser):
    codigo = '012'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodoRV = Field(13, 21, 9, int)
    DatadoCVNSU = Field(22, 29, 8, date_factory)
    Zeros = Field(30, 37, 8, int)
    ValordoCVNSU = Field(38, 52, 15, monetary_factory)
    Valordagorjeta = Field(53, 67, 15, monetary_factory)
    Numerodocartao = Field(68, 83, 16, str)
    StatusdoCVNSU = Field(84, 86, 3, str)
    Numerodeparcelas = Field(87, 88, 2, int)
    NumerodoCVNSU = Field(89, 100, 12, int)
    Numerodereferencia = Field(101, 113, 13, str)
    Valordodesconto = Field(114, 128, 15, monetary_factory)
    Nodaautorizacao = Field(129, 134, 6, str)
    Horadatransacao = Field(135, 140, 6, hour_factory)
    Nodobilhete = Field(141, 156, 16, str)
    Nodobilhete = Field(157, 172, 16, str)
    Nodobilhete = Field(173, 188, 16, str)
    Nodobilhete = Field(189, 204, 16, str)
    Tipodecaptura = Field(205, 205, 1, str)
    ValorliquidodoCVNSU = Field(206, 220, 15, monetary_factory)
    Valorliquidodaprimeiraparcela = Field(221, 235, 15, monetary_factory)
    Valorliquidodasdemaisparcelas = Field(236, 250, 15, monetary_factory)
    Numerodoterminal = Field(251, 258, 8, str)
    Sigladopais = Field(259, 261, 3, str)
    Bandeira = Field(262, 262, 1, str)


class Registro014ParcelasParceladosemjuros(LineParser):
    codigo = '014'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodoRV = Field(13, 21, 9, int)
    DatadoRV = Field(22, 29, 8, date_factory)
    Brancos = Field(30, 37, 8, int)
    Numerodaparcela = Field(38, 39, 2, int)
    Valordaparcelabruto = Field(40, 54, 15, monetary_factory)
    Valordodescontosobreaparcela = Field(55, 69, 15, monetary_factory)
    Valordaparcelaliquida = Field(70, 84, 15, monetary_factory)
    Datadocredito = Field(85, 92, 8, date_factory)
    Livre = Field(93, 1024, 932, str)


class Registro008CVNSUrotativo(LineParser):
    codigo = '008'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodoRV = Field(13, 21, 9, int)
    DatadoCVNSU = Field(22, 29, 8, date_factory)
    Zeros = Field(30, 37, 8, int)
    ValordoCVNSU = Field(38, 52, 15, monetary_factory)
    Valordagorjeta = Field(53, 67, 15, monetary_factory)
    Numerodocartao = Field(68, 83, 16, str)
    StatusdoCVNSU = Field(84, 86, 3, str)
    NumerodoCVNSU = Field(87, 98, 12, int)
    Numerodereferencia = Field(99, 111, 13, str)
    Valordodesconto = Field(112, 126, 15, monetary_factory)
    Noautorizacao = Field(127, 132, 6, str)
    Horadatransacao = Field(133, 138, 6, hour_factory)
    Nodobilhete = Field(139, 154, 16, str)
    Nodobilhete = Field(155, 170, 16, str)
    Nodobilhete = Field(171, 186, 16, str)
    Nodobilhete = Field(187, 202, 16, str)
    Tipodecaptura = Field(203, 203, 1, str)
    Valorliquido = Field(204, 218, 15, monetary_factory)
    Numerodoterminal = Field(219, 226, 8, str)
    Sigladopais = Field(227, 229, 3, str)
    Bandeira = Field(230, 230, 1, str)


class Registro034CVNSURotativoecommerce(LineParser):
    codigo = '034'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodoRV = Field(13, 21, 9, int)
    DatadoCVNSU = Field(22, 29, 8, date_factory)
    ValordoCVNSU = Field(30, 44, 15, monetary_factory)
    Numerodocartao = Field(45, 60, 16, str)
    NumerodoCVNSU = Field(61, 72, 12, int)
    NoAutorizacao = Field(73, 78, 6, str)
    TID = Field(79, 98, 20, str)
    NumerodoPedido = Field(99, 128, 30, str)


class Registro010RVparceladosemjuros(LineParser):
    codigo = '010'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodoRV = Field(13, 21, 9, int)
    Nodobanco = Field(22, 24, 3, int)
    Nodaagencia = Field(25, 29, 5, int)
    Nodacontacorrente = Field(30, 40, 11, int)
    DatadoRV = Field(41, 48, 8, date_factory)
    QuantidadedeCVNSUs = Field(49, 53, 5, int)
    Valorbruto = Field(54, 68, 15, monetary_factory)
    Valordagorjeta = Field(69, 83, 15, monetary_factory)
    Valorrejeitado = Field(84, 98, 15, monetary_factory)
    Valordodesconto = Field(99, 113, 15, monetary_factory)
    Valorliquido = Field(114, 128, 15, monetary_factory)
    Datadecreditoda1aparcela = Field(129, 136, 8, date_factory)
    Bandeira = Field(137, 137, 1, str)


class Registro006RVrotativo(LineParser):
    codigo = '006'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodoRV = Field(13, 21, 9, int)
    Nodobanco = Field(22, 24, 3, int)
    Nodaagencia = Field(25, 29, 5, int)
    Nodacontacorrente = Field(30, 40, 11, int)
    DatadoRV = Field(41, 48, 8, date_factory)
    QuantidadedeCVNSUsacatados = Field(49, 53, 5, int)
    Valorbruto = Field(54, 68, 15, monetary_factory)
    Valordagorjeta = Field(69, 83, 15, monetary_factory)
    Valorrejeitado = Field(84, 98, 15, monetary_factory)
    Valordodesconto = Field(99, 113, 15, monetary_factory)
    Valorliquido = Field(114, 128, 15, monetary_factory)
    Datadecredito = Field(129, 136, 8, date_factory)
    Bandeira = Field(137, 137, 1, str)


class Registro028Trailerdearquivo(LineParser):
    codigo = '028'
    TipoderegistroTrailerdearquivo = Field(1, 3, 3, int)
    Quantidadedematrizes = Field(4, 7, 4, int)
    Quantidadederegistros = Field(8, 13, 6, int)
    NoPVgrupo = Field(14, 22, 9, str)
    Valortotalbruto = Field(23, 37, 15, monetary_factory)
    QuantidadedeCVNSUsrejeitados = Field(38, 43, 6, int)
    Valortotalrejeitado = Field(44, 58, 15, monetary_factory)
    Valortotalrotativo = Field(59, 73, 15, monetary_factory)
    Valortotalparceladosemjuros = Field(74, 88, 15, monetary_factory)
    ValortotalparceladoIATA = Field(89, 103, 15, monetary_factory)
    Valortotaldolar = Field(104, 118, 15, monetary_factory)
    Valortotaldesconto = Field(119, 133, 15, monetary_factory)
    Valortotalliquido = Field(134, 148, 15, monetary_factory)
    Valortotalgorjeta = Field(149, 163, 15, monetary_factory)
    Valortotaldataxadeembarque = Field(164, 178, 15, monetary_factory)
    QuantCVNSUacatados = Field(179, 184, 6, int)


class Registro026TotalizadorMatriz(LineParser):
    codigo = '026'
    Tipoderegistro = Field(1, 3, 3, int)
    NoPVmatriz = Field(4, 12, 9, str)
    Valortotalbruto = Field(13, 27, 15, monetary_factory)
    QuantidadedeCVNSUsrejeitados = Field(28, 33, 6, int)
    Valortotalrejeitado = Field(34, 48, 15, monetary_factory)
    Valortotalrotativo = Field(49, 63, 15, monetary_factory)
    Valortotalparceladosemjuros = Field(64, 78, 15, monetary_factory)
    ValortotalparceladoIATA = Field(79, 93, 15, monetary_factory)
    Valortotaldolar = Field(94, 108, 15, monetary_factory)
    Valortotaldesconto = Field(109, 123, 15, monetary_factory)
    Valortotalliquido = Field(124, 138, 15, monetary_factory)
    Valortotaldagorjeta = Field(139, 153, 15, monetary_factory)
    Valortotaldataxadeembarque = Field(154, 168, 15, monetary_factory)
    QuantCVNSUacatados = Field(169, 174, 6, int)


class Registro004Headermatriz(LineParser):
    codigo = '004'
    Tipoderegistro = Field(1, 3, 3, int)
    NoPVmatriz = Field(4, 12, 9, str)
    Nomecomercialdamatriz = Field(13, 34, 22, str)


class Registro002HeaderdoArquivo(LineParser):
    codigo = '002'
    Tipoderegistro = Field(1, 3, 3, int)
    Datadeemissao = Field(4, 11, 8, date_factory)
    Rede = Field(12, 19, 8, str)
    ExtratoEletronicodeVendas = Field(20, 49, 30, str)
    Nomecomercial = Field(50, 71, 22, str)
    Sequenciadomovimento = Field(72, 77, 6, int)
    NoPVgrupooumatriz = Field(78, 86, 9, int)
    Tipodemovimento = Field(87, 101, 15, str)
    Versaodoarquivo = Field(102, 121, 20, str)
    Livre = Field(122, 1024, 903, str)


class Registro005Request6(LineParser):
    codigo = '005'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodoRV = Field(13, 21, 9, int)
    Numerodocartao = Field(22, 37, 16, str)
    ValordatransacaoCVNSU = Field(38, 52, 15, monetary_factory)
    DatadatransacaoCVNSU = Field(53, 60, 8, date_factory)
    NumerodeReferencia = Field(61, 75, 15, int)
    Numerodoprocesso = Field(76, 90, 15, int)
    NumerodoCVNSU = Field(91, 102, 12, int)
    Nodeautorizacao = Field(103, 108, 6, str)
    CodigodoRequest = Field(109, 112, 4, str)
    Limitedeenviodosdocumentos = Field(113, 120, 8, date_factory)
    Bandeira = Field(121, 121, 1, str)
    Livre = Field(122, 1024, 903, str)


class Registro011AjustesacreditoExtratoEletronicodeVendas(LineParser):
    codigo = '011'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPVcreditado = Field(4, 12, 9, int)
    Numerodoresumodocredito = Field(13, 21, 9, int)
    Datadoajuste = Field(22, 29, 8, date_factory)
    Valordoajuste = Field(30, 44, 15, monetary_factory)
    Datadocredito = Field(45, 52, 8, date_factory)
    Valordocredito = Field(53, 67, 15, monetary_factory)
    C = Field(68, 68, 1, int)
    Banco = Field(69, 71, 3, int)
    Agencia = Field(72, 77, 6, int)
    Contacorrente = Field(78, 88, 11, int)
    Motivodoajuste = Field(89, 90, 2, int)
    Descricaodoajuste = Field(91, 118, 28, str)
    Bandeira = Field(119, 119, 1, str)


