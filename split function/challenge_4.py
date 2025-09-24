line=input("entrer votre phrase: ")
mot_a_changer=input("entrer le mot a changer: ")
mot_de_remplacement=input("entrer le mot de remplacement: ")

# new_line1=line.split(mot_a_changer)
# new_line2=mot_de_remplacement.join(new_line1)
# print(new_line2)

new_line=mot_de_remplacement.join(line.split(mot_a_changer))
print(new_line)