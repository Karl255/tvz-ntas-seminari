import networkx as nx
def najkraci_put(ceste, pocetak, kraj, kriterij='udaljenost'):
    # Kreiranje usmjerenog grafa
    G = nx.DiGraph()

    # Dodavanje bridova s atributima
    for grad, putevi in ceste.items():
        for put in putevi:
            G.add_edge(grad, put.odrediste,
                       udaljenost=put.udaljenost,
                       trajanje=put.trajanje,
                       oznaka=put.oznaka)
    """
    Pronalazi najkraći put između dva grada prema odabranom kriteriju.

    Parametri:
        G (nx.Graph): Graf
        pocetak (str): Početni grad
        kraj (str): Odredišni grad
        kriterij (str): 'udaljenost' ili 'trajanje'

    Vraća:
        tuple: (ukupna vrijednost, lista čvorova)
    """
    try:
        if kriterij == 'udaljenost':
            put = nx.shortest_path(G, source=pocetak, target=kraj, weight='udaljenost')
            vrijednost = nx.shortest_path_length(G, source=pocetak, target=kraj, weight='udaljenost')
        elif kriterij == 'trajanje':
            put = nx.shortest_path(G, source=pocetak, target=kraj, weight='trajanje')
            vrijednost = nx.shortest_path_length(G, source=pocetak, target=kraj, weight='trajanje')
        else:
            raise ValueError("Kriterij mora biti 'udaljenost' ili 'trajanje'")

        return (vrijednost, put)
    except nx.NetworkXNoPath:
        return (None, None)

def ispisNajkracegPuta(ceste, pocetak, kraj):
    # Najkraći put prema udaljenosti
    udaljenost, put_udaljenost = najkraci_put(ceste, pocetak, kraj, 'udaljenost')
    if put_udaljenost:
        print(f"Najkraći put po udaljenosti ({udaljenost} km): {' -> '.join(put_udaljenost)}")
    else:
        print("Nema puta po udaljenosti")

    # Najkraći put prema trajanju
    trajanje, put_trajanje = najkraci_put(ceste, pocetak, kraj, 'trajanje')
    if put_trajanje:
        print(f"Najkraći put po trajanju ({trajanje:.1f} min): {' -> '.join(put_trajanje)}")
    else:
        print("Nema puta po trajanju")