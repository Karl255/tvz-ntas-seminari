# ZADATAK 1

import pandas as pd


class Cesta:
    def __init__(self, polaziste, odrediste, oznaka_ceste, udaljenost, prosjecna_brzina, trajanje):
        self.polaziste = polaziste
        self.odrediste = odrediste
        self.oznaka_ceste = oznaka_ceste
        self.udaljenost = round(udaljenost, 2)
        self.prosjecna_brzina = prosjecna_brzina
        self.trajanje = round(trajanje, 2)


def ucitaj_excel_u_segmente(file):
    df = pd.read_excel(file)
    ceste = []
    for _, red in df.iterrows():
        segment = Cesta(
            polaziste=red['POLAZIŠTE'],
            odrediste=red['ODREDIŠTE'],
            oznaka_ceste=red['OZNAKA CESTE'],
            udaljenost=red['UDALJENOST km'],
            prosjecna_brzina=red['PROSJEČNA BRZ km/h'],
            trajanje=red['TRAJANJE [min]']
        )
        ceste.append(segment)
    return ceste


def generiraj_listu_susjedstva(segmenti):
    lista_susjedstva = {}
    for segment in segmenti:
        if segment.polaziste not in lista_susjedstva:
            lista_susjedstva[segment.polaziste] = []
        if segment.odrediste not in lista_susjedstva:
            lista_susjedstva[segment.odrediste] = []
        lista_susjedstva[segment.polaziste].append((segment.odrediste, segment.udaljenost))
        lista_susjedstva[segment.odrediste].append((segment.polaziste, segment.udaljenost))
    return lista_susjedstva


def generiraj_matricu_susjedstva(segmenti):
    gradovi = list(set([segment.polaziste for segment in segmenti] + [segment.odrediste for segment in segmenti]))
    indeksi_gradova = {grad: index for index, grad in enumerate(gradovi)}
    velicina_matrice = len(gradovi)
    matrica_susjedstva = [[0] * velicina_matrice for _ in range(velicina_matrice)]

    for segment in segmenti:
        i = indeksi_gradova[segment.polaziste]
        j = indeksi_gradova[segment.odrediste]
        matrica_susjedstva[i][j] = segment.udaljenost
        matrica_susjedstva[j][i] = segment.udaljenost

    return matrica_susjedstva, gradovi


file = 'MREZA_CESTOVNIH_PRAVACA.xlsx'
ceste = ucitaj_excel_u_segmente(file)

lista_susjedstva = generiraj_listu_susjedstva(ceste)
print("Lista susjedstva:")
for grad, susjedi in lista_susjedstva.items():
    print(f"{grad}: {susjedi}")

matrica_susjedstva, gradovi = generiraj_matricu_susjedstva(ceste)
print("\nMatrica susjedstva:")
print(f"Gradovi: {gradovi}")
for red in matrica_susjedstva:
    print(red)
