from openpyxl import load_workbook

RDECA = "FF0000"
ORANZNA = "FFA500"
MODRA = "99FFFF"


def preveri_meje_omare(seznam):
    # funkcija prejme seznam s 25 elementi, ter binarno vrendost trafo

    slovar_problematicnih_meritev = dict()

    if seznam[3] == "X":
        slovar_problematicnih_meritev[3] = MODRA
    else:
        if float(seznam[3].replace(">", "").replace(",", ".")) > 1 and 10 > float(
            seznam[3].replace(">", "").replace(",", ".")
        ):
            slovar_problematicnih_meritev[3] = ORANZNA
        elif float(seznam[3].replace(">", "").replace(",", ".")) >= 10:
            slovar_problematicnih_meritev[3] = RDECA

    return slovar_problematicnih_meritev
