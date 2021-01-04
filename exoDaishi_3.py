import random

# exo 3.1 
issues = 0
counter = 0
for i in range(0, 2):
    for j in range(0, 2):
        issues += 1
        if i == 0 and j == 0:
            
            counter += 1

probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir pile & pile avec deux lancers")

# exo 3.2 
issues = 0
counter = 0
for i in range(0, 2):
    for j in range(0, 2):
            for k in range(0,2):
                issues += 1

                if i == 0 and j == 0:
                    
                    counter += 1

probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir pile & pile lors des deux premiers lancers sur les trois au total")

# exo 3.3 : Alice parie qu'elle va obtenir au moins 2 fois pile, avec 3 lancers.
# Avant d'écrire le code, détaillez toutes les issues possibles pour Alice.
# Puis rédigez le code qui indique la probabilité que Alice gagne.
issues = 0
counter = 0
for i in range(0, 2):
    for j in range(0, 2):
            for k in range(0,2):
                issues += 1

                if i == 0:
                    print("Pile", end='')
                else:
                    print("Face", end='')

                if j == 0:
                    print(" & pile", end='')
                else:
                    print(" & face", end='')
                    
                if k == 0:
                    print(" & pile")
                else:
                    print(" & face")   
                     
                    counter += 1

probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir pile & pile lors des trois lancers")