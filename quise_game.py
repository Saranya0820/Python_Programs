print("Welcome To My Computer Quiz-game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "randam access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score +=1
else:
    print("Incorrect")

answer = input("What does CNG stand for? ")
if answer.lower() == "cryptographic next generation":
    print("Correct!")
    score +=1
else:
    print("Incorrect")

print("you got " + str(score) + " question correct!")
print("you got " + str((score/5) *100) + "%.")





