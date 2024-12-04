import random
number = int(input("Input a number that is a password : ")) 
guess = 0 
while (guess!= number):
    guess = random.randint(0,999999) 
    print(guess)
print("Y") 
print("your password is" + str(number)) 