# This is a snake-water-gun game.

rounds = 3
user1Wins = 0
user2Wins = 0

def checkFinalWinner(user1Wins,user2Wins):
    if user1Wins > user2Wins:
        return "User 1 is the winner of the game!"
    elif user2Wins > user1Wins:
        return "User 2 is the winner of the game!"
    else:
        return "Game is draw!"

# We can access the global variables normally in any function, but in order to modify the value of a global variable, we must
# use the "global" keyword before the variable name inside the function, like shown below.
# Without "global" keyword it's just a normal local variable.

def winnerOfRound(round,user1Choice,user2Choice):
    global user1Wins
    global user2Wins

    if (user1Choice == user2Choice):
        return f"Round {round} is draw!"
    
    elif (user1Choice == "snake") and (user2Choice == "gun"):
        user2Wins = user2Wins + 1
        return f"User 2 wins round {round}"
    
    elif (user1Choice == "snake") and (user2Choice == "water"):
        user1Wins = user1Wins + 1
        return f"User 1 wins round {round}"
    
    elif (user1Choice == "water") and (user2Choice == "snake"):
        user2Wins = user2Wins + 1
        return f"User 2 wins round {round}"
    
    elif (user1Choice == "water") and (user2Choice == "gun"):
        user1Wins = user1Wins + 1
        return f"User 1 wins round {round}"
    
    elif (user1Choice == "gun") and (user2Choice == "water"):
        user2Wins = user2Wins + 1
        return f"User 2 wins round {round}"
    
    elif (user1Choice == "gun") and (user2Choice == "snake"):
        user1Wins = user1Wins + 1
        return f"User 1 wins round {round}"
    else:
        return "Something went wrong!"
    

rounds = int(input("Choose number of rounds -> "))

for i in range(1,rounds + 1):
    print(f"Round {i} starts!")
    print()
    user1Choice = input("User 1's turn -> ")
    user2Choice = input("User 2's turn -> ")
    print()
    print(winnerOfRound(i,user1Choice.strip(),user2Choice.strip()))
    print()


# Declare the final winner.
print(checkFinalWinner(user1Wins,user2Wins))