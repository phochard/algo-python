# exo 2.1 : Reprenez le code 2.3 et ajoutez-y un compteur pour calculer le nombre total d'issues. Inspirez-vous de l'exemple 2.2.

issues = 0

for i in range(0, 2):
    for j in range(0, 2):
        issues += 1
        
print(f"Il y a {issues} issues possibles.")

# exo 2.2 : Maintenant, rédigez le code qui indique toutes les issues possibles d'un lancer de dés ainsi que le nombre total d'issues. Inspirez-vous de l'exemple 2.2.

issues = 0

for i in range(0, 2):
        issues += 1
        if i == 0:
            print("Pile")
        else:
            print("face")


print(f"Il y a {issues} issues possibles.")

# exo 2.3 : Rédigez le code qui indique toutes les issues possibles de deux lancers de dés. Inspirez-vous des exemples 2.2 et 2.3.

issues = 0

for i in range(0, 2):
    for j in range(0, 2):
        issues += 1
        if i == 0:
            print("Pile", end='')
        else:
            print("face", end='')

        if j == 0:
            print(" & pile")
        else:
            print(" & face")

print(f"Il y a {issues} issues possibles.")