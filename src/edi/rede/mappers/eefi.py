from edi.rede.mappers.utils import Field, LineParser, LineParserMeta
from edi.rede.mappers.factories import *
import sys


class Registro030Headerdearquivo(LineParser):
    codigo = '030'
    Tipoderegistro = Field(1, 3, 3, int)
    Datadeemissao = Field(4, 11, 8, date_factory)
    Rede = Field(12, 19, 8, str)
    Extratodemovimentacaofinanceira = Field(20, 53, 34, str)
    Nomecomercial = Field(54, 75, 22, str)
    Sequenciadomovimento = Field(76, 81, 6, int)
    NoPVgrupooumatriz = Field(82, 90, 9, int)
    Tipodeprocessamento = Field(91, 105, 15, str)
    Versaodoarquivo = Field(106, 125, 20, str)


class Registro032HeaderMatriz(LineParser):
    codigo = '032'
    Tipoderegistro = Field(1, 3, 3, int)
    NoPVmatriz = Field(4, 12, 9, str)
    Nomecomercialdamatriz = Field(13, 34, 22, str)


class Registro035AjustesNeteDesagendamentos(LineParser):
    codigo = '035'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPVajustado = Field(4, 12, 9, int)
    NumerodoRVajustado = Field(13, 21, 9, int)
    Datadoajuste = Field(22, 29, 8, date_factory)
    Valordoajuste = Field(30, 44, 15, monetary_factory)
    D = Field(45, 45, 1, str)
    Motivodoajuste = Field(46, 47, 2, int)
    Motivodoajuste = Field(48, 75, 28, str)
    Numerodocartao = Field(76, 91, 16, card_number_factory)
    DatadatransacaoCV = Field(92, 99, 8, date_factory, default='01011900')
    NumerodoRVoriginal = Field(100, 108, 9, int)
    Numerodereferenciadacartafax = Field(109, 123, 15, str)
    Datadacarta = Field(124, 131, 8, date_factory, default='01011900')
    Mesdereferencia = Field(132, 137, 6, month_year_factory, default='011900')
    NoPVoriginal = Field(138, 146, 9, int)
    DataRVoriginal = Field(147, 154, 8, date_factory, default='01011900')
    Valordatransacao = Field(155, 169, 15, monetary_factory)
    D = Field(170, 170, 1, str)
    Datadocredito = Field(171, 178, 8, date_factory)
    Novovalordaparcela = Field(179, 193, 15, monetary_factory)
    Valororiginaldaparcela = Field(194, 208, 15, monetary_factory)
    Valorbrutodoresumodevendasoriginal = Field(209, 223, 15, monetary_factory)
    Valordocancelamentosolicitado = Field(224, 238, 15, monetary_factory)
    NumerodoNSU = Field(239, 250, 12, int)
    Numerodaautorizacao = Field(251, 256, 6, str)
    Tipodedebito = Field(257, 257, 1, str)
    NumerodaOrdemdeDebito = Field(258, 268, 11, int)
    Valordodebitototal = Field(269, 283, 15, monetary_factory)
    Valorpendente = Field(284, 298, 15, monetary_factory)
    BandeiradoRVdeorigem = Field(299, 299, 1, str)
    BandeiradoRVajustado = Field(300, 300, 1, str)


class Registro036Antecipacoes(LineParser):
    codigo = '036'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    Numerododocumento = Field(13, 23, 11, int)
    Datadolancamento = Field(24, 31, 8, date_factory)
    Valordolancamento = Field(32, 46, 15, monetary_factory)
    C = Field(47, 47, 1, str)
    Banco = Field(48, 50, 3, int)
    Agencia = Field(51, 56, 6, int)
    Contacorrente = Field(57, 67, 11, int)
    NumerodoRVcorrespondente = Field(68, 76, 9, int)
    DatadoRVcorrespondente = Field(77, 84, 8, date_factory)
    Valordocreditooriginal = Field(85, 99, 15, monetary_factory)
    Datadovencimentooriginal = Field(100, 107, 8, date_factory)
    Numerodaparcelatotal = Field(108, 112, 5, str)
    Valorbruto = Field(113, 127, 15, monetary_factory)
    Valordataxadedesconto = Field(128, 142, 15, monetary_factory)
    NoPVoriginal = Field(143, 151, 9, int)
    Bandeira = Field(152, 152, 1, str)


