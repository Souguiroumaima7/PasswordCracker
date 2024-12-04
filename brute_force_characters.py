import random
character = "1238ytreziujjgffjvjccdcdjjcqcrolmq@"
character_list = list(character)
password =input("Enter your password :")
guess = ""
while (guess != password):
    guess = random.choice(character_list , k=len(password))
    print(guess)
    guess = "".join(guess)
    print(guess)
    print("Enter your password: " + guess)