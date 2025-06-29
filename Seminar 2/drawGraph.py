import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(g, otezanost='udaljenost'):
    G = nx.DiGraph()  # Koristimo DiGraph jer su putevi usmjereni (možete koristiti nx.Graph() za neusmjereni graf)

    # Dodavanje čvorova i bridova
    for grad, putevi in g.items():
        for put in putevi:
            # Dodajemo brid od 'grad' do 'put.odrediste' s atributima
            G.add_edge(grad, put.odrediste,
                       udaljenost=put.udaljenost,
                       oznaka=put.oznaka,
                       trajanje=put.trajanje)

    # Crtanje grafa
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)  # Postavljanje pozicija čvorova

    # Crtanje čvorova i bridova
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=2, arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Dodavanje oznaka na bridove (možete koristiti bilo koji atribut)
    #edge_labels = nx.get_edge_attributes(G, 'oznaka')
    if otezanost == 'udaljenost':
        edge_labels = {(u, v): f"{d['udaljenost']} km" for u, v, d in G.edges(data=True)}
    if otezanost == 'trajanje':
        edge_labels = {(u, v): f"{d['trajanje']} min" for u, v, d in G.edges(data=True)}
    #edge_labels = {(u, v): f"{d['oznaka']}\n{d['udaljenost']} km" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Gradovi i putevi u Hrvatskoj")
    plt.axis('off')  # Isključujemo osi
    plt.tight_layout()
    plt.show()