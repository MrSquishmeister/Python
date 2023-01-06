import random
import os

mtitle = ("Master", "Sir", "Knight", "Mr", "Doctor", "Emperor", "Dictator", "Agent", "Pope", "Lord", "Prince", "Duke", "Wizard")
ftitle = ("Princess", "Duchess", "Countess", "Baroness", "Madam", "Mistress", "Maid", "Fairy", "Mrs", "Miss")
syntax = ("Icy", "Premium", "Imperfect", "True", "Momentous", "Tart", "Chivalrous", "Venomous", "Sheep", "Cannon" ,"Stale", "Magical", "Sweet")
extra = ("Control Fire", "Control Water", "Control Electricity", "Read Minds", "Camoflarge Anywhere", "Heal")
num = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")

mchar = ((random.choice(mtitle)) + (random.choice(syntax)) + (random.choice(syntax))) 
#male username
fchar = ((random.choice(ftitle)) + (random.choice(syntax)) + (random.choice(syntax))) 
#female username

rtitle = ((random.choice(mtitle + ftitle)))
rsyntax = ((random.choice(syntax)) + (random.choice(syntax)))
rchar = (rtitle + rsyntax)
#completely random character

gender = input("Select a gender 1=Male 2=Female: ")
print()
#user picks gender and username created matches critera


if gender == 1:
    print("You:")
    print("-------------------------------")
    print("Username: " + (mchar))
    print("-------------------------------")
    print(("-Brains: ") + (random.choice(num)))
    print(("-Attack: ") + (random.choice(num)))
    print(("-Defence: ") + (random.choice(num)))
    print(("-Followers: ") + (random.choice(num)))
    print(("-Ability to: ") + (random.choice(extra)))
else:
    print("You:")
    print("-------------------------------")
    print("Username: " + (fchar))
    print("-------------------------------")
    print(("-Brains: ") + (random.choice(num)))
    print(("-Attack: ") + (random.choice(num)))
    print(("-Defence: ") + (random.choice(num)))
    print(("-Followers: ") + (random.choice(num)))
    print(("-Ability to: ") + (random.choice(extra)))

print()
print("VS")
print()
print("Opponent:")
print("-------------------------------")
print("Username: " + (rchar))
print("-------------------------------")
print(("-Brains: ") + (random.choice(num)))
print(("-Attack: ") + (random.choice(num)))
print(("-Defence: ") + (random.choice(num)))
print(("-Followers: ") + (random.choice(num)))
print(("-Ability to: ") + (random.choice(extra)))


