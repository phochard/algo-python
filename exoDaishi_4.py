import random

# Il existe un type de données particulier en Python : le tuple.

# code 4.1
my_tuple = ('foo', 123)

# Les tuples ressemblent aux listes car on peut y lire des données à la façon d'une liste.

# code 4.2
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])

# Mais à la différence des listes, une fois que l'on a créé un tuple, on ne peut plus le changer.

# code 4.3
# Si vous activez le code suivante, vous verrez l'erreur "# TypeError: 'tuple' object does not support item assignment"
# my_tuple[0] = 'lorem'

# Cela ne vous empêche pas de changer complètement le contenu de la variable.
# Mais cela ne change rien au fait qu'on ne pas changer le tuple.

# code 4.4
my_tuple = None
# Malgré cette limitation, les tuples sont pratiques pour créer des objets composites à partir de données de base ("int", "float", "bool", "str")

# Par exemple, on peut s'en servir pour modéliser un jeu de carte à jouer.

# code 4.5
cards = []

for i in range(0, 4):
    # Dans un jeu, il y a les cartes de 1 à 10 et les têtes, dans 4 couleurs.
    # Pour les têtes : valet = 11, reine = 12 et roi = 13
    # Pour les couleurs : cœur = 0, carreau = 1, pique = 2, trèfle = 3
    for j in range(1, 14):
        if i == 0:
            color = 'rouge'
            symbol = 'cœur'
        elif i == 1:
            color = 'rouge'
            symbol = 'carreau'
        elif i == 2:
            color = 'noir'
            symbol = 'pique'
        elif i == 3:
            color = 'noir'
            symbol = 'trèfle'

        cards.append((symbol, color, j))

print(cards)

# Voici comment mélanger le jeu de carte.

# code 4.6
random.shuffle(cards)

# Voici comment tirer au hasard une carte du jeu.

# code 4.7
# sélection d'une carte au hasard
card = random.choice(cards)
print(card)
# suppression de la carte de la liste (la carte est dans les mains d'Alice)
cards.remove(card)

# Voici comment remettre une carte dans le jeu.

# code 4.8
cards.append(card)

# Voici comment tirer 1 carte du jeu, la mettre dans le paquet d'Alice et au final les remettre dans le jeu.

# code 4.9
# le paquet de carte d'Alice (au début, il est vide)
alice = []

# sélection d'une carte au hasard
card = random.choice(cards)
# suppression de la carte de la liste (la carte est dans les mains d'Alice)
cards.remove(card)
# ajout de la carte dans le paquet d'Alice
alice.append(card)

# remise des cartes d'alices dans le jeu
cards.extend(alice)
# suppression de toutes les carte d'Alices de son paquet
alice.clear()

# exo 4.1 : Rédigez le code qui affiche la valeur et la couleur de chaque carte du jeu.
cards = []

for i in range(0, 4):
    for j in range(1, 14):
        if i == 0:
            color = 'rouge'
            symbol = 'cœur'
        elif i == 1:
            color = 'rouge'
            symbol = 'carreau'
        elif i == 2:
            color = 'noir'
            symbol = 'pique'
        elif i == 3:
            color = 'noir'
            symbol = 'trèfle'

        cards.append((symbol, color, j))

print(f"les cartes sont : {cards}")
print(len(cards))

# exo 4.2 
for i in range (0,2):
    card = random.choice(cards)
    alice.append(card)
    cards.remove(card)
    i =+ 1

print(alice)

print(len(cards))

# exo 4.3 

bob =[]
for i in range (0,3):
    card = random.choice(cards)
    bob.append(card)
    cards.remove(card)
    i =+ 1

print(bob)
print(len(cards))

cards.extend(bob)
cards.extend(alice)
print(len(cards))

# exo 4.4 : Alice et Bob parient en jouant aux cartes.
# Voici comment se déroule le jeu :
# 1. Bob mélange les cartes, puis Alice tire trois cartes.
# 2. Elle parie que si un 3 (de n'importe quelle couleur) ou deux cœurs figurent parmi les cartes tirées, elle gagne.
# 3. Alice remets ses cartes dans le jeu, le mélange à nouveau, puis Bob tire 3 cartes.
# 4. Il parie que si un 7 (de n'importe quelle couleur) ou deux piques figurent parmi les cartes tirées, il gagne.
# 5. Bob remet ses cartes dans le jeu, ce qui termine une manche.
# Ils décident de faire trois manches.
# Rédigez le code qui modélise ce jeu et indiquez qui sera le gagnant des trois manches.

Alice = 0
Bob = 0

for i in range(0,3):

    random.shuffle(cards)

    alice =[]
    for i in range (0,3):
        card = random.choice(cards)
        alice.append(card)
        cards.remove(card)
        i =+ 1

    x = 0
    y = 0
    for item in alice:
        x += item.count(3)
        y += item.count('cœur')
    if x == 1 or y == 2 :
        Alice += 1
    
    cards.extend(alice)
    random.shuffle(cards)

    bob =[]
    for i in range (0,3):
        card = random.choice(cards)
        bob.append(card)
        cards.remove(card)
        i =+ 1

    x = 0
    y = 0
    for item in bob:
        x += item.count(7)
        y += item.count('pique')
    if x == 1 or y == 2 :
        Bob += 1

    cards.extend(bob)

if Alice > Bob:
    print("The winner is Alice !")
elif Bob > Alice:
    print("The winner is Bob !")
elif Alice == Bob:
    print("Egalité.")