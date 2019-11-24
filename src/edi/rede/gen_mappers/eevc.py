from rede.gen_mappers.utils import Table, to_class


tables = [
Table('035', 'Registro 35 - CV / NSU Parcelado s/ juros (e-commerce)',
'''            001             003              3            Num.       Tipo de registro ("035")
               004             012              9            Num        Número do PV
               013             021              9            Num        Número do RV
               022             029              8            Num        Data do CV / NSU (DDMMAAAA)
               030             044              15          9(13)V99    Valor do CV / NSU
               045             060              16            Alfa      Número do cartão
               061             072              12           Num        Número do CV / NSU
               073             078              6             Alfa      Nº Autorização
               079             098              20            Alfa      TID
               099             128              30            Alfa      Número Pedido'''),
Table('012', 'Registro 12 - CV/NSU parcelado s/juros',
'''            001            003       003           Num.      Tipo de registro (“012”)
               004            012       009           Num.      Número do PV
               013            021       009           Num.      Número do RV
               022            029       008           Num.      Data do CV/NSU (DDMMAAAA)
               030            037       008           Num.      Zeros
               038            052       015          9(13)V99   Valor do CV/NSU
               053            067       015          9(13)V99   Valor da gorjeta
               068            083       016            Alfa     Número do cartão
               084            086       003            Alfa     Status do CV/NSU (1)
               087            088       002           Num.      Número de parcelas
               089            100       012           Num.      Número do CV/NSU
               101            113       013            Alfa     Número de referência
               114            128       015          9(13)V99   Valor do desconto
               129            134       006            Alfa     Nº da autorização
               135            140       006           Num.      Hora da transação (HHMMSS)
               141            156       016            Alfa     Nº do bilhete
               157            172       016            Alfa     Nº do bilhete
               173            188       016            Alfa     Nº do bilhete
               189            204       016            Alfa     Nº do bilhete
               205            205       001            Alfa     Tipo de captura
               206            220       015          9(13)V99   Valor líquido do CV/NSU
               221            235       015          9(13)V99   Valor líquido da primeira parcela
               236            250       015          9(13)V99   Valor líquido das demais parcelas
               251            258       008            Alfa     Número do terminal
               259            261       003            Alfa     Sigla do país
               262            262       001            Alfa     Bandeira'''),
Table('014', 'Registro 014 - Parcelas - Parcelado sem juros',
'''              001           003        003           Num.       Tipo de registro (“014”)
                 004           012        009           Num.       Número do PV
                 013           021        009           Num.       Número do RV
                 022           029        008           Num.       Data do RV(DDMMAAAA)
                 030           037        008           Num.       Brancos
                 038           039        002           Num.       Número da parcela
                 040           054        015          9(13)V99    Valor da parcela bruto
                 055           069        015          9(13)V99    Valor do desconto sobre aparcela
                 070           084        015          9(13)V99    Valor da parcela líquida
                 085           092        008           Num.       Data do crédito (DDMMAAAA)
                 093           1024       932            Alfa      Livre'''),
Table('008', 'Registro 008 – CV/NSU rotativo',
'''001            003      003           Num.     Tipo de registro (“008”)
   004            012      009           Num.     Número do PV
   013            021      009           Num.     Número do RV
   022            029      008           Num.     Data do CV/NSU (DDMMAAAA)
   030            037      008           Num.     Zeros
   038            052      015         9(13)V99   Valor do CV/NSU
   053            067      015         9(13)V99   Valor da gorjeta
   068            083      016           Alfa     Número do cartão
   084            086      003           Alfa     Status do CV/NSU (4)
   087            098      012           Num.     Número do CV/NSU
   099            111      013           Alfa     Número de referência
   112            126      015         9(13)V99   Valor do desconto
   127            132      006           Alfa     Nº autorização
   133            138      006           Num.     Hora da transação (HHMMSS)
   139            154      016           Alfa     Nº do bilhete
   155            170      016           Alfa     Nº do bilhete
   171            186      016           Alfa     Nº do bilhete
   187            202      016           Alfa     Nº do bilhete
   203            203      001           Alfa     Tipo de captura
   204            218      015         9(13)V99   Valor líquido
   219            226      008           Alfa     Número do terminal
   227            229      003           Alfa     Sigla do país
   230            230      001           Alfa     Bandeira'''),
Table('034', 'Registro 034 – CV/NSU Rotativo (e-commerce)',
'''              1              3       3          Num        Tipo de registro (“034”)
                 4             12       9          Num        Número do PV
                13             21       9          Num        Número do RV
                22             29       8          Num        Data do CV / NSU (DDMMAAAA)
                30             44      15        9(13)V99     Valor do CV / NSU
                45             60      16           Alfa      Número do cartão
                61             72      12          Num        Número do CV / NSU
                73             78       6           Alfa      Nº Autorização
                79             98      20           Alfa      TID
                99             128     30           Alfa      Número do Pedido'''),
Table('010', 'Registro 010 - RV parcelado sem juros',
'''           001             003       003           Num.       Tipo de registro (“010”)
              004             012       009           Num.       Número do PV
              013             021       009           Num.       Número do RV
              022             024       003           Num.       Nº do banco
              025             029       005           Num.       Nº da agência
              030             040       011           Num.       Nº da conta-corrente
              041             048       008           Num.       Data do RV(DDMMAAAA)
              049             053       005           Num.       Quantidade de CV/NSUs
              054             068       015          9(13)V99    Valor bruto
              069             083       015          9(13)V99    Valor da gorjeta
              084             098       015          9(13)V99    Valor rejeitado
              099             113       015          9(13)V99    Valor do desconto
              114             128       015          9(13)V99    Valor líquido
              129             136       008           Num.       Data de crédito da 1ª parcela(DDMMAAAA)
              137             137       001            Alfa      Bandeira (2)'''),
Table('006', 'Registro 006 - RV rotativo',
'''       001             003      003           Num.        Tipo de registro (“006”)
          004             012      009           Num.        Número do PV
          013             021      009           Num.        Número do RV
          022             024      003           Num.        Nº do banco
          025             029      005           Num.        Nº da agência
          030             040      011           Num.        Nº da conta-corrente
          041             048      008           Num.        Data do RV(DDMMAAAA)
          049             053      005           Num.        Quantidade de CV/NSUs acatados (somenteaprovadas)
          054             068      015         9(13)V99      Valor bruto
          069             083      015         9(13)V99      Valor da gorjeta
          084             098      015         9(13)V99      Valor rejeitado (transações manuais eTO)
          099             113      015         9(13)V99      Valor do desconto
          114             128      015         9(13)V99      Valor líquido
          129             136      008           Num.        Data de crédito (DDMMAAAA)
          137             137      001            Alfa       Bandeira (2)'''),
Table('028', 'Registro 028 - Trailer de arquivo',
'''            001               003        003           Num.       Tipo de registro (“028”) - Trailer de arquivo
               004               007        004           Num.       Quantidade de matrizes
               008               013        006           Num.       Quantidade de registros
               014               022        009            Alfa      Nº PVgrupo
               023               037        015          9(13)V99    Valor total bruto
               038               043        006           Num.       Quantidade de CV/NSUs rejeitados
               044               058        015          9(13)V99    Valor total rejeitado
               059               073        015          9(13)V99    Valor total rotativo
               074               088        015          9(13)V99    Valor total parcelado semjuros
               089               103        015          9(13)V99    Valor total parcelado IATA
               104               118        015          9(13)V99    Valor total dólar
               119               133        015          9(13)V99    Valor total desconto
               134               148        015          9(13)V99    Valor total líquido
               149               163        015         9(13)V999    Valor total gorjeta
               164               178        015          9(13)V99    Valor total da taxa de embarque
               179               184        006           Num.       Quant. CV/NSU acatados'''),
Table('026', 'Registro 026 - Totalizador – Matriz',
'''            001             003      003           Num.       Tipo de registro (“026”)
               004             012      009            Alfa      Nº PVmatriz
               013             027      015          9(13)V99    Valor total bruto
               028             033      006           Num.       Quantidade de CV/NSUs rejeitados
               034             048      015          9(13)V99    Valor total rejeitado
               049             063      015          9(13)V99    Valor total rotativo
               064             078      015          9(13)V99    Valor total parcelado semjuros
               079             093      015          9(13)V99    Valor total parcelado IATA
               094             108      015          9(13)V99    Valor total dólar
               109             123      015          9(13)V99    Valor total desconto
               124             138      015          9(13)V99    Valor total líquido
               139             153      015          9(13)V99    Valor total da gorjeta
               154             168      015          9(13)V99    Valor total da taxa de embarque
               169             174      006           Num.       Quant. CV/NSU acatados'''),
Table('004', 'Registro 004 - Header matriz',
'''            001             003       003            Num.         Tipo de registro (“004”)
               004             012       009             Alfa        Nº-PVmatriz
               013             034       022             Alfa        Nome comercial da matriz'''),
Table('002', 'Registro 002 – Header do Arquivo',
'''            001             003       003            Num.         Tipo de registro (“002”)
               004             011       008            Num.         Data de emissão (DDMMAAAA)
               012             019       008             Alfa        “Rede”
               020             049       030             Alfa        “Extrato Eletrônico de Vendas”
               050             071       022             Alfa        Nome comercial (grupo/matriz)
               072             077       006            Num.         Sequência do movimento
               078             086       009            Num.         Nº PVgrupo ou matriz
               087             101       015             Alfa        Tipo de movimento
               102             121       020             Alfa        Versão do arquivo
               122             1024      903             Alfa        Livre'''),
Table('005', 'Registro 005 –Request 6',
'''            001              003      003           Num.       Tipo de registro (“005”)
               004              012      009           Num.       Número do PV
               013              021      009           Num.       Número do RV
               022              037      016            Alfa      Número do cartão
               038              052      015          9(13)V99    Valor da transação“CV/NSU”
               053              060      008           Num.       Data da transação “CV/NSU” (DDMMAAAA)
               061              075      015           Num.       Número de Referência
               076              090      015           Num.       Número do processo
               091              102      012           Num.       Número do CV/NSU
               103              108      006            Alfa      Nº-de autorização
               109              112      004            Alfa      Código do Request
               113              120      008           Num.       Limite de envio dos documentos(DDMMAAAA)
               121              121      001            Alfa      Bandeira (2)
               122            1024       903            Alfa      Livre'''),
Table('011', 'Registro 011 - Ajustes a crédito – Extrato Eletrônico de Vendas',
'''            001             003         003           Num.       Tipo de registro (“011”)
               004             012         009           Num.       Número do PVcreditado
               013             021         009           Num.       Número do resumo do crédito
               022             029         008           Num.       Data do ajuste (DDMMAAAA)
               030             044         015          9(13)V99    Valor do ajuste
               045             052         008           Num.       Data do crédito (DDMMAAAA)
               053             067         015          9(13)V99    Valor do crédito
               068             068         001           Num.       C(Crédito)
               069             071         003           Num.       Banco
               072             077         006           Num.       Agência
               078             088         011           Num.       Conta-corrente
               089             090         002           Num.       Motivo do ajuste (cód. da tabelaV)
               091             118         028            Alfa      Descrição do ajuste (String)
               119             119         001            Alfa      Bandeira'''),
]

if __name__ == '__main__':
    for t in tables:
        to_class(t)
        print()
        print()

