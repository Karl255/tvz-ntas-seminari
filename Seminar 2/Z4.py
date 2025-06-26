# ZADATAK 4

import networkx as nx

def generiraj_nevazani_graf(segments):
    G = nx.Graph()
    for segment in segments:
        G.add_edge(segment.polaziste, segment.odrediste)
    return G

file_path = 'MREZA_CESTOVNIH_PRAVACA.xlsx'
road_segments = ucitaj_excel_u_segmente(file_path)

G_unweighted = generiraj_nevazani_graf(road_segments)

print("Netežinska inačica grafa:")
df = nx.to_pandas_edgelist(G_unweighted)
print(df)


# ZADATAK 4.b

diameter = nx.diameter(G_unweighted)
print(f"\nDijametar grafa: {diameter}")

density = nx.density(G_unweighted)
print(f"\nGustoća grafa: {density}")

degrees = dict(G_unweighted.degree())
print("\nStupnjevi svih čvorova:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")