class Registro037Totalizadordecreditos(LineParser):
    codigo = '037'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    Brancos = Field(13, 19, 7, str)
    Datadocredito = Field(20, 27, 8, date_factory, default='01011900')
    Valortotaldocredito = Field(28, 42, 15, monetary_factory)
    Brancos = Field(43, 43, 1, str)
    Numerodobanco = Field(44, 46, 3, int)
    Numerodaagencia = Field(47, 52, 6, int)
    Numerodacontacorrente = Field(53, 63, 11, int)
    Datadageracaodoarquivo = Field(64, 71, 8, date_factory)
    Datadocreditoantecipado = Field(72, 79, 8, date_factory, default='01011900')
    Valortotaldoscreditosantecipados = Field(80, 94, 15, monetary_factory)


class Registro038Ajustesadebitoviabanco(LineParser):
    codigo = '038'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    Numerododocumento = Field(13, 23, 11, int)
    Datadaemissao = Field(24, 31, 8, date_factory)
    Valordodebito = Field(32, 46, 15, monetary_factory)
    D = Field(47, 47, 1, str)
    Banco = Field(48, 50, 3, int)
    Agencia = Field(51, 56, 6, int)
    Contacorrente = Field(57, 67, 11, int)
    NumerodoRVoriginal = Field(68, 76, 9, int)
    DataRVoriginal = Field(77, 84, 8, date_factory, default='01011900')
    Valordocreditooriginal = Field(85, 99, 15, monetary_factory)
    Motivododebito = Field(100, 101, 2, int)
    Motivododebito = Field(102, 129, 28, str)
    Numerodocartao = Field(130, 145, 16, card_number_factory)
    Numerodereferenciadacartafax = Field(146, 160, 15, str)
    Mesdereferencia = Field(161, 166, 6, month_year_factory)
    Datadacarta = Field(167, 174, 8, int)
    Valordocancelamentosolicitado = Field(175, 189, 15, monetary_factory)
    Numerodoprocesso = Field(190, 204, 15, int)
    NoPVoriginal = Field(205, 213, 9, int)
    DatadatransacaoCV = Field(214, 221, 8, date_factory, default='01011900')
    NumerodoNSU = Field(222, 233, 12, int)
    Numerodoresumododebito = Field(234, 242, 9, int)
    Datadodebito = Field(243, 250, 8, date_factory)
    Valordatransacaooriginal = Field(251, 265, 15, monetary_factory)
    Numerodaautorizacao = Field(266, 271, 6, int, '-99999')
    Tipodedebito = Field(272, 272, 1, str)
    Valordodebitototal = Field(273, 287, 15, monetary_factory)
    Valorpendente = Field(288, 302, 15, monetary_factory)
    BandeiradoRVdeorigem = Field(303, 303, 1, str)


class Registro040Serasa(LineParser):
    codigo = '040'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    Quantidadedeconsultasrealizadasnoperiodo = Field(13, 17, 5, int)
    Valortotaldasconsultasnoperiodo = Field(18, 32, 15, monetary_factory)
    Iniciodoperiododaconsulta = Field(33, 40, 8, date_factory)
    Fimdoperiododaconsulta = Field(41, 48, 8, date_factory)
    Valorporconsultadesteperiodo = Field(49, 63, 15, monetary_factory)


class Registro041AVS(LineParser):
    codigo = '041'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    Quantidadedeconsultasrealizadasnoperiodo = Field(13, 17, 5, int)
    Valortotaldasconsultasnoperiodo = Field(18, 32, 15, monetary_factory)
    Iniciodoperiododaconsulta = Field(33, 40, 8, date_factory)
    Fimdoperiododaconsulta = Field(41, 48, 8, date_factory)
    Valorporconsultadesteperiodo = Field(49, 63, 15, monetary_factory)


class Registro042SecureCode(LineParser):
    codigo = '042'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    Quantidadedeconsultasrealizadasnoperiodo = Field(13, 17, 5, int)
    Valortotaldasconsultasnoperiodo = Field(18, 32, 15, monetary_factory)
    Iniciodoperiododaconsulta = Field(33, 40, 8, date_factory)
    Fimdoperiododaconsulta = Field(41, 48, 8, date_factory)
    Valorporconsultadesteperiodo = Field(49, 63, 15, monetary_factory)
    Bandeira = Field(64, 64, 1, str)


