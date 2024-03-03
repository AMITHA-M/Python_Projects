print("Welcome to my AI quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Father of Artificial Intelligence? ")
if answer.lower() == "john mccarthy":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Whose name is the Turing test named after? ")
if answer.lower() == "alan turing":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does LLM stand for? ")
if answer.lower() == "large language models":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Artificial Intelligence is associated with computers of which generation? ")
if answer.lower() == "fifth":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
