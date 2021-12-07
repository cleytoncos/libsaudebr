import random

sigtap_outros_desc_list = [
    'ATIVIDADE EDUCATIVA / ORIENTAÇÃO EM GRUPO NA ATENÇÃO PRIMÁRIA',
    'PRÁTICA CORPORAL / ATIVIDADE FÍSICA EM GRUPO',
    'PREVENÇÃO DA COVID-19 NAS ESCOLAS',
    'AÇÃO COLETIVA DE APLICAÇÃO TÓPICA DE FLÚOR GEL',
    'AÇÃO COLETIVA DE BOCHECHO FLUORADO',
    'AÇÃO COLETIVA DE ESCOVAÇÃO DENTAL SUPERVISIONADA',
    'AÇÃO COLETIVA DE EXAME BUCAL COM FINALIDADE EPIDEMIOLÓGICA',
    'APLICAÇÃO DE CARIOSTÁTICO (POR DENTE)',
    'APLICAÇÃO DE SELANTE (POR DENTE)',
    'APLICAÇÃO TÓPICA DE FLÚOR (INDIVIDUAL POR SESSÃO)',
    'EVIDENCIAÇÃO DE PLACA BACTERIANA',
    'SELAMENTO PROVISÓRIO DE CAVIDADE DENTÁRIA',
    'ORIENTAÇÃO DE HIGIENE BUCAL',
    'AÇÃO COLETIVA DE PREVENÇÃO DE CÂNCER BUCAL',
    'ORIENTAÇÃO DE HIGIENIZAÇÃO DE PRÓTESES DENTÁRIAS',
    'VISITA DOMICILIAR POR PROFISSIONAL DE NÍVEL MÉDIO',
    'VISITA DOMICILIAR/INSTITUCIONAL POR PROFISSIONAL DE NÍVEL SUPERIOR',
    'AVALIAÇÃO ANTROPOMÉTRICA',
    'APLICAÇÃO DE SUPLEMENTOS DE MICRONUTRIENTES',
    'PRATICAS CORPORAIS EM MEDICINA TRADICIONAL CHINESA',
    'TERAPIA COMUNITÁRIA',
    'YOGA',
    'OFICINA DE MASSAGEM/ AUTO-MASSAGEM',
    'SESSÃO DE ARTETERAPIA',
    'SESSÃO DE MEDITAÇÃO',
    'SESSÃO DE MUSICOTERAPIA',
    'SESSÃO DE ANTROPOSOFIA APLICADA À SAÚDE',
    'SESSÃO DE BIODANÇA',
    'SESSÃO DE BIOENERGÉTICA',
    'SESSÃO DE CONSTELAÇÃO FAMILIAR',
    'SESSÃO DE DANÇA CIRCULAR',
    'SESSÃO DE TERMALISMO',
    'COLETA DE LINFA PARA PESQUISA DE M. LEPRAE',
    'COLETA DE MATERIAL DO COLO DE ÚTERO PARA EXAME CITOPATOLÓGICO',
    'COLETA DE MATERIAL PARA EXAME LABORATORIAL',
    'COLETA DE SANGUE PARA TRIAGEM NEONATAL',
    'PESQUISA DE PLASMODIO',
    'INTRADERMORREACAO COM DERIVADO PROTEICO PURIFICADO (PPD)',
    'PESQUISA DE GONADOTROFINA CORIONICA',
    'RADIOGRAFIA INTERPROXIMAL (BITE WING)',
    'RADIOGRAFIA PERIAPICAL',
    'GLICEMIA CAPILAR',
    'PESQUISA DE CORPOS CETONICOS NA URINA',
    'PESQUISA DE GLICOSE NA URINA',
    'CONSULTA AO PACIENTE CURADO DE TUBERCULOSE (TRATAMENTO SUPERVISIONADO)',
    'CONSULTA COM IDENTIFICAÇÃO DE CASOS NOVOS DE TUBERCULOSE',
    'CONSULTA DE PROFISSIONAIS DE NÍVEL SUPERIOR NA ATENÇÃO PRIMÁRIA (EXCETO MÉDICO)',
    'CONSULTA MEDICA EM ATENÇÃO PRIMÁRIA',
    'CONSULTA PARA AVALIAÇÃO CLÍNICA DO FUMANTE',
    'CONSULTA PRÉ-NATAL',
    'CONSULTA PUERPERAL',
    'CONSULTA/ATENDIMENTO DOMICILIAR',
    'PRIMEIRA CONSULTA ODONTOLOGICA PROGRAMÁTICA',
    'CONSULTA PRÉ-NATAL DO PARCEIRO',
    'TELECONSULTA NA ATENÇÃO PRIMÁRIA',
    'AVALIAÇÃO DO CRESCIMENTO NA PUERICULTURA',
    'AVALIAÇÃO DO DESENVOLVIMENTO DA CRIANÇA NA PUERICULTURA',
    'AVALIAÇÃO DO ESTÁGIO DE MATURAÇÃO SEXUAL',
    'ATENDIMENTO DE ADOLESCENTES EM CUMPRIMENTO DE MEDIDAS SOCIOEDUCATIVAS',
    'ATENDIMENTO CLÍNICO PARA INDICAÇÃO E FORNECIMENTO DO DIAFRAGMA UTERINO',
    'ESCUTA INICIAL / ORIENTAÇÃO (ACOLHIMENTO A DEMANDA ESPONT NEA)',
    'ATENDIMENTO EM GRUPO NA ATENÇÃO PRIMÁRIA',
    'INSERÇÃO DO DISPOSITIVO INTRA-UTERINO (DIU)',
    'RETIRADA DO DISPOSITIVO INTRA-UTERINO (DIU)',
    'ASSISTÊNCIA DOMICILIAR POR EQUIPE MULTIPROFISSIONAL.',
    'ASSISTÊNCIA DOMICILIAR POR PROFISSIONAL DE NÍVEL MÉDIO',
    'ANTIBIOTICOTERAPIA PARENTERAL',
    'ATENDIMENTO MEDICO COM FINALIDADE DE ATESTAR ÓBITO',
    'VISITA DOMICILIAR PÓS ÓBITO',
    'ADMINISTRAÇÃO DE IMUNODERIVADOS (ORAL E/OU PARENTERAL)',
    'TERAPIA DE REIDRATAÇÃO PARENTERAL',
    'BUSCA ATIVA',
    'VISITA DOMICILIAR POR PROFISSIONAL DE NÍVEL SUPERIOR',
    'ACOMPANHAMENTO DE PACIENTE EM TERAPIA NUTRICIONAL',
    'ATENDIMENTO DE URGÊNCIA EM ATENÇÃO BÁSICA',
    'ATENDIMENTO DE URGÊNCIA EM ATENÇÃO PRIMÁRIA COM OBSERVAÇÃO ATÉ 8 HORAS',
    'ATENDIMENTO DE URGÊNCIA EM ATENÇÃO PRIMÁRIA COM REMOÇÃO',
    'ESTIMULAÇÃO PRECOCE PARA DESENVOLVIMENTO NEUROPSICOMOTOR',
    'ABORDAGEM COGNITIVA COMPORTAMENTAL DO FUMANTE (POR ATENDIMENTO / PACIENTE)',
    'AVALIAÇÃO MULTIDIMENSIONAL DA PESSOA IDOSA',
    'AFERIÇÃO DE PRESSÃO ARTERIAL',
    'CATETERISMO VESICAL DE DEMORA',
    'LAVAGEM GASTRICA',
    'ORDENHA MAMÁRIA',
    'OXIGENOTERAPIA POR DIA',
    'SONDAGEM GÁSTRICA',
    'TERAPIA DE REIDRATAÇÃO ORAL',
    'ADMINISTRAÇÃO DE MEDICAMENTOS POR VIA SUBCUTÂNEA (SC)',
    'PREPARAÇÃO PARA O ELETROCARDIOGRAMA',
    'ATENDIMENTO DE PACIENTE EM CUIDADOS PALIATIVOS',
    'REMOÇÃO MANUAL DE FECALOMA',
    'CAPEAMENTO PULPAR',
    'RESTAURAÇÃO DE DENTE PERMANENTE ANTERIOR COM RESINA COMPOSTA',
    'TRATAMENTO INICIAL DO DENTE TRAUMATIZADO',
    'TRATAMENTO RESTAURADOR ATRAUMÁTICO (TRA/ART)',
    'RESTAURAÇÃO DE DENTE DECÍDUO POSTERIOR COM RESINA COMPOSTA',
    'RESTAURAÇÃO DE DENTE DECÍDUO POSTERIOR COM AMÁLGAMA',
    'RESTAURAÇÃO DE DENTE DECÍDUO POSTERIOR COM IONÔMERO DE VIDRO',
    'RESTAURAÇÃO DE DENTE DECÍDUO ANTERIOR COM RESINA COMPOSTA.',
    'RESTAURAÇÃO DE DENTE PERMANENTE POSTERIOR COM RESINA COMPOSTA',
    'RESTAURAÇÃO DE DENTE PERMANENTE POSTERIOR COM AMÁLGAMA',
    'ADEQUAÇÃO DO COMPORTAMENTO DA PESSOA COM DEFICIÊNCIA',
    'ADEQUAÇÃO DO COMPORTAMENTO DE CRIANÇAS',
    'ACESSO A POLPA DENTARIA E MEDICACAO (POR DENTE)',
    'CURATIVO DE DEMORA C/ OU S/ PREPARO BIOMECANICO',
    'PULPOTOMIA DENTÁRIA',
    'RASPAGEM ALISAMENTO SUBGENGIVAIS (POR SEXTANTE)',
    'PROFILAXIA / REMOÇÃO DA PLACA BACTERIANA',
    'RASPAGEM ALISAMENTO E POLIMENTO SUPRAGENGIVAIS (POR SEXTANTE)',
    'TRATAMENTO DE GENGIVITE ULCERATIVA NECROSANTE AGUDA (GUNA)',
    'TRATAMENTO DE LESÕES DA MUCOSA ORAL',
    'TRATAMENTO DE PERICORONARITE',
    'MOLDAGEM DENTO-GENGIVAL P/ CONSTRUCAO DE PROTESE DENTARIA',
    'CIMENTAÇÃO DE PRÓTESE DENTÁRIA',
    'ADAPTAÇÃO DE PRÓTESE DENTÁRIA',
    'AJUSTE OCLUSAL',
    'INSTALAÇÃO DE PRÓTESE DENTÁRIA',
    'MOLDAGEM DENTO-GENGIVAL COM FINALIDADE ORTODÔNTICA',
    'SESSÃO DE AURICULOTERAPIA',
    'SESSÃO DE MASSOTERAPIA',
    'TRATAMENTO TERMAL/CRENOTERÁPICO',
    'TRATAMENTO NATUROPÁTICO',
    'TRATAMENTO OSTEOPÁTICO',
    'TRATAMENTO QUIROPRÁTICO',
    'SESSÃO DE APITERAPIA',
    'SESSÃO DE AROMATERAPIA',
    'SESSÃO DE CROMOTERAPIA',
    'SESSÃO DE GEOTERAPIA',
    'SESSÃO DE HIPNOTERAPIA',
    'SESSÃO DE IMPOSIÇÃO DE MÃOS',
    'SESSÃO DE OZONIOTERAPIA APLICADA À ODONTOLOGIA',
    'SESSÃO DE TERAPIA DE FLORAIS',
    'TRATAMENTO HOMEOPÁTICO',
    'TRATAMENTO FITOTERÁPICO',
    'TRATAMENTO ANTROPOSÓFICO',
    'TRATAMENTO AYURVÉDICO',
    'TRATAMENTO EM MEDICINA TRADICIONAL CHINESA',
    'ASSISTÊNCIA AO PARTO SEM DISTOCIA',
    'EXCISÃO E/OU SUTURA SIMPLES DE PEQUENAS LESÕES / FERIMENTOS DE PELE / ANEXOS E MUCOSA',
    'FRENÉCTOMIA/FRENOTOMIA.',
    'ATENDIMENTO DE URGÊNCIA EM PEQUENO QUEIMADO',
    'EXODONTIA DE DENTE DECÍDUO',
    'EXODONTIA DE DENTE PERMANENTE',
    'GLOSSORRAFIA',
    'TRATAMENTO CIRÚRGICO DE HEMORRAGIA BUCO-DENTAL',
    'TRATAMENTO DE ALVEOLITE',
    'ULOTOMIA/ULECTOMIA',
    'EXODONTIA DE DENTE SUPRANUMERÁRIO',
    'ADESÃO A ASSISTÊNCIA PRE-NATAL - INCENTIVO PHPN (COMPONENTE I)',
    'CONCLUSÃO DA ASSISTÊNCIA PRE-NATAL (INCENTIVO)'
]

sigtap_outros_cod_list = [
    '0101010010',
    '0101010036',
    '0101010095',
    '0101020015',
    '0101020023',
    '0101020031',
    '0101020040',
    '0101020058',
    '0101020066',
    '0101020074',
    '0101020082',
    '0101020090',
    '0101020104',
    '0101020112',
    '0101020120',
    '0101030010',
    '0101030029',
    '0101040024',
    '0101040067',
    '0101050011',
    '0101050020',
    '0101050046',
    '0101050054',
    '0101050062',
    '0101050070',
    '0101050089',
    '0101050097',
    '0101050100',
    '0101050119',
    '0101050127',
    '0101050135',
    '0101050143',
    '0201020025',
    '0201020033',
    '0201020041',
    '0201020050',
    '0202020452',
    '0202030245',
    '0202050254',
    '0204010217',
    '0204010225',
    '0214010015',
    '0214010023',
    '0214010031',
    '0301010013',
    '0301010021',
    '0301010030',
    '0301010064',
    '0301010099',
    '0301010110',
    '0301010129',
    '0301010137',
    '0301010153',
    '0301010234',
    '0301010250',
    '0301010269',
    '0301010277',
    '0301010285',
    '0301010293',
    '0301040010',
    '0301040079',
    '0301040087',
    '0301040141',
    '0301040150',
    '0301050023',
    '0301050058',
    '0301050082',
    '0301050090',
    '0301050104',
    '0301050112',
    '0301050120',
    '0301050139',
    '0301050147',
    '0301050155',
    '0301060037',
    '0301060045',
    '0301060053',
    '0301070202',
    '0301080011',
    '0301090033',
    '0301100039',
    '0301100055',
    '0301100128',
    '0301100136',
    '0301100144',
    '0301100179',
    '0301100187',
    '0301100225',
    '0301100268',
    '0301140014',
    '0303070030',
    '0307010015',
    '0307010031',
    '0307010066',
    '0307010074',
    '0307010082',
    '0307010090',
    '0307010104',
    '0307010112',
    '0307010120',
    '0307010139',
    '0307010147',
    '0307010155',
    '0307020010',
    '0307020029',
    '0307020070',
    '0307030024',
    '0307030040',
    '0307030059',
    '0307030067',
    '0307030075',
    '0307030083',
    '0307040070',
    '0307040135',
    '0307040143',
    '0307040151',
    '0307040160',
    '0307040178',
    '0309050049',
    '0309050057',
    '0309050065',
    '0309050073',
    '0309050081',
    '0309050090',
    '0309050111',
    '0309050120',
    '0309050138',
    '0309050146',
    '0309050154',
    '0309050162',
    '0309050170',
    '0309050189',
    '0309050197',
    '0309050200',
    '0309050219',
    '0309050227',
    '0309050235',
    '0310010012',
    '0401010066',
    '0401010082',
    '0413010023',
    '0414020120',
    '0414020138',
    '0414020170',
    '0414020359',
    '0414020383',
    '0414020405',
    '0414020430',
    '0801010012',
    '0801010020'
]

