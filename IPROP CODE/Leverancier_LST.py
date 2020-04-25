import random

def init_glob_vars():
    global randomint1
    global randomint2
    global randomint3

    randomint1 = random.randint(1000,3000)
    randomint2 = random.randint(1000,3000)
    randomint3 = random.randint(1000,3000)

def init_lists():
    global leveranciers_lst
    leveranciers_lst = []
    leveranciers_lst.append({"leverancier": 1, "naam": "Shenzhen Electronics Co.", "levertijd": "1 werkdag", "voorraad": 17, "prijs": randomint1})
    leveranciers_lst.append({"leverancier": 2, "naam": "Harwood BV.", "levertijd": "3 werkdagen", "voorraad": 38, "prijs": randomint2})
    leveranciers_lst.append({"leverancier": 3, "naam": "Gansu Bixi International Trade Co.", "levertijd": "5 werkdagen", "voorraad": 24, "prijs": randomint3})

    global producten_lst_ab
    producten_lst_ab = []
    producten_lst_ab.append({"artikelnr": 1, "artikelnaam": "Asus PC", "specs": "Core i5, 16GB RAM, 256GB Storage", "prijs": 1100, "voorraad": 10, "levertijd": "1 dag"})
    producten_lst_ab.append({"artikelnr": 2, "artikelnaam": "Acer PC", "specs": "Core i5, 32GB RAM, 512GB Storage", "prijs": 1500, "voorraad": 10, "levertijd": "1 dag"})
    producten_lst_ab.append({"artikelnr": 3, "artikelnaam": "Razer PC", "specs": "Core i7, 32GB RAM, 512GB Storage", "prijs": 2000, "voorraad": 10, "levertijd": "1 dag"}) 
    producten_lst_ab.append({"artikelnr": 4, "artikelnaam": "Alienware PC", "specs": "Core i7, 64GB RAM, 512GB Storage", "prijs": 2300, "voorraad": 10, "levertijd": "1 dag"})
    producten_lst_ab.append({"artikelnr": 5, "artikelnaam": "Apple PC", "specs": "Core i7, 64GB RAM, 1TB Storage", "prijs": 2800, "voorraad": 10, "levertijd": "1 dag"})
