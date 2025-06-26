# ZADATAK 2

from Z1 import *
import networkx as nx
import matplotlib.pyplot as plt


def generiraj_graf(segmenti, tip_grafa='udaljenost'):
    G = nx.Graph()
    for segment in segmenti:
        if tip_grafa == 'udaljenost':
            tezina = segment.udaljenost
        elif tip_grafa == 'trajanje':
            tezina = segment.trajanje
        else:
            print("\nGreska:")
        G.add_edge(segment.polaziste, segment.odrediste, weight=tezina, label=f"{tezina}")
    return G


def prikazi_mrezu_cesta(G, naslov):
    pos = nx.spring_layout(G, seed=42, k=10)

    plt.figure(figsize=(10, 8))

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos, node_size=400, node_color='skyblue')
    nx.draw_networkx_labels(G, pos, font_color='black', font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(naslov)

    ax = plt.gca()
    ax.set_axis_off()
    plt.show()


G_udaljenost = generiraj_graf(cestovni_segmenti, tip_grafa='udaljenost')
prikazi_mrezu_cesta(G_udaljenost, "Mreža cesta prema udaljenosti")

G_trajanje = generiraj_graf(cestovni_segmenti, tip_grafa='trajanje')
prikazi_mrezu_cesta(G_trajanje, "Mreža cesta prema trajanju")
