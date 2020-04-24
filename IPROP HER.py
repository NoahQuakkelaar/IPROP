import time
import random
import sys

randomint1 = random.randint(1000,3000)
randomint2 = random.randint(1000,3000)
randomint3 = random.randint(1000,3000)
    


global leverancier_lst
leveranciers_lst = []
leveranciers_lst.append({"leverancier": 1, "naam": "Shenzhen Electronics Co.", "levertijd": "1 werkdag", "voorraad": 17, "prijs": randomint1})
leveranciers_lst.append({"leverancier": 2, "naam": "Harwood BV.", "levertijd": "3 werkdagen", "voorraad": 38, "prijs": randomint2})
leveranciers_lst.append({"leverancier": 3, "naam": "Gansu Bixi International Trade Co.", "levertijd": "5 werkdagen", "voorraad": 3, "prijs": randomint3})



def artikel_kopen():
    global artikel
    artikel = int(input())
    if artikel > 5 or artikel < 1:
        print("Voer alstublieft een geldig artikelnummer in.")
        time.sleep(2)
        artikel_kopen() 
    

    else:
        print("Hoeveel artikelen van dit product wilt u kopen? (Graag een getal ingeven)")
        aantal_kopen()



def aantal_kopen():
        global aantal
        aantal = int(input())
        if aantal > 10 or aantal < 1:
            print("Ongeldig aantal. Vul alstublieft een geldig aantal in.")
            aantal_kopen()
        else:
            print("Kies alstublieft uit de volgende leveranciers: ")
            time.sleep(1)
    
            for leverancier in leveranciers_lst:
                global productprijs
                productprijs = random.randint(1000,3000)
                
                
                print('\nNummer Leverancier:', leverancier["leverancier"], "\n", 'Naam Leverancier:', leverancier["naam"], '\n', 'Product prijs:', leverancier["prijs"], "\n", 'Levertijd:', leverancier["levertijd"], '\n', 'Voorraad product:', leverancier["voorraad"])

            leverancierkiezen()

def prnt_naam_leverancier():
    if leverancier == 1:
        return leveranciers_lst[0]["naam"]
    elif leverancier == 2:
        return leveranciers_lst[1]["naam"]
    else:
        return leveranciers_lst[2]["naam"]

def prnt_levertijd_leverancier():
    if leverancier == 1:
        return leveranciers_lst[0]["levertijd"]
    elif leverancier == 2:
        return leveranciers_lst[1]["levertijd"]
    else:
        return leveranciers_lst[2]["levertijd"]

def leverancierkiezen():
    global leverancier
    leverancier = int(input())
    if leverancier > 3 or leverancier < 1:
        print("Ongeldige leverancier. Vul alstublieft een geldige leverancier in.")
        leverancierkiezen()
    else:
        print("Wilt u uw bestelling bekijken? (Voer in 'Ja' of 'Nee' in.)")
        janee()

def janee():
    janee_input = input()
    if janee_input == "Ja":
        show_bestelling()
    elif janee_input == "Nee":
        eind_bestelling()
    else:
        print("Ongeldige waarde. Vul alstublieft een geldige waarde in.")
        janee()
        


def eind_bestelling():
    print("\nHartelijk bedankt voor uw bestelling bij:", prnt_naam_leverancier(), "\n", "Het totaal bedrag is:", bereken_totaalbedrag(), "\n", "De levertijd is:", prnt_levertijd_leverancier(), "\n", "Uw bestelling wordt vandaag nog naar u verzonden!")


def show_bestelling():
    if artikel == 1:
        print(producten_lst_ab[0]["artikelnaam"])
    elif artikel == 2:
        print(producten_lst_ab[1]["artikelnaam"])
    elif artikel == 3:
        print(producten_lst_ab[2]["artikelnaam"])
    elif artikel == 4:
        print(producten_lst_ab[3]["artikelnaam"])
    else:
        print(producten_lst_ab[4]["artikelnaam"])

    print("Wilt u de bestelling bevestigen? Zo ja, voer 'Ja' in. Zo niet, voer 'Nee' in.")
    bevestig_factuur()

def bevestig_factuur():
    janee_input = input()
    if janee_input == "Ja":
        eind_bestelling()
    elif janee_input == "Nee":
        print("Bestelling geannuleerd.")
        sys.exit()
    else:
        print("Ongeldige waarde. Voer alstublieft een geldige waarde in.")
        bevestig_factuur()


def totaalbedrag_f():
    global totaalbedrag
    if leverancier == 1:
        totaalbedrag = aantal * leveranciers_lst[0]["prijs"]
    elif leverancier == 2:
        totaalbedrag =  aantal * leveranciers_lst[1]["prijs"]
    else:
        totaalbedrag = aantal * leveranciers_lst[2]["prijs"]

def bereken_totaalbedrag():
    if artikel == 1:
        totaalbedrag_f()
    elif artikel == 2:
        totaalbedrag_f()
    elif artikel == 3:
        totaalbedrag_f()
    elif artikel == 4:
        totaalbedrag_f()
    else:
        totaalbedrag_f()

    return str(totaalbedrag)


def bestellen():
    
    global producten_lst_ab

    producten_lst_ab = []
    producten_lst_ab.append({"artikelnr": 1, "artikelnaam": "Asus PC", "specs": "Core i5, 16GB RAM, 256GB Storage", "prijs": 1100, "voorraad": 10, "levertijd": "1 dag"})
    producten_lst_ab.append({"artikelnr": 2, "artikelnaam": "Acer PC", "specs": "Core i5, 32GB RAM, 512GB Storage", "prijs": 1500, "voorraad": 10, "levertijd": "1 dag"})
    producten_lst_ab.append({"artikelnr": 3, "artikelnaam": "Razer PC", "specs": "Core i7, 32GB RAM, 512GB Storage", "prijs": 2000, "voorraad": 10, "levertijd": "1 dag"}) 
    producten_lst_ab.append({"artikelnr": 4, "artikelnaam": "Alienware PC", "specs": "Core i7, 64GB RAM, 512GB Storage", "prijs": 2300, "voorraad": 10, "levertijd": "1 dag"})
    producten_lst_ab.append({"artikelnr": 5, "artikelnaam": "Apple PC", "specs": "Core i7, 64GB RAM, 1TB Storage", "prijs": 2800, "voorraad": 10, "levertijd": "1 dag"})

    for product in producten_lst_ab:
        print('Artikelnr:', product["artikelnr"], '\n', 'Artikelnaam:',product["artikelnaam"], '\n','Specificaties:', product["specs"], '\n', 'Voorraad:' , product["voorraad"], '\n')


    print('Welk product wenst u te kopen? (Voer artikelnummer in a.u.b)')
    artikel_kopen()



def main():

    print("Welkom bij Alibaba!\n \nBedankt dat u van plan bent bij ons te shoppen, wij verkopen producten door van andere bedrijven naar u,\ndaarom kunnen de prijzen, levertijden en de voorraden verschillen. Wij zullen nu de producten laten zien die wij verkopen op dit moment.")
    time.sleep(6)
    print("\nWij wensen u heel veel shop plezier!\n")
    time.sleep(5)

    bestellen()

main()