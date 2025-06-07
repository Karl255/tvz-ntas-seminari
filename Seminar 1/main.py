from binaryTree import *
from loadingMovies import *
from OperacijeNaStablu import *



# Load movies from file (with pickle caching)
movies = load_movies_from_file("movie.txt", "movies.pickle")

# Display loaded movies
'''
print("Loaded Movies (every 11th row starting from row 10):")
for idx, movie in enumerate(movies):
    actual_row = 10 + idx * 11
    print(f"Row: {actual_row}, ID: {movie['id']}, Short: '{movie['short_name']}', Long: '{movie['long_name']}'")
'''
print(f"\nTotal movies loaded: {len(movies)}")

try:
    myTree = loadTreeAsPickle("tree.pickle")
except:
    myTree = BinaryTree()

    '''a) Na temelju sadržaja tekstualne datoteke treba izgraditi AVL stablo uporabom razreda BinaryTree temeljem 
    kraćeg naziva filma kao indeksnog ključa. 
    Ispisati visinu dobivenog AVL stabla.'''
    vals = []
    for i in movies:
        vals.append(i)
        if not i in myTree:
            myTree.add(i)
    saveTreeAsPickle(myTree, "tree.pickle")

print ("Visina: ", myTree.root.height)

'''b) Implementirati pretraživanje podataka o filmu uporabom implementiranog indeksa i to tako da se za 
traženje može zadati kraći naziv filma cjelovito ili djelomično u obliku prefiksa korištenjem znaka '*'. 
Primjerice, može se unijeti cjeloviti naziv 'Bugsy' ili samo dio odnosno prefiks naziva 'Bug*'. 
Nakon što je podatak pronađen treba ispisati cijeli zapis: ID, kraći naziv, duži naziv.'''
#print(searchInTree(myTree.root, "A*"))
'''
c) Implementirati funkciju za traženje u rangu npr. sve filmove od 'Pick' do 'Ten', ili od 'F' do 'M'. 
Rangove treba moći zadati proizvoljno.'''
l = searchRankInTree(myTree.root, "A", "G")
print ("Broj rezultata: ", len(l))
for i in range(100):
    print(l[i])



'''
d) Ispisati minimalnu i maksimalnu vrijednost indeksa i pripadnih podataka za te indekse.

print("Mini: ", getMinInTree(myTree.root))
print("Maxi: ", getMaxInTree(myTree.root))
'''

'''
e) Napraviti metode za ispis broja lijevih rotacija i broja desnih rotacija kod umetanja čvora u stablo.
item = {'id': 69420, 'short_name': 'Start Wars: Rogue One', 'long_name': 'Start Wars: Rogue One (2016)'}
ispisRotacijaKodDodavanja(myTree, item)
'''

'''
f) Ispisati stablo po razinama počevši od korijena prema dolje u cik-cak redoslijedu. 
To znači da se čvorovi na prvoj razini ispisuju s lijeva na desno, 
na drugoj razini s desna na lijevo, pa na trećoj razini s lijeva na desno itd. 
Ispis raditi po razinama, odnosno svaku razinu ispisati u posebnom retku.
ispisStabla(myTree)
'''



'''
g) Nasumično birati zapise iz skupa podataka i graditi obično nebalansirano binarno stablo pretraživanja sve dok je to moguće. 
Zabilježiti visinu takvog nebalansiranog stabla te ponoviti postupak za isti niz zapisa u izgradnji AVL stabla za koji 
također treba zabilježiti visinu dobivenog stabla.

for i in range (10):
    usporediStabla(vals)
'''