import networkx as nx
import pandas as pd

def ispisMatrice(g):
    # Kreiranje grafa
    G = nx.DiGraph()

    # Dodavanje bridova s atributima
    for grad, putevi in g.items():
        for put in putevi:
            G.add_edge(grad, put.odrediste,
                       udaljenost=put.udaljenost,
                       trajanje=put.trajanje,
                       oznaka=put.oznaka)

    # Generiranje matrice susjedstva (udaljenost)
    gradovi = sorted(G.nodes())
    matrica_susjedstva = nx.to_pandas_adjacency(G, weight='udaljenost', dtype=int)

    # Spremanje u CSV
    matrica_susjedstva.to_csv('matrica_susjedstva_udaljenost.csv')
    print("Matrica susjedstva (udaljenost) spremljena u 'matrica_susjedstva_udaljenost.csv'")

    # Opcionalno: Matrica susjedstva za trajanje
    matrica_trajanje = nx.to_pandas_adjacency(G, weight='trajanje', dtype=int)
    matrica_trajanje.to_csv('matrica_susjedstva_trajanje.csv')
    print("Matrica susjedstva (trajanje) spremljena u 'matrica_susjedstva_trajanje.csv'")

    # Prikaz prvih redova matrice
    print("\nPrimjer matrice susjedstva (udaljenost):")
    print(matrica_susjedstva.head())