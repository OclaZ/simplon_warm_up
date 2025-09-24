import numpy as np
import json
import os

# Variables globales pour stocker les données
noms_etudiants = []
notes_array = np.array([])

def charger_donnees():
    """Charge les données du fichier JSON au démarrage"""
    global noms_etudiants, notes_array
    
    if os.path.exists("etudiants.json"):
        with open("etudiants.json", "r") as fichier:
            donnees = json.load(fichier)
            
            # Convertir le dictionnaire en listes
            noms_etudiants = list(donnees.keys())
            notes = list(donnees.values())
            notes_array = np.array(notes)
            
            print(f"Données chargées: {len(noms_etudiants)} étudiants")
    else:
        print("Nouveau fichier créé")

def sauvegarder_donnees():
    """Sauvegarde les données dans un fichier JSON"""
    # Créer un dictionnaire à partir des listes
    donnees = {}
    for i in range(len(noms_etudiants)):
        donnees[noms_etudiants[i]] = float(notes_array[i])
    
    # Sauvegarder dans le fichier
    with open("etudiants.json", "w") as fichier:
        json.dump(donnees, fichier, indent=2)
    
    print("Données sauvegardées!")

def ajouter_etudiant():
    """Ajouter un nouvel étudiant"""
    global noms_etudiants, notes_array
    
    # Demander le nom
    nom = input("Nom de l'étudiant: ")
    
    # Demander la note
    note = float(input("Note (0-20): "))
    
    # Vérifier que la note est valide
    if note < 0 or note > 20:
        print("Erreur: la note doit être entre 0 et 20")
        return
    
    # Ajouter à la liste des noms
    noms_etudiants.append(nom)
    
    # Ajouter à l'array NumPy des notes
    notes_array = np.append(notes_array, note)
    
    # Sauvegarder
    sauvegarder_donnees()
    print(f"Étudiant {nom} ajouté avec la note {note}")

def calculer_statistiques():
    """Calculer et afficher les statistiques"""
    if len(notes_array) == 0:
        print("Aucune note disponible")
        return
    
    print("\n--- STATISTIQUES ---")
    
    # Calculs avec NumPy
    moyenne = np.mean(notes_array)
    mediane = np.median(notes_array)
    variance = np.var(notes_array)
    ecart_type = np.std(notes_array)
    
    # Affichage
    print(f"Moyenne: {moyenne:.2f}")
    print(f"Médiane: {mediane:.2f}")
    print(f"Variance: {variance:.2f}")
    print(f"Écart-type: {ecart_type:.2f}")

def meilleure_pire_note():
    """Afficher la meilleure et la pire note"""
    if len(notes_array) == 0:
        print("Aucune note disponible")
        return
    
    print("\n--- MEILLEURE ET PIRE NOTE ---")
    
    # Trouver les indices avec NumPy
    index_max = np.argmax(notes_array)
    index_min = np.argmin(notes_array)
    
    # Récupérer les valeurs
    meilleure_note = notes_array[index_max]
    pire_note = notes_array[index_min]
    meilleur_etudiant = noms_etudiants[index_max]
    pire_etudiant = noms_etudiants[index_min]
    
    # Affichage
    print(f"Meilleure note: {meilleur_etudiant} - {meilleure_note}")
    print(f"Pire note: {pire_etudiant} - {pire_note}")

def afficher_tous():
    """Afficher tous les étudiants"""
    if len(noms_etudiants) == 0:
        print("Aucun étudiant")
        return
    
    print("\n--- TOUS LES ÉTUDIANTS ---")
    for i in range(len(noms_etudiants)):
        print(f"{noms_etudiants[i]}: {notes_array[i]}")

def menu():
    """Menu principal"""
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter un étudiant")
        print("2. Voir tous les étudiants")
        print("3. Voir les statistiques")
        print("4. Meilleure/Pire note")
        print("5. Quitter")
        
        choix = input("Votre choix (1-5): ")
        
        if choix == "1":
            ajouter_etudiant()
        elif choix == "2":
            afficher_tous()
        elif choix == "3":
            calculer_statistiques()
        elif choix == "4":
            meilleure_pire_note()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Choix invalide!")

# Programme principal
print("Gestionnaire d'étudiants - Version simple")
charger_donnees()
menu()