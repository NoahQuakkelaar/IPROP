import time
import random
import sys
import Leverancier_LST

def artikel_kopen():
    global artikel
    try:
        artikel = int(input())
        if artikel > 5 or artikel < 1:
            print("Voer alstublieft een geldig artikelnummer in.")
            time.sleep(2)
            artikel_kopen() 
        

        else:
            print("Hoeveel artikelen van dit product wilt u kopen? (Graag een getal ingeven)")
            aantal_kopen()
    except ValueError:
       print("Voer alstublieft een getal in.")
       artikel_kopen()



def aantal_kopen():
        global aantal
        try:
            aantal = int(input())
            if aantal > 10 or aantal < 1:
                print("Ongeldig aantal. Vul alstublieft een geldig aantal in. (Let hierbij op de voorraad)")
                aantal_kopen()
            else:
                print("Kies alstublieft uit de volgende leveranciers: ")
                time.sleep(1)
        
                for leverancier in Leverancier_LST.leveranciers_lst:
                    global productprijs
                    productprijs = random.randint(1000,3000)
                    
                    
                    print('\nNummer Leverancier:', leverancier["leverancier"], "\n", 'Naam Leverancier:', leverancier["naam"], '\n', 'Product prijs:', leverancier["prijs"], "\n", 'Levertijd:', leverancier["levertijd"], '\n', 'Voorraad product:', leverancier["voorraad"])

                leverancierkiezen()
        except ValueError:
            print("Voer alstublieft een getal in.")
            aantal_kopen()

def prnt_naam_leverancier():
    return Leverancier_LST.leveranciers_lst[leverancier - 1]["naam"]

def prnt_levertijd_leverancier():
    return Leverancier_LST.leveranciers_lst[leverancier -1]["levertijd"]
    

def leverancierkiezen():
    global leverancier
    leverancier = int(input())
    if leverancier > 3 or leverancier < 1:
        print("Ongeldige leverancier. Vul alstublieft een geldige leverancier in.")
        leverancierkiezen()
    else:
        print("Wilt u uw bestelling bekijken? (Voer in 'Ja' of 'Nee' in.)")
        leverancier_input()

def leverancier_input():
    lvrc_input = input()
    if lvrc_input == "Ja" or lvrc_input == "ja" or lvrc_input == "JA":
        show_bestelling()
    elif lvrc_input == "Nee" or lvrc_input == "nee" or lvrc_input == "NEE":
        eind_bestelling()
    else:
        print("Ongeldige waarde. Vul alstublieft een geldige waarde in.")
        leverancier_input()
        


def eind_bestelling():
    print("\nHartelijk bedankt voor uw bestelling bij:", prnt_naam_leverancier(), "\n", "Het totaal bedrag is:", totaalbedrag_check(), "\n", "De levertijd is:", prnt_levertijd_leverancier(), "\n", "Uw bestelling wordt vandaag nog naar u verzonden!")


def show_bestelling():
    print(Leverancier_LST.producten_lst_ab[artikel - 1]["artikelnaam"])
    print("Wilt u de bestelling bevestigen? Zo ja, voer 'Ja' in. Als u de bestelling wilt annuleren, voer 'Nee' in.")
    bevestig_factuur()

def bevestig_factuur():
    bevestig_input = input()
    if bevestig_input == "Ja" or bevestig_input == "ja" or bevestig_input == "JA":
        eind_bestelling()
    elif bevestig_input == "Nee" or bevestig_input == "nee" or bevestig_input == "NEE":
        print("Bestelling geannuleerd.")
        sys.exit()
    else:
        print("Ongeldige waarde. Voer alstublieft een geldige waarde in.")
        bevestig_factuur()


def totaalbedrag_check():
    global totaalbedrag
    totaalbedrag = aantal * Leverancier_LST.leveranciers_lst[leverancier - 1]["prijs"]
    return str(totaalbedrag)


def bestellen():
    for product in Leverancier_LST.producten_lst_ab:
        print('Artikelnr:', product["artikelnr"], '\n', 'Artikelnaam:',product["artikelnaam"], '\n','Specificaties:', product["specs"], '\n', 'Voorraad:' , product["voorraad"], '\n')


    print('Welk product wenst u te kopen? (Voer artikelnummer in a.u.b)')
    artikel_kopen()



def main():
    Leverancier_LST.init_glob_vars()
    Leverancier_LST.init_lists()

    print("Welkom bij Alibaba!\n \nBedankt dat u van plan bent bij ons te shoppen, wij verkopen producten door van andere bedrijven naar u,\ndaarom kunnen de prijzen, levertijden en de voorraden verschillen. Wij zullen nu de producten laten zien die wij verkopen op dit moment.")
    time.sleep(6)
    print("\nWij wensen u heel veel shop plezier!\n")
    time.sleep(5)

    bestellen()

main()