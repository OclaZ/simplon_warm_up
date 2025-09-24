
print('CALCULATRICE')
try:
        nombre1=float(input('entrer le premier nombre :'))
        nombre2=float(input('entrer le deuxieme nombre :'))

        operation=input("entrez l'operation [ + , - , *, / ] :")
        print(type(operation))

        if operation=='+':
            resultat=nombre1+nombre2
            print(f"{nombre1} + {nombre2} = {resultat}")
        elif operation == '-':
            resultat = nombre1 - nombre2
            print(f"{nombre1} - {nombre2} = {resultat}")
            
        elif operation == '*':
            resultat = nombre1 * nombre2
            print(f"{nombre1} * {nombre2} = {resultat}")
        elif operation == "/":
            try:
                resultat = nombre1 / nombre2
                print(f"{nombre1} / {nombre2} = {resultat}")
            except ZeroDivisionError:
                print("Erreur: division par zero impossible ")
        else:
            print('operation inconnue')
except ValueError:
            print("Erreur:entrer des nombres valides!")
    