def sigtap_outros_desc():
    sigtap = random.choice(sigtap_outros_desc_list)
    return sigtap

def sigtap_outros_cod():
    sigtap = random.choice(sigtap_outros_cod_list)
    return sigtap

def valida_cns(cns):
    if len(cns) != 15:
        cns_valido = 0
    else:
        if cns[0:1] in ("1","2"):
            pis = cns[0:11]
            soma_pis = (int(pis[0:1]) * 15) + (int(pis[1:2]) * 14) + (int(pis[2:3]) * 13) + (int(pis[3:4]) * 12) + (int(pis[4:5]) * 11) + (int(pis[5:6]) * 10) + (int(pis[6:7]) * 9) + (int(pis[7:8]) * 8) + (int(pis[8:9]) * 7) + (int(pis[9:10]) * 6) + (int(pis[10:11]) * 5)
            resto_pis = int(soma_pis) % 11
            dv_pis = 11 - resto_pis

            if dv_pis == 11:
                dv_pis = 0

            if dv_pis == 10:
                soma_pis = (str(int(pis[0:1]) * 15)) + (str(int(pis[1:2]) * 14)) + (str(int(pis[2:3]) * 13)) + (str(int(pis[3:4]) * 12)) + (str(int(pis[4:5]) * 11)) + (str(int(pis[5:6]) * 10)) + (str(int(pis[6:7]) * 9)) + (str(int(pis[7:8]) * 8)) + (str(int(pis[8:9]) * 7)) + (str(int(pis[9:10]) * 6)) + (str(int(pis[10:11]) * 5))
                soma_pis = int(soma_pis) + 2
                resto_pis = soma_pis % 11
                dv_pis = 11 - resto_pis
                resultado = str(pis) + "001" + str(dv_pis)
            else:
                resultado = str(pis) + "000" + str(dv_pis)
            if resultado != cns:
                cns_valido = 0
            else:
                cns_valido = 1
        else:
            soma_cns = (int(cns[0:1]) * 15) + (int(cns[1:2]) * 14) + (int(cns[2:3]) * 13) + (int(cns[3:4]) * 12) + (int(cns[4:5]) * 11) + (int(cns[5:6]) * 10) + (int(cns[6:7]) * 9) + (int(cns[7:8]) * 8) + (int(cns[8:9]) * 7) + (int(cns[9:10]) * 6) + (int(cns[10:11]) * 5) + (int(cns[11:12]) * 4) + (int(cns[12:13]) * 3) + (int(cns[13:14]) * 2) + (int(cns[14:15]) * 1)
            resto_cns = int(soma_cns) % 11

            if resto_cns != 0:
                cns_valido = 0
            else:
                cns_valido = 1
    return cns_valido

