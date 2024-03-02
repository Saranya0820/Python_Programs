import random

'''print(random.randrange(-1,11))  inclulde 11 
   print(random.randint(-1,11)) exclude 11'''

top_on_range = input("Type a Number: ")

if top_on_range.isdigit():
    top_on_range=int(top_on_range)

    if top_on_range<=0:
        print("Please Enter the number larger than 0 next time.")
        quit()

else:
    print("Please Enter the number next time")
    quit()

random_number = random.randint(0,top_on_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please a enter the number next time")
        continue

    if user_guess == random_number:
        print("you got it!")
        break   
    elif user_guess > random_number:
        print("you were about the number")
    else:
        print("you were below the number")
        
print("you got it in ", guess ,"guesses")