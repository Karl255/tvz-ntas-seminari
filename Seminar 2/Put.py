class Put:
    def __init__(self, odrediste, udaljenost, pb, oznaka=None, trajanje=None):
        self.odrediste = odrediste
        self.udaljenost = udaljenost
        self.pb = pb
        self.oznaka = oznaka
        self.trajanje = trajanje
        self.short = self.odrediste[0] + self.odrediste[1]
    def __str__(self):
        return f"{self.odrediste} ({self.udaljenost} km, {self.trajanje:.1f} min)"

    def __repr__(self):
        return self.odrediste

def netezinskaInacica(ceste):
    d=dict()
    for i in ceste:
        d[i] = []
        for j in ceste[i]:
            d[i].append(j.odrediste)
    return d