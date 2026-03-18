lista = [1, 2, 3, 4, 5]
stringa = "Buongiorno prof come sta oggi?"
d = {"uno" : 1, "due" : 2, "tre" : 3}
indice = 2

# 1. Scrivi una funzione "filtra_dispari(lista)" che restituisca una nuova lista contenente solo i numeri dispari.

def filtra_dispari(lista):
    dispari = []
    for num in lista:
        if num %2 != 0:
            dispari.append(num)
    print("I numeri dispari sono:")
    print(dispari)
    print(" ")

filtra_dispari(lista)

# 2. Scrivi una funzione "somma_indici_dispari(lista)" che sommi gli elementi agli indici dispari.

def somma_indici_dispari(lista):
    dispari = []
    somma = 0
    indice = 0
    for indice in lista:
        if indice %2 != 0:
            somma += indice
    print("La somma degli indici dispari è:")
    print(indice)
    print(" ")
        
somma_indici_dispari(lista)

# 3. Scrivi una funziona "spezza_lista(lista, indice)" che spezzi la lista in ingresso nella posizione corrispondente ad indice e ritorni le due liste separate.

def spezza_lista(lista, indice):
    lista2 = lista[indice:max(lista)]
    lista = lista[0:indice]
    print("La prima parte della lista è:")
    print(lista)
    print(" ")

    print("La seconda parte della lista è:")
    print(lista2)
    print(" ")
spezza_lista(lista, indice)

# 4. Scrivi una funzione "conta_spazi(stringa)" che restituisca il numero di spazi nella stringa di ingresso.

def conta_spazi(stringa):
    conta = 0
    for char in stringa:
        if char == " ":
            conta += 1
    print("Gli spazi presenti sono:")
    print(conta)
    print(" ")

conta_spazi(stringa)

# 5. Scrivi una funzione "rimuovi_doppie(stringa) che rimuova le doppie nella stringa di ingresso.

def rimuovi_doppie(stringa):
    senza_doppie = ""
    for char in stringa:
        if char not in senza_doppie:
            senza_doppie += char
    print("La stringa senza doppie è:")
    print(senza_doppie)
    print(" ")

rimuovi_doppie(stringa)

# 6. Scrivi una funzione "parola_piu_lunga(stringa)" che ritorni la parola più lunga nella stringa in ingresso.
def parola_piu_lunga(stringa):
    L = stringa.split(" ")
    pmax = None
    max = 0
    for p in L:
        if len(p) > max:
            pmax = p
            max = len(p)
    print("La parola più lunga è:")
    print(pmax)
    print(" ")

parola_piu_lunga(stringa)

# 7. Scrivi una funzione "prodotto_valori(d)" che restituisca il prodotto dei valori numerici.

def prodotto_valori(d):
    prodotto = 1
    valori = dict.values(d)
    for num in valori:
        prodotto = prodotto * num
    print("Il prodotto dei valori è:")
    print(prodotto)
    print(" ")
prodotto_valori(d)

# 8. Scrivi una funzione "inverti_dizionario(d)" che scambi chiavi e valori.

def inverti_dizionario(d):
    chiavi = dict.keys(d)
    valori = dict.values(d)
    dizionario2 = {}
    # dict.keys(dizionario2) = valori
    # dict.values(dizionario2) = chiavi
    print(dizionario2)

inverti_dizionario(d)

# 9. Scrivi una funzione "conta_lettere(testo)" che restituisce un dizionario con la frequenza delle lettere.

def conta_lettere(testo):
    lettere_frequenza = {} 