class Registro043AjustesacreditoExtratoEletronicoFinanceiro(LineParser):
    codigo = '043'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPVcreditado = Field(4, 12, 9, int)
    Numerodoresumodocredito = Field(13, 21, 9, int)
    Numerododocumento = Field(22, 32, 11, int)
    Datadaemissao = Field(33, 40, 8, date_factory)
    Datadocredito = Field(41, 48, 8, date_factory)
    Valordocredito = Field(49, 63, 15, monetary_factory)
    C = Field(64, 64, 1, str)
    Banco = Field(65, 67, 3, int)
    Agencia = Field(68, 73, 6, int)
    Contacorrente = Field(74, 84, 11, str)
    Motivodocredito = Field(85, 86, 2, int)
    Motivodocredito = Field(87, 114, 28, str)
    Bandeira = Field(115, 115, 1, str)


class Registro044Debitospendentes(LineParser):
    codigo = '044'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodaOrdemdeDebito = Field(13, 23, 11, int)
    DatadaOD = Field(24, 31, 8, date_factory)
    ValordaOD = Field(32, 46, 15, monetary_factory)
    Motivodoajuste = Field(47, 48, 2, int)
    Motivodoajuste = Field(49, 76, 28, str)
    Numerodocartao = Field(77, 92, 16, card_number_factory)
    NumerodoNSU = Field(93, 104, 12, int)
    DatadoCVoriginaldatransacao = Field(105, 112, 8, int)
    Numerodaautorizacao = Field(113, 118, 6, str)
    Valordatransacaooriginal = Field(119, 133, 15, monetary_factory)
    NumerodoRVoriginal = Field(134, 142, 9, int)
    DataRVoriginal = Field(143, 150, 8, int)
    NumerodoPVoriginal = Field(151, 159, 9, int)
    Numerodereferenciadacartafax = Field(160, 174, 15, str)
    Datadacarta = Field(175, 182, 8, int)
    Numerodoprocessodechargeback = Field(183, 197, 15, int)
    Mesdereferencia = Field(198, 203, 6, int)
    Valorcompensadopago = Field(204, 218, 15, monetary_factory)
    Datadopagamento = Field(219, 226, 8, int)
    Valorpendentededebito = Field(227, 241, 15, monetary_factory)
    Numerodeprocessoderetencao = Field(242, 256, 15, int, default='-99999')
    Meiodecompensacao = Field(257, 258, 2, int)
    Meiodecompensacao = Field(259, 286, 28, str)
    Identificaabandeira = Field(287, 287, 1, str)


class Registro055DebitosPendentesecommerce(LineParser):
    codigo = '055'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoCartao = Field(4, 19, 16, card_number_factory)
    NumerodoNSU = Field(20, 31, 12, int)
    DatadoCVoriginaldatransacao = Field(32, 39, 8, int)
    NumerodaAutorizacao = Field(40, 45, 6, str)
    ValordatransacaoOriginal = Field(46, 60, 15, monetary_factory)
    NumerodoRVoriginal = Field(61, 69, 9, int)
    NumerodoPVOriginal = Field(70, 78, 9, int)
    TID = Field(79, 98, 20, str)
    NumeroPedido = Field(99, 128, 30, str)


class Registro045Debitosliquidados(LineParser):
    codigo = '045'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPV = Field(4, 12, 9, int)
    NumerodaOrdemdeDebito = Field(13, 23, 11, int)
    DatadaOD = Field(24, 31, 8, date_factory)
    ValordaOD = Field(32, 46, 15, monetary_factory)
    Motivodoajuste = Field(47, 48, 2, int)
    Motivodoajuste = Field(49, 76, 28, str)
    Numerodocartao = Field(77, 92, 16, card_number_factory)
    NumerodoNSU = Field(93, 104, 12, int)
    DatadoCVoriginaldatransacao = Field(105, 112, 8, int)
    Numerodaautorizacao = Field(113, 118, 6, str)
    Valordatransacaooriginal = Field(119, 133, 15, monetary_factory)
    NumerodoRVoriginal = Field(134, 142, 9, int)
    DataRVoriginal = Field(143, 150, 8, int)
    NumerodoPVoriginal = Field(151, 159, 9, int)
    Numerodereferenciadacartafax = Field(160, 174, 15, str)
    Datadacarta = Field(175, 182, 8, int)
    Numerodoprocessodechargeback = Field(183, 197, 15, int)
    Mesdereferencia = Field(198, 203, 6, int)
    Valorliquidado = Field(204, 218, 15, monetary_factory)
    Datadaliquidacao = Field(219, 226, 8, int)
    Numerodeprocessoderetencao = Field(227, 241, 15, str)
    Meiodecompensacao = Field(242, 243, 2, int)
    Meiodecompensacao = Field(244, 271, 28, str)
    Identificaabandeira = Field(272, 272, 1, str)


