import random
def nombre_mystere():
    difficulte=input("Choisissez une difficulte (facile, moyen, difficile) : ").lower()
    if difficulte =='facile':
        borne_max=10
    elif difficulte =='moyen':
        borne_max=50
    elif difficulte =='difficile': 
        borne_max=100
    else:
        print("Difficulte invalide ! ")
        return

    n=random.randint(1,borne_max)
    #print(n)
    i=1
    p=int(input(f"Choisissez un nombre entre 1 et {borne_max} : "))
            
    while p != n :
        
        if p < n and p >= 1 and p <= borne_max:
            print("Trop petit !")
        elif p > n and p >= 1 and p <= borne_max:
            print("Trop grand !")
        else:
            print(f"Le nombre doit etre entre 1 et {borne_max} !")
        p = int(input(f"Rechoisissez un autre nombre entre 1 et {borne_max} : "))
        i += 1
    print("Bravo, trouvé ! en", i, "essais")


nombre_mystere()