def cns():
    new_cns = []
    cns_valido = 0
    while cns_valido != 1:
        # Gera número aleatório de 1 até 3
        n1 = random.randint(0,2) + 1
        if n1 == 3:
            n1 = random.randint(0,2) + 7
        while len(new_cns) != 11:
            n2 = random.randint(0,99998) + 1
            n3 = random.randint(0,99998) + 1
            new_cns = str(n1) + ("0" + str(n2))[1:6] + ("0" + str(n3))[1:6]
            str(new_cns)
        soma = 0
        soma = (int(new_cns[0:1]) * 15) + (int(new_cns[1:2]) * 14) + (int(new_cns[2:3]) * 13) + (int(new_cns[3:4]) * 12) + (int(new_cns[4:5]) * 11) + (int(new_cns[5:6]) * 10) + (int(new_cns[6:7]) * 9) + (int(new_cns[7:8]) * 8) + (int(new_cns[8:9]) * 7) + (int(new_cns[9:10]) * 6) + (int(new_cns[10:11]) * 5)
        resto = int(soma) % 11
        dv = 11 - resto

        if dv == 11:
            dv = 0

        if dv == 10:
            soma = 0
            soma = (int(new_cns[0:1]) * 15) + (int(new_cns[1:2]) * 14) + (int(new_cns[2:3]) * 13) + (int(new_cns[3:4]) * 12) + (int(new_cns[4:5]) * 11) + (int(new_cns[5:6]) * 10) + (int(new_cns[6:7]) * 9) + (int(new_cns[7:8]) * 8) + (int(new_cns[8:9]) * 7) + (int(new_cns[9:10]) * 6) + (int(new_cns[10:11]) * 5) + 2
            resto = int(soma) % 11
            dv = 11 - resto
            new_cns = new_cns + "001" + str(dv)
        else:
            dv = str(dv)
            new_cns = new_cns + "000" + str(dv)
        cns_valido = valida_cns(new_cns)
    return new_cns