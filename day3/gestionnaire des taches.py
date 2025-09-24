import os
import numpy

# Ma liste de taches
taches = []

# Fonction pour ajouter une tache
def ajouter_tache():
    print("--- Ajouter une tache ---")
    description = input("Ajoute ta tache : ")
    
    if description == "":
        print("Tu n'as rien ajoute !")
        return
    
    duree = input("Duree en minute : ")
    
    if duree != "" and duree.isdigit():
        tache_complete = description + " - " + duree + " min"
    else:
        tache_complete = description
    
    taches.append(tache_complete)
    print("Tache ajoutee !")
    
    # Sauvegarder dans le fichier
    fichier = open("taches.txt", "w")
    for i in range(len(taches)):
        fichier.write(str(i+1) + ". " + taches[i] + "\n")
    fichier.close()
    print("Sauvegarde dans taches.txt")

# Fonction pour voir toutes les taches
def voir_taches():
    print("--- Mes taches ---")
    
    if len(taches) == 0:
        print("Pas de taches !")
        
        # Essayer de lire depuis le fichier
        if os.path.exists("taches.txt"):
            print("Je lis depuis le fichier...")
            fichier = open("taches.txt", "r")
            lignes = fichier.readlines()
            for ligne in lignes:
                ligne = ligne.strip()
                if ligne != "":
                    print(ligne)
                    # Extraire juste la tache sans le numero
                    if ". " in ligne:
                        tache = ligne.split(". ")[1]
                        taches.append(tache)
            fichier.close()
        return
    
    # Afficher les taches
    for i in range(len(taches)):
        print(str(i+1) + ". " + taches[i])
    
    
    durees = []
    for tache in taches:
        if " - " in tache and " min" in tache:
            parties = tache.split(" - ")
            if len(parties) == 2:
                duree_texte = parties[1].replace(" min", "")
                if duree_texte.isdigit():
                    durees.append(int(duree_texte))
    
    if len(durees) > 0:
        durees_np = numpy.array(durees)
        print("Temps total :", numpy.sum(durees_np), "minutes")

# Fonction pour supprimer une tache
def supprimer_tache():
    print("--- Supprimer une tache ---")
    
    if len(taches) == 0:
        print("Pas de taches a supprimer !")
        return
    
    # Montrer les taches
    for i in range(len(taches)):
        print(str(i+1) + ". " + taches[i])
    
    numero = input("Quel numero supprimer ? ")
    
    if numero.isdigit():
        num = int(numero)
        if num >= 1 and num <= len(taches):
            tache_supprimee = taches[num-1]
            
            # Supprimer de la liste
            nouvelle_liste = []
            for i in range(len(taches)):
                if i != num-1:
                    nouvelle_liste.append(taches[i])
            taches.clear()
            for t in nouvelle_liste:
                taches.append(t)
            
            print("Supprime :", tache_supprimee)
            
            # Sauvegarder
            fichier = open("taches.txt", "w")
            for i in range(len(taches)):
                fichier.write(str(i+1) + ". " + taches[i] + "\n")
            fichier.close()
            
        else:
            print("Numero invalide !")
    else:
        print("Ce n'est pas un numero !")

# Programme principal
print("=== GESTIONNAIRE DE TACHES ===")

while True:
    print("\n1. Ajouter une tache")
    print("2. Voir mes taches")
    print("3. Supprimer une tache")
    print("4. Quitter")
    
    choix = input("Ton choix (1-4) : ")
    
    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        voir_taches()
    elif choix == "3":
        supprimer_tache()
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Choix invalide !")
    
    input("Appuie sur Entree...")

print("Fini !")