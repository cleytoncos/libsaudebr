import random
from sigtap import sigtap

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
                soma_pis = (int(pis[0:1]) * 15) + (int(pis[1:2]) * 14) + (int(pis[2:3]) * 13) + (int(pis[3:4]) * 12) + (int(pis[4:5]) * 11) + (int(pis[5:6]) * 10) + (int(pis[6:7]) * 9) + (int(pis[7:8]) * 8) + (int(pis[8:9]) * 7) + (int(pis[9:10]) * 6) + (int(pis[10:11]) * 5) + 2
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



sigtap_outros_desc()