class Registro056DebitosLiquidadosecommerce(LineParser):
    codigo = '056'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoCartao = Field(4, 19, 16, card_number_factory)
    NumerodoNSU = Field(20, 31, 12, int)
    DatadoCVoriginaldatransacao = Field(32, 39, 8, int)
    NumerodaAutorizacao = Field(40, 45, 6, str)
    ValordatransacaoOriginal = Field(46, 60, 15, monetary_factory)
    NumerodoRVoriginal = Field(61, 69, 9, int)
    NumerodoPVOriginal = Field(70, 78, 9, int)
    TID = Field(79, 98, 20, str)
    Numerodopedido = Field(99, 128, 30, str)


class Registro049Desagendamentodeparcelas(LineParser):
    codigo = '049'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPVoriginal = Field(4, 12, 9, int)
    NumerodoRVoriginal = Field(13, 21, 9, int)
    Numerodereferencia = Field(22, 36, 15, str)
    Datadocredito = Field(37, 44, 8, date_factory)
    Novovalordaparcela = Field(45, 59, 15, monetary_factory)
    Valororiginaldaparcelaalterada = Field(60, 74, 15, monetary_factory)
    Valordoajuste = Field(75, 89, 15, monetary_factory)
    Datadocancelamento = Field(90, 97, 8, date_factory)
    ValordoRVoriginal = Field(98, 112, 15, monetary_factory)
    Valordocancelamentosolicitado = Field(113, 127, 15, monetary_factory)
    Numerodocartao = Field(128, 143, 16, card_number_factory)
    Datadatransacao = Field(144, 151, 8, date_factory)
    NSU = Field(152, 163, 12, int)
    Tipodedebito = Field(164, 164, 1, int)
    Numerodaparcela = Field(165, 166, 2, int)
    BandeiradoRVdeorigem = Field(167, 167, 1, str)


class Registro057DesagendamentodeParcelasecommerce(LineParser):
    codigo = '057'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPVoriginal = Field(4, 12, 9, int)
    NumerodoRVoriginal = Field(13, 21, 9, int)
    ValordoRVoriginal = Field(98, 112, 15, monetary_factory)
    Numerodocartao = Field(128, 143, 16, card_number_factory)
    Datadatransacao = Field(144, 151, 8, date_factory, default='01011900')
    NSU = Field(152, 163, 12, int, default='-99999')
    TID = Field(165, 166, 20, str)
    Numerodopedido = Field(167, 196, 30, str)


class Registro050TotalizadorMatriz(LineParser):
    codigo = '057'
    Tipoderegistro = Field(1, 3, 3, int)
    NoPVmatriz = Field(4, 12, 9, int)
    Quantidadetotalderesumosmatriz = Field(13, 18, 6, int)
    Valortotaldoscreditosnormais = Field(19, 33, 15, monetary_factory)
    Quantidadedecreditosantecipados = Field(34, 39, 6, int)
    Valortotalantecipado = Field(40, 54, 15, monetary_factory)
    Quantidadedeajustesacredito = Field(55, 58, 4, int)
    Valortotaldeajustesacredito = Field(59, 73, 15, monetary_factory)
    Quantidadedeajustesadebito = Field(74, 79, 6, int)
    Valortotaldeajustesadebito = Field(80, 94, 15, monetary_factory)


