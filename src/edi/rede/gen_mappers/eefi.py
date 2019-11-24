from edi.rede.gen_mappers.utils import Table, to_class


tables = [
Table('030', 'Registro 030 - Header de arquivo',
'''            001             003        003           Num.         Tipo de registro (“030”)
               004             011        008           Num.         Data de emissão (DDMMAAAA)
               012             019        008            Alfa        “Rede”
               020             053        034            Alfa        “Extrato de movimentação financeira”
               054             075        022            Alfa        Nome comercial (grupo/matriz)
               076             081        006           Num.         Sequência do movimento
               082             090        009           Num.         Nº-PVgrupo oumatriz
               091             105        015            Alfa        Tipo de processamento
               106             125        020            Alfa        Versão do arquivo'''),
Table('032', 'Registro 032 - Header – Matriz',
'''            001             003        003           Num.         Tipo de registro (“032”)
               004             012        009            Alfa        Nº-PVmatriz
               013             034        022            Alfa        Nome comercial da matriz'''),
Table('035', 'Registro 035 - Ajustes Net e Desagendamentos',
'''           001          003         003        Num.     Tipo de registro (“035”)
              004          012         009        Num.     Número do PVajustado
              013          021         009        Num.     Número do RVajustado
              022          029         008        Num.     Data do ajuste (DDMMAAAA)
              030          044         015      9(13)V99   Valor do ajuste
              045          045         001        Alfa     D (Débito)
              046          047         002        Num.     Motivo do ajuste (cód. da tabela III)
              048          075         028        Alfa     Motivo do ajuste (string - tabelaIII)
              076          091         016        Num.     Número do cartão
              092          099         008        Num.     Data da transação“CV” (DDMMAAAA)
              100          108         009        Num.     Número do RVoriginal
              109          123         015        Alfa     Número de referência da carta/fax
              124          131         008        Num.     Data da carta (DDMMAAAA)
              132          137         006        Num.     Mês de referência (serviços, POSetc.) (MMAAAA)
              138          146         009        Num.     Nº-PVoriginal
              147          154         008        Alfa     Data RVoriginal (DDMMAAAA)
              155          169         015      9(13)V99   Valor da transação
              170          170         001        Alfa     D (Desagendamento) ou N (Net)
              171          178         008        Num.     Data do crédito (DDMMAAAA)
              179          193         015      9(13)V99   Novo valor da parcela
              194          208         015      9(13)V99   Valor original da parcela
              209          223         015      9(13)V99   Valor bruto do resumo de vendasoriginal
              224          238         015      9(13)V99   Valor do cancelamento solicitado
              239          250         012        Num.     Número do NSU (motivos 16, 18 e23)
              251          256         006        Alfa     Número da autorização
              257          257         001        Alfa     Tipo de débito
              258          268         011        Num.     Número da Ordem de Débito
              269          283         015      9(13)V99   Valor do débito total
              284          298         015      9(13)V99   Valor pendente
              299          299         001        Alfa     Bandeira do RVde origem (2)
              300          300         001        Alfa     Bandeira do RVajustado (2)'''),
Table('036', 'Registro 036 –Antecipações',
'''              001           003        003          Num.      Tipo de registro (“036”)
                 004           012        009          Num.      Número do PV
                 013           023        011          Num.      Número do documento
                 024           031        008          Num.      Data do lançamento(DDMMAAAA)
                 032           046        015         9(13)V99   Valor do lançamento
                 047           047        001           Alfa     C(Crédito)
                 048           050        003          Num.      Banco
                 051           056        006          Num.      Agência
                 057           067        011          Num.      Conta-corrente
                 068           076        009          Num.      Número do RVcorrespondente
                 077           084        008          Num.      Data do RVcorrespondente (DDMMAAAA)
                 085           099        015         9(13)V99   Valor do crédito original
                 100           107        008          Num.      Data do vencimento original(DDMMAAAA)
                 108           112        005           Alfa     Número da parcela/total
                 113           127        015         9(13)V99   Valor bruto
                 128           142        015         9(13)V99   Valor da taxa de desconto
                 143           151        009          Num.      Nº-PVoriginal
                 152           152        001           Alfa     Bandeira'''),
Table('037', 'Registro 037 – Totalizador de créditos',
'''           001            003       003          Num.      Tipo de registro (“037”)
              004            012       009          Num.      Número do PV
              013            019       007           Alfa     Brancos
              020            027       008          Num.      Data do crédito (DDMMAAAA)
              028            042       015         9(13)V99   Valor total do crédito
              043            043       001           Alfa     Brancos
              044            046       003          Num.      Número do banco
              047            052       006          Num.      Número da agência
              053            063       011          Num.      Número da conta-corrente
              064            071       008          Num.      Data da geração do arquivo (DDMMAAAA)
              072            079       008          Num.      Data do crédito antecipado(DDMMAAAA)
              080            094       015         9(13)V99   Valor total dos créditos antecipados'''),
Table('038', 'Registro 038 - Ajustes a débito (via banco)',
'''            001            003           003        Num.       Tipo de registro (“038”)
               004            012           009        Num.       Número do PV
               013            023           011        Num.       Número do documento
               024            031           008        Num.       Data da emissão (DDMMAAAA)
               032            046           015       9(13)V99    Valor do débito
               047            047           001         Alfa      D (Débito)
               048            050           003        Num.       Banco
               051            056           006        Num.       Agência
               057            067           011        Num.       Conta-corrente
               068            076           009        Num.       Número do RVoriginal
               077            084           008        Num.       Data RVoriginal (DDMMAAAA)
               085            099           015       9(13)V99    Valor do crédito original
               100            101           002        Num.       Motivo do débito (cód. da tabela itemIII)
               102            129           028       9(13)V99    Motivo do débito (String - tabela item III)
               130            145           016        Num.       Número do cartão
               146            160           015         Alfa      Número de referência da carta/fax
               161            166           006        Num.       Mês de referência (DDMMAAAA)       
               167            174           008        Num.       Data da carta
               175            189           015       9(13)V99    Valor do cancelamento solicitado
               190            204           015        Num.       Número do processo
               205            213           009        Num.       Nº-PVoriginal
               214            221           008        Num.       Data da transação“CV” (DDMMAAAA)
               222            233           012        Num.       Número do NSU (motivos 16, 18 e23)
               234            242           009        Num.       Número do resumo do débito
               243            250           008        Num.       Data do débito (DDMMAAAA)
               251            265           015       9(13)V99    Valor da transação original
               266            271           006        Num.       Número da autorização
               272            272           001         Alfa      Tipo de débito
               273            287           015       9(13)V99    Valor do débito total
               288            302           015       9(13)V99    Valor pendente
               303            303           001         Alfa      Bandeira do RVde origem (2)'''),
Table('040', 'Registro 040 –Serasa',
'''             001           003           003           Num.      Tipo de registro (“040”)
                004           012           009           Num.      Número do PV
                013           017           005           Num.      Quantidade de consultas realizadas no período
                018           032           015          9(13)V99   Valor total das consultas no período
                033           040           008           Num.      Início do período da consulta(DDMMAAAA)
                041           048           008           Num.      Fim do período da consulta (DDMMAAAA)
                049           063           015          9(13)V99   Valor por consulta deste período'''),
Table('041', 'Registro 041 -AVS',
'''           001              003        003          Num.       Tipo de registro (“041”)
              004              012        009          Num.       Número do PV
              013              017        005          Num.       Quantidade de consultas realizadas no período
              018              032        015         9(13)V99    Valor total das consultas no período
              033              040        008          Num.       Início do período da consulta(DDMMAAAA)
              041              048        008          Num.       Fim do período da consulta (DDMMAAAA)
              049              063        015         9(13)V99    Valor por consulta deste período'''),
Table('042', 'Registro 042 -SecureCode',
'''            001              003        003          Num.      Tipo de registro (“042”)
               004              012        009          Num.      Número do PV
               013              017        005          Num.      Quantidade de consultas realizadas no período
               018              032        015         9(13)V99   Valor total das consultas no período
               033              040        008          Num.      Início do período da consulta(DDMMAAAA)
               041              048        008          Num.      Fim do período da consulta (DDMMAAAA)
               049              063        015         9(13)V99   Valor por consulta deste período
                64              64         001           Alfa     Bandeira'''),
Table('043', 'Registro 043 - Ajustes a crédito (Extrato Eletrônico Financeiro)',
'''            001              003          003         Num.       Tipo de registro (“043”)
               004              012          009         Num.       Número do PVcreditado
               013              021          009         Num.       Número do resumo do crédito
               022              032          011         Num.       Número do documento
               033              040          008         Num        Data da emissão (DDMMAAAA)
               041              048          008         Num        Data do crédito (DDMMAAAA)
               049              063          015        9(13)V99    Valor do crédito
               064              064          001         Num.       C(Crédito)
               065              067          003         Num.       Banco
               068              073          006         Num.       Agência
               074              084          011          Alfa      Conta-corrente
               085              086          002         Num.       Motivo do crédito (cód. da tabelaIII)
               087              114          028          Alfa      Motivo do crédito(String)
               115              115          001          Alfa      Bandeira'''),
Table('044', 'Registro 044 - Débitos pendentes',
'''           001          003         003        Num.     Tipo de registro (“044”)
              004          012         009        Num.     Número do PV
              013          023         011        Num.     Número da Ordem de Débito
              024          031         008        Num.     Data da OD (DDMMAAAA)
              032          046         015      9(13)V99   Valor da OD
              047          048         002        Num.     Motivo do ajuste (cód. da tabela III)
              049          076         028        Alfa     Motivo do ajuste (String – tabelaIII)
              077          092         016        Num.     Número do cartão
              093          104         012        Num.     Número do NSU (motivos 16, 18 e23)
              105          112         008        Num.     Data do CVoriginal datransação
              113          118         006        Alfa     Número da autorização
              119          133         015      9(13)V99   Valor da transação original
              134          142         009        Num.     Número do RVoriginal
              143          150         008        Num.     Data RVoriginal
              151          159         009        Num.     Número do PVoriginal
              160          174         015        Alfa     Número de referência da carta/fax
              175          182         008        Num.     Data da carta
              183          197         015        Num.     Número do processo de chargeback
              198          203         006        Num.     Mês de referência (serviços, POSetc.)
              204          218         015      9(13)V99   Valor compensado/pago
              219          226         008        Num.     Data do pagamento
              227          241         015      9(13)V99   Valor pendente de débito
              242          256         015        Num.     Número de processo de retenção
              257          258         002        Num.     Meio de compensação (código)
              259          286         028        Alfa     Meio de compensação (String)
              287          287         001        Alfa     Identifica abandeira'''),
Table('055', 'Registro 055 - Débitos Pendentes - (e-commerce)',
'''             1              3               3           Num.       Tipo de registro (“055”)
                4              19           16             Num.       Número do Cartão
                20             31           12             Num.       Número do NSU (motivos 16, 18 e23)
                32             39              8           Num.       Data do CVoriginal datransação
                40             45              6            Alfa      Número da Autorização
                46             60           15            9(13)V99    Valor da transação Original
                61             69              9           Num.       Número do RVoriginal
                70             78              9           Num.       Número do PVOriginal
                79             98           20              Alfa      TID
                99             128          30              Alfa      Número Pedido'''),
Table('045', 'Registro 045 - Débitos liquidados',
'''              001          003        003           Num.      Tipo de registro (“045”)
                 004          012        009           Num.      Número do PV
                 013          023        011           Num.      Número da Ordem de Débito
                 024          031        008           Num.      Data da OD (DDMMAAAA)
                 032          046        015          9(13)V99   Valor da OD
                 047          048        002           Num.      Motivo do ajuste (cód. da tabela III)
                 049          076        028            Alfa     Motivo do ajuste (String – tabelaIII)
                 077          092        016           Num.      Número do cartão
                 093          104        012           Num.      Número do NSU (motivos 16, 18 e23)
                 105          112        008           Num.      Data do CVoriginal datransação
                 113          118        006            Alfa     Número da autorização
                 119          133        015          9(13)V99   Valor da transação original
                 134          142        009           Num.      Número do RVoriginal
                 143          150        008           Num.      Data RVoriginal
                 151          159        009           Num.      Número do PVoriginal
                 160          174        015            Alfa     Número de referência da carta/fax
                 175          182        008           Num.      Data da carta
                 183          197        015           Num.      Número do processo de chargeback
                 198          203        006           Num.      Mês de referência (serviços, POSetc.)
                 204          218        015          9(13)V99   Valor liquidado
                 219          226        008           Num.      Data da liquidação
                 227          241        015            Alfa     Número de processo de retenção
                 242          243        002           Num.      Meio de compensação (código)
                 244          271        028            Alfa     Meio de compensação (String)
                 272          272        001            Alfa     Identifica abandeira'''),
Table('056', 'Registro 056 - Débitos Liquidados - (e-commerce)',
'''             1               3              3           Num        Tipo de registro (“056”)
                4               19          16             Num        Número do Cartão
                20              31          12             Num        Número do NSU (motivos 16, 18 e23)
                32              39             8           Num        Data do CVoriginal datransação
                40              45             6            Alfa      Número da Autorização
                46              60          15            9(13)V99    Valor da transação Original
                61              69             9           Num        Número do RVoriginal
                70              78             9           Num        Número do PVOriginal
                79              98          20              Alfa      TID
                99             128          30              Alfa      Número do pedido'''),
Table('049', 'Registro 049 - Desagendamento de parcelas',
'''              001          003          003         Num.      Tipo de registro (“049”)
                 004          012          009         Num.      Número do PVoriginal
                 013          021          009         Num.      Número do RVoriginal
                 022          036          015         Alpha     Número de referência
                 037          044          008         Num.      Data do crédito (DDMMAAAA)
                 045          059          015        9(13)V99   Novo valor da parcela
                 060          074          015        9(13)V99   Valor original da parcela alterada
                 075          089          015        9(13)V99   Valor do ajuste
                 090          097          008         Num.      Data do cancelamento (DDMMAAAA)
                 098          112          015        9(13)V99   Valor do RVoriginal
                 113          127          015        9(13)V99   Valor do cancelamento solicitado
                 128          143          016         Num.      Número do cartão
                 144          151          008         Num.      Data da transação (DDMMAAAA)
                 152          163          012         Num.      NSU
                 164          164          001         Num.      Tipo de débito
                 165          166          002         Num.      Número da parcela
                 167          167          001          Alfa     Bandeira do RVde origem'''),
Table('057', 'Registro 057 - Desagendamento de Parcelas (e-commerce)',
'''              1               3               3            Num        Tipo de registro (“057”)
                 4             12                9            Num        Número do PVoriginal
                 13            21                9            Num        Número do RVoriginal
                 98            112               15          9(13)V99    Valor do RVoriginal
               128             143               16           Num        Número do cartão
               144             151               8            Num        Data da transação
               152             163               12           Num        NSU
               165             166               20            Alfa      TID
               167             196               30            Alfa      Número do pedido'''),
Table('057', 'Registro 050 - Totalizador - Matriz',
'''              001           003            003         Num.      Tipo de registro (“050”)
                 004           012            009         Num.      Nº PVmatriz
                 013           018            006         Num.      Quantidade total de resumosmatriz
                 019           033            015       9(13)V99    Valor total dos créditos normais
                 034           039            006         Num.      Quantidade de créditos antecipados
                 040           054            015       9(13)V99    Valor total antecipado
                 055           058            004         Num.      Quantidade de ajustes acrédito
                 059           073            015       9(13)V99    Valor total de ajustes a crédito
                 074           079            006         Num.      Quantidade de ajustes adébito
                 080           094            015       9(13)V99    Valor total de ajustes adébito'''),
Table('050', 'Registro 050 - Totalizador - Matriz',
'''              001           003            003         Num.      Tipo de registro (“050”)
                 004           012            009         Num.      Nº PVmatriz
                 013           018            006         Num.      Quantidade total de resumosmatriz
                 019           033            015       9(13)V99    Valor total dos créditos normais
                 034           039            006         Num.      Quantidade de créditos antecipados
                 040           054            015       9(13)V99    Valor total antecipado
                 055           058            004         Num.      Quantidade de ajustes acrédito
                 059           073            015       9(13)V99    Valor total de ajustes a crédito
                 074           079            006         Num.      Quantidade de ajustes adébito
                 080           094            015       9(13)V99    Valor total de ajustes adébito'''),
Table('052', 'Registro 052 - Trailer do arquivo',
'''              001             003            003         Num.      Tipo de registro (“052”)
               004             007            004         Num.      Quantidade de matrizes no arquivo
               008             013            006         Num.      Quantidade de registros no arquivo
               014             022            009         Num.      Nº PVgrupo
               023             026            004         Num.      Quantidade total de resumosgrupo
               027             041            015       9(13)V99    Valor total dos créditos normais
               042             047            006         Num.      Quantidade de créditos antecipados
               048             062            015       9(13)V99    Valor total antecipado
               063             066            004         Num.      Quantidade de ajustes acrédito
               067             081            015       9(13)V99    Valor total de ajustes a crédito
               082             085            004         Num.      Quantidade de ajustes adébito
               086             100            015       9(13)V99    Valor total de ajustes adébito'''),
Table('053', 'Registro 053 - Ajustes NET e desagendamentos (e-commerce) 7',
'''              1              3          3           Num.      Tipo de registro (“053”)
                 4              19        16           Num.      Número do Cartão
                 20             27         8           Num.      Data da Transação“CV”
                 28             36         9           Num.      Número do RVoriginal
                 37             45         9           Num.      Nº PVOriginal
                 46             60        15          9(13)V99   Valor da transação
                 61             72        12           Num.      Número do NSU (motivos 16, 18 e23)
                 73             78         6            Alfa     Número da autorização
                 79             98        20            Alfa     TID
                 99            128        30            Alfa     Número Pedido'''),
Table('034', 'Registro 034 -Créditos',
'''            001             003     003           Num.       Tipo de registro (“034”)
               004             012     009           Num.       Número do PVcentralizador
               013             023     011           Num.       Número do documento
               024             031     008           Num.       Data do lançamento(DDMMAAAA)
               032             046     015          9(13)V99    Valor do lançamento
               047             047     001            Alfa      C(Crédito)
               048             050     003           Num.       Banco
               051             056     006           Num.       Agência
               057             067     011           Num.       Conta-corrente
               068             075     008           Num.       Data do movimento (DDMMAAAA)
               076             084     009           Num.       Número do RV
               085             092     008           Num.       Data do RV(DDMMAAAA)
               093             093     001            Alfa      Bandeira
               094             094     001           Num.       Tipo de transação
               095             109     015          9(13)V99    Valor bruto do RV
               110             124     015          9(13)V99    Valor da taxa de desconto
               125             129     005            Alfa      Número da parcela/total
               130             131     002            Alfa      Status do crédito - TabelaII
               132             140     009           Num.       Nº-PVoriginal'''),
]

if __name__ == '__main__':
    for t in tables:
        to_class(t)
        print()
        print()

