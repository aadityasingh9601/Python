import random

with open("poems.txt","r") as q1:
    text = q1.read()
    print(text)
    print(type(text))
    index = text.find("twinkle")
    if index == -1:
        print("NO, twinkle doesn't exists!")
    else:
        print("Yes, poem has twinkle!")


def game():
    return random.choice([1,2,3,4,5])

userScore = game()

with open("Hi-score.txt","r+") as q2:
    highScore = q2.read().strip() or "0" # Moves cursor to the end of file
    q2.seek(0) # Move the cursor to the starting, else write will act like append because of cursor position.
    if  (userScore > int(highScore)):
        q2.write(str(userScore))
        print(f"The new highScore is {userScore}")
    else:
        print(f"Your score is {userScore} & highest score is {highScore}")