class Registro050TotalizadorMatriz(LineParser):
    codigo = '050'
    Tipoderegistro = Field(1, 3, 3, int)
    NoPVmatriz = Field(4, 12, 9, int)
    Quantidadetotalderesumosmatriz = Field(13, 18, 6, int)
    Valortotaldoscreditosnormais = Field(19, 33, 15, monetary_factory)
    Quantidadedecreditosantecipados = Field(34, 39, 6, int)
    Valortotalantecipado = Field(40, 54, 15, monetary_factory)
    Quantidadedeajustesacredito = Field(55, 58, 4, int)
    Valortotaldeajustesacredito = Field(59, 73, 15, monetary_factory)
    Quantidadedeajustesadebito = Field(74, 79, 6, int)
    Valortotaldeajustesadebito = Field(80, 94, 15, monetary_factory)


class Registro052Trailerdoarquivo(LineParser):
    codigo = '052'
    Tipoderegistro = Field(1, 3, 3, int)
    Quantidadedematrizesnoarquivo = Field(4, 7, 4, int)
    Quantidadederegistrosnoarquivo = Field(8, 13, 6, int)
    NoPVgrupo = Field(14, 22, 9, int)
    Quantidadetotalderesumosgrupo = Field(23, 26, 4, int)
    Valortotaldoscreditosnormais = Field(27, 41, 15, monetary_factory)
    Quantidadedecreditosantecipados = Field(42, 47, 6, int)
    Valortotalantecipado = Field(48, 62, 15, monetary_factory)
    Quantidadedeajustesacredito = Field(63, 66, 4, int)
    Valortotaldeajustesacredito = Field(67, 81, 15, monetary_factory)
    Quantidadedeajustesadebito = Field(82, 85, 4, int)
    Valortotaldeajustesadebito = Field(86, 100, 15, monetary_factory)


class Registro053AjustesNETedesagendamentosecommerce7(LineParser):
    codigo = '053'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoCartao = Field(4, 19, 16, card_number_factory)
    DatadaTransacaoCV = Field(20, 27, 8, int)
    NumerodoRVoriginal = Field(28, 36, 9, int)
    NoPVOriginal = Field(37, 45, 9, int)
    Valordatransacao = Field(46, 60, 15, monetary_factory)
    NumerodoNSU = Field(61, 72, 12, int)
    Numerodaautorizacao = Field(73, 78, 6, str)
    TID = Field(79, 98, 20, str)
    NumeroPedido = Field(99, 128, 30, str)


class Registro034Creditos(LineParser):
    codigo = '034'
    Tipoderegistro = Field(1, 3, 3, int)
    NumerodoPVcentralizador = Field(4, 12, 9, int)
    Numerododocumento = Field(13, 23, 11, int)
    Datadolancamento = Field(24, 31, 8, date_factory)
    Valordolancamento = Field(32, 46, 15, monetary_factory)
    C = Field(47, 47, 1, str)
    Banco = Field(48, 50, 3, int)
    Agencia = Field(51, 56, 6, int)
    Contacorrente = Field(57, 67, 11, int)
    Datadomovimento = Field(68, 75, 8, date_factory, default='01011900')
    NumerodoRV = Field(76, 84, 9, int)
    DatadoRV = Field(85, 92, 8, date_factory)
    Bandeira = Field(93, 93, 1, str)
    Tipodetransacao = Field(94, 94, 1, int)
    ValorbrutodoRV = Field(95, 109, 15, monetary_factory)
    Valordataxadedesconto = Field(110, 124, 15, monetary_factory)
    Numerodaparcelatotal = Field(125, 129, 5, str)
    StatusdocreditoTabelaII = Field(130, 131, 2, str)
    NoPVoriginal = Field(132, 140, 9, int)


if __name__ == '__main__':
    V = locals().values()
    parsers = {_.codigo: _ for _ in V if isinstance(_, LineParserMeta) and hasattr(_, 'codigo')}
    csv_files = {k: open(f'/tmp/o/{v.__name__}.csv', 'w') for k, v in parsers.items()}

    for csv, cls in zip(csv_files.values(), parsers.values()):
        csv.write(','.join(cls.headers()))
        csv.write('\n')


    with open(sys.argv[1]) as fi:
        for row in fi.read().split('\n'):
            if not row:
                continue
            codigo = row[:3]
            line = parsers[codigo](row)
            csv_files[codigo].write(','.join(line.values_as_str()))
            csv_files[codigo].write('\n')

    for csv in csv_files.values():
        csv.close()
