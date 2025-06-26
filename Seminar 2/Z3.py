# ZADATAK 3
def pronadi_najkraci_put(G, izvor, cilj, tezina='udaljenost'):
    put = nx.shortest_path(G, source=izvor, target=cilj, weight='weight')
    duljina = nx.shortest_path_length(G, source=izvor, target=cilj, weight='weight')
    return put, duljina


primjeri = [
    ('ZAGREB', 'POŽEGA'),
    ('ZAGREB', 'IVANIĆ GRAD'),
    ('IVANIĆ GRAD', 'KUTINA'),
    ('KUTINA', 'POŽEGA')
]

for izvor, cilj in primjeri:
    put_udaljenost, duljina_udaljenost = pronadi_najkraci_put(G_udaljenost, izvor, cilj, tezina='udaljenost')
    put_trajanje, duljina_trajanje = pronadi_najkraci_put(G_trajanje, izvor, cilj, tezina='trajanje')

    print(f"Najkraći put od {izvor} do {cilj} prema udaljenosti:")
    print(f"Put: {' -> '.join(put_udaljenost)}, Udaljenost: {round(duljina_udaljenost, 2)} km")

    print(f"Najkraći put od {izvor} do {cilj} prema trajanju:")
    print(f"Put: {' -> '.join(put_trajanje)}, Trajanje: {round(duljina_trajanje, 2)} min")
    print("-" * 50)
