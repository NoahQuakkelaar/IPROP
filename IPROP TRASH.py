def bestellen():







    # hier maak ik een lijst van dictionaries met alle producten die we gaan verkopen, vgm 5, en dat per bedrijf dat ali baba gebruikt om door te verkopen
    

    producten_lst_ab = []
    producten_lst_ab.append({"artikelnr": 1, "artikelnaam": "asus pc", "specs": "core i5, 16gb ram, 256 gb storage", "prijs": 1100, "voorraad": 10, "levertijd": "1 dag"})
    producten_lst_ab.append({"artikelnr": 2, "artikelnaam": "acer pc", "specs": "core i5, 32 gb ram, 512 gb storage", "prijs": 1500, "voorraad": 10, "levertijd": "1 dag"})
    producten_lst_ab.append({"artikelnr": 3, "artikelnaam": "razer pc", "specs": "core i7, 32 gb ram, 512 gb storage", "prijs": 2000, "voorraad": 10, "levertijd": "1 dag"}) 
    producten_lst_ab.append({"artikelnr": 4, "artikelnaam": "alienware pc", "specs": "core i7, 64gb ram, 512 gb storage", "prijs": 2300, "voorraad": 10, "levertijd": "1 dag"})
    producten_lst_ab.append({"artikelnr": 5, "artikelnaam": "apple pc", "specs": "core i7, 64gb ram, 1 terrabyte storage", "prijs": 2800, "voorraad": 10, "levertijd": "1 dag"})

    

    producten_lst = []
    producten_lst.append({"artikelnr": 1, "artikelnaam": "asus pc", "specs": "core i5, 16 gb ram, 256 gb storage", "prijs": 1000, "voorraad": 10, "levertijd": "2 dagen"})
    producten_lst.append({"artikelnr": 2, "artikelnaam": "acer pc", "specs": "core i5, 32 gb ram, 512 gb storage", "prijs": 1400, "voorraad": 10, "levertijd": "2 dagen"})
    producten_lst.append({"artikelnr": 3, "artikelnaam": "razer pc", "specs": "core i7, 32 gb ram, 512 gb storage", "prijs": 1800, "voorraad": 10, "levertijd": "2 dagen"})
    producten_lst.append({"artikelnr": 4, "artikelnaam": "alienware pc", "specs": "core i7, 64 gb ram, 512 gb storage", "prijs": 2400, "voorraad": 10, "levertijd": "2 dagen"})
    producten_lst.append({"artikelnr": 5, "artikelnaam": "apple pc", "specs": "core i7, 64gb ram, 1 terrabyte storage", "prijs": 3000, "voorraad": 10, "levertijd": "2 dagen"})

    

    producten_lst_3 = []
    producten_lst_3.append({"artikelnr": 1, "artikelnaam": "asus pc", "specs": "core i5, 16 gb ram, 256 gb storage", "prijs": 1200, "voorraad": 10, "levertijd": "3 dagen"})
    producten_lst_3.append({"artikelnr": 2, "artikelnaam": "acer pc", "specs": "core i5, 32 gb ram, 512 gb storage", "prijs": 1300, "voorraad": 10, "levertijd": "3 dagen"})
    producten_lst_3.append({"artikelnr": 3, "artikelnaam": "razer pc", "specs": "core i7, 32 gb ram, 512 gb storage", "prijs": 1900, "voorraad": 10, "levertijd": "3 dagen"})
    producten_lst_3.append({"artikelnr": 4, "artikelnaam": "alienware pc", "specs": "core i7, 64 gb ram, 512 gb storage", "prijs": 2100, "voorraad": 10, "levertijd": "3 dagen"})
    producten_lst_3.append({"artikelnr": 5, "artikelnaam": "apple pc", "specs": "core i7, 64gb ram, 1 terrabyte storage", "prijs": 2900, "voorraad": 10, "levertijd": "3 dagen"})






    

    # hier zet ik alle producten met alle eigenschappen van het product op het scherm
    
    for product in producten_lst_ab:
        print('artikelnr:', product["artikelnr"], '\n', 'artikelnaam:',product["artikelnaam"], '\n','specificaties:', product["specs"], '\n')
    print()

    






    

    # hier vraag ik om welke product ze willen en aantal, daarna per bedrijf laten zien de voorraad, verzendtijd en prijs en uiteindelijk totaalbedrag van de producten
    
    print('welk product wil je(typ artikelnummer in)')
    artikel = int(input())
    print("hoeveel wil je ervan")
    aantal = int(input())
    print("Dit zijn de prijzen, bezorgtijden en voorraad van elke leverancier, welke wil je, typ 1, 2 of 3", '\n')
    print('1:', '\n')
    print('prijs:', producten_lst_ab[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_ab[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_ab[artikel-1]["levertijd"], '\n')
    print('2:', '\n')
    print('prijs:', producten_lst[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst[artikel-1]["levertijd"], '\n')
    print('3:', '\n')
    print('prijs:', producten_lst_3[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_3[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_3[artikel-1]["levertijd"], '\n')
    print("welke leverancier wilt u(typ 1, 2 of 3)")
    leverancier = int(input())
    if leverancier == 1:
        print ('totale prijs producten:',producten_lst_ab[artikel-1]['prijs']*aantal)
        producten_lst_ab[artikel-1]['voorraad']=producten_lst_ab[artikel-1]['voorraad'] - aantal
    elif leverancier == 2:
        print ('totale prijs producten:',producten_lst[artikel-1]['prijs']*aantal)
        producten_lst[artikel-1]['voorraad']=producten_lst[artikel-1]['voorraad'] - aantal
    elif leverancier == 3:
        print ('totale prijs producten:',producten_lst_3[artikel-1]['prijs']*aantal)
        producten_lst_3[artikel-1]['voorraad']=producten_lst_3[artikel-1]['voorraad'] - aantal
            






    

    # hieronder vraag ik of ze nog wat willen, zoja dan herhaalt het zih weer, zonee dan door naar betalen/kassa/verzending

    # ik heb het bewust 5 keer gedaan , omdat er 5 producten zijn, dus dat is dan ook de max

    
    
    print('wil je nog iets(ja/nee)')
    antwoord = input()
    if antwoord == 'ja':
        
        for product in producten_lst_ab:
            print('artikelnr:', product["artikelnr"], '\n', 'artikelnaam:',product["artikelnaam"], '\n','specificaties:', product["specs"], '\n')
            print()

        print('welk product wil je(typ artikelnummer in)')
        artikel = int(input())
        print("hoeveel wil je ervan")
        aantal = int(input())
        print("Dit zijn de prijzen, bezorgtijden en voorraad van elke leverancier, welke wil je, typ 1, 2 of 3", '\n')
        print('1:', '\n')
        print('prijs:', producten_lst_ab[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_ab[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_ab[artikel-1]["levertijd"], '\n')
        print('2:', '\n')
        print('prijs:', producten_lst[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst[artikel-1]["levertijd"], '\n')
        print('3:', '\n')
        print('prijs:', producten_lst_3[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_3[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_3[artikel-1]["levertijd"], '\n')
        print("welke leverancier wilt u(typ 1, 2 of 3)")
        leverancier = int(input())
        if leverancier == 1:
            print ('totale prijs producten:',producten_lst_ab[artikel-1]['prijs']*aantal)
            producten_lst_ab[artikel-1]['voorraad']=producten_lst_ab[artikel-1]['voorraad'] - aantal
        elif leverancier == 2:
            print ('totale prijs producten:',producten_lst[artikel-1]['prijs']*aantal)
            producten_lst[artikel-1]['voorraad']=producten_lst[artikel-1]['voorraad'] - aantal
        elif leverancier == 3:
            print ('totale prijs producten:',producten_lst_3[artikel-1]['prijs']*aantal)
            producten_lst_3[artikel-1]['voorraad']=producten_lst_3[artikel-1]['voorraad'] - aantal

        
            

    
    
        print('wil je nog iets(ja/nee)')
        antwoord = input()
        
        if antwoord == 'ja':
            
            for product in producten_lst_ab:
                print('artikelnr:', product["artikelnr"], '\n', 'artikelnaam:',product["artikelnaam"], '\n','specificaties:', product["specs"], '\n')
                print()

            print('welk product wil je(typ artikelnummer in)')
            artikel = int(input())
            print("hoeveel wil je ervan")
            aantal = int(input())
            print("Dit zijn de prijzen, bezorgtijden en voorraad van elke leverancier, welke wil je, typ 1, 2 of 3", '\n')
            print('1:', '\n')
            print('prijs:', producten_lst_ab[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_ab[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_ab[artikel-1]["levertijd"], '\n')
            print('2:', '\n')
            print('prijs:', producten_lst[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst[artikel-1]["levertijd"], '\n')
            print('3:', '\n')
            print('prijs:', producten_lst_3[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_3[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_3[artikel-1]["levertijd"], '\n')
            print("welke leverancier wilt u(typ 1, 2 of 3)")
            leverancier = int(input())
            if leverancier == 1:
                print ('totale prijs producten:',producten_lst_ab[artikel-1]['prijs']*aantal)
                producten_lst_ab[artikel-1]['voorraad']=producten_lst_ab[artikel-1]['voorraad'] - aantal
            elif leverancier == 2:
                print ('totale prijs producten:',producten_lst[artikel-1]['prijs']*aantal)
                producten_lst[artikel-1]['voorraad']=producten_lst[artikel-1]['voorraad'] - aantal
            elif leverancier == 3:
                print ('totale prijs producten:',producten_lst_3[artikel-1]['prijs']*aantal)
                producten_lst_3[artikel-1]['voorraad']=producten_lst_3[artikel-1]['voorraad'] - aantal

         
            print('wil je nog iets(ja/nee)')
            antwoord = input()
            
            if antwoord == 'ja':
                
                for product in producten_lst_ab:
                    print('artikelnr:', product["artikelnr"], '\n', 'artikelnaam:',product["artikelnaam"], '\n','specificaties:', product["specs"], '\n')
                    print()

                print('welk product wil je(typ artikelnummer in)')
                artikel = int(input())
                print("hoeveel wil je ervan")
                aantal = int(input())
                print("Dit zijn de prijzen, bezorgtijden en voorraad van elke leverancier, welke wil je, typ 1, 2 of 3", '\n')
                print('1:', '\n')
                print('prijs:', producten_lst_ab[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_ab[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_ab[artikel-1]["levertijd"], '\n')
                print('2:', '\n')
                print('prijs:', producten_lst[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst[artikel-1]["levertijd"], '\n')
                print('3:', '\n')
                print('prijs:', producten_lst_3[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_3[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_3[artikel-1]["levertijd"], '\n')
                print("welke leverancier wilt u(typ 1, 2 of 3)")
                leverancier = int(input())
                if leverancier == 1:
                    print ('totale prijs producten:',producten_lst_ab[artikel-1]['prijs']*aantal)
                    producten_lst_ab[artikel-1]['voorraad']=producten_lst_ab[artikel-1]['voorraad'] - aantal
                elif leverancier == 2:
                    print ('totale prijs producten:',producten_lst[artikel-1]['prijs']*aantal)
                    producten_lst[artikel-1]['voorraad']=producten_lst[artikel-1]['voorraad'] - aantal
                elif leverancier == 3:
                    print ('totale prijs producten:',producten_lst_3[artikel-1]['prijs']*aantal)
                    producten_lst_3[artikel-1]['voorraad']=producten_lst_3[artikel-1]['voorraad'] - aantal

                
                print('wil je nog iets(ja/nee)')
                antwoord = input()
                
                if antwoord == 'ja':
                    
                    for product in producten_lst_ab:
                        print('artikelnr:', product["artikelnr"], '\n', 'artikelnaam:',product["artikelnaam"], '\n','specificaties:', product["specs"], '\n')
                        print()

                    print('welk product wil je(typ artikelnummer in)')
                    artikel = int(input())
                    print("hoeveel wil je ervan")
                    aantal = int(input())
                    print("Dit zijn de prijzen, bezorgtijden en voorraad van elke leverancier, welke wil je, typ 1, 2 of 3", '\n')
                    print('1:', '\n')
                    print('prijs:', producten_lst_ab[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_ab[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_ab[artikel-1]["levertijd"], '\n')
                    print('2:', '\n')
                    print('prijs:', producten_lst[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst[artikel-1]["levertijd"], '\n')
                    print('3:', '\n')
                    print('prijs:', producten_lst_3[artikel-1]["prijs"],'\n' 'voorraad:', producten_lst_3[artikel-1]["voorraad"], '\n', 'levertijd:', producten_lst_3[artikel-1]["levertijd"], '\n')
                    print("welke leverancier wilt u(typ 1, 2 of 3)")
                    leverancier = int(input())
                    if leverancier == 1:
                        print ('totale prijs producten:',producten_lst_ab[artikel-1]['prijs']*aantal)
                        producten_lst_ab[artikel-1]['voorraad']=producten_lst_ab[artikel-1]['voorraad'] - aantal
                    elif leverancier == 2:
                        print ('totale prijs producten:',producten_lst[artikel-1]['prijs']*aantal)
                        producten_lst[artikel-1]['voorraad']=producten_lst[artikel-1]['voorraad'] - aantal
                    elif leverancier == 3:
                        print ('totale prijs producten:',producten_lst_3[artikel-1]['prijs']*aantal)
                        producten_lst_3[artikel-1]['voorraad']=producten_lst_3[artikel-1]['voorraad'] - aantal

                    
                    print('Bedankt voor het bestellen bij ali baba! Uw pakketje wordt direct naar u verstuurd.')
                    
                    
                    
                else:
                    print('Bedankt voor het bestellen bij ali baba! Uw pakketje wordt direct naar u verstuurd.') 
                    
                    
            else:
                print('Bedankt voor het bestellen bij ali baba! Uw pakketje wordt direct naar u verstuurd.') 
        
        else:
            print('Bedankt voor het bestellen bij ali baba! Uw pakketje wordt direct naar u verstuurd.') 
        
    else:
        print('Bedankt voor het bestellen bij ali baba! Uw pakketje wordt direct naar u verstuurd.') 
            










# dit is een functie voor het printen van de lijst met alle producten en eigenschappen ervan

def print_producten(producten_lst_ab):
    for product in producten_lst_ab:
        print('artikelnr:', product["artikelnr"], '\n', 'artikelnaam:',product["artikelnaam"],'\n','prijs', product["prijs"], '\n','specificaties:', product["specs"], '\n', 'voorraad:', product['voorraad'], '\n')
    print()






# MAIN
# =====
def main():
    print("Welkom bij ali baba,")
    print()
    print("bedankt dat u van plan bent bij ons te shoppen, wij verkopen producten door van andere bedrijven naar u,daarom kunnen de prijzen, levertijden en de voorraden verschillen,")
    print()
    print("zorg er wel voor dat uw binnen de aangegeven voorraad zit en veel shopplezier")
    print("")
    bestellen()

    
        


main()
