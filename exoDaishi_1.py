import random

# exo 1.1 
head_or_tail = random.randint(0, 1)
print(head_or_tail)

if head_or_tail:
    print("Bob is the winner!")
else:
    print("Alice is the winner!")

# exo 1.2 
dice = random.randint(1, 6)
print(dice)

if dice < 4:
    print("The winner is Bob!")
elif dice >= 4:
    print("The winner is Alice!")

# exo 1.3 
alice = random.randint(1, 3)
bob = random.randint(1, 3)
print(alice)
print(bob)

if alice > bob:
    print("Alice wins!")
elif bob > alice:
    print("Bob wins!")
else : 
    print("Try again.")
    