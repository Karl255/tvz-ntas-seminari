from Put import *
import pandas as pd
from drawGraph import *
from najkraciPut import *
from graf import *
from Centralnosti import *
from Matrica import *


def ucitaj_excel_u_segmente(file):
    df = pd.read_excel(file)
    ceste = dict()
    for _, red in df.iterrows():

        if red['POLAZIŠTE'] not in ceste:
            ceste[red['POLAZIŠTE']] = []
        if red['ODREDIŠTE'] not in ceste:
            ceste[red['ODREDIŠTE']] = []


        segment1 = Put(
            odrediste=red['ODREDIŠTE'],
            oznaka=red['OZNAKA CESTE'],
            udaljenost=red['UDALJENOST km'],
            pb=red['PROSJEČNA BRZ km/h'],
            trajanje=red['TRAJANJE [min]']
        )
        segment2 = Put(
            odrediste=red['POLAZIŠTE'],
            oznaka=red['OZNAKA CESTE'],
            udaljenost=red['UDALJENOST km'],
            pb=red['PROSJEČNA BRZ km/h'],
            trajanje=red['TRAJANJE [min]']
        )
        ceste[red['POLAZIŠTE']].append(segment1)
        ceste[red['ODREDIŠTE']].append(segment2)
    return ceste


file = 'MREZA_CESTOVNIH_PRAVACA_CUSTOM.xlsx'
ceste = ucitaj_excel_u_segmente(file)
ispisMatrice(ceste)

'''
for i in ceste:
    print(i, end=": [ ")
    l=ceste[i]
    for j in l:
        print((j.short, j.udaljenost), end=" ")
    print("]")
'''


#draw_graph(ceste)

#ispisNajkracegPuta(ceste, 'Zagreb', 'Split')

graph = Graph(netezinskaInacica(ceste))

#print("Dijametar:" ,graph.diameter())
#print("Gustoća: ", graph.density())
#for ver in graph:
#    print(ver, ": ", graph.vertex_degree(ver))

#centralnosti(netezinskaInacica(ceste))