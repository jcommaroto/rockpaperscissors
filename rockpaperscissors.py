import time
import random
import sys

cpuWins = 0
humanWins = 0
draws = 0

print("Welcome to the game. \n")
time.sleep(1.5)
userName = input("What is your name? ")
print("\n ")
print("Hello ", userName, " \n ")
time.sleep(2)

def wantToPlay():
    gameResponse = input("Want to play rock, paper, scissors? yes/no ")
    gamerGuess(gameResponse.lower())

def gamerGuess(gameResponse):
    if gameResponse == "yes" or gameResponse == "y":
        time.sleep(1.5)
        howToPlay()

    elif gameResponse == "no" or gameResponse == "n":
        print("Sorry to hear that. Perhaps another time.")
    else:
        print("Sorry, I didn't understand your reply. Please try again.")

def howToPlay():
    print("\n")
    print("This is a simple but fun game \n")
    time.sleep(1.5)
    print("Make your choice", userName)
    print("\n")
    startGame()

def startGame():
    scoreBoard()
    time.sleep(2)
    userChoice = input("Rock, paper or scissors? ")
    testChoice(userChoice.lower())
    
def testChoice(userChoice):    
    userChoice.lower()
    if userChoice == "rock" or userChoice == "paper" or userChoice == "scissors":
        print("\n")
        print("You have chosen", userChoice, "\n")
        computerChoice(userChoice)
    else:
        print("That is not a valid choice. Try again.")
        startGame()
        
def computerChoice(userChoice):
    choices = ['rock','paper','scissors']
    computerChoice = random.choice(choices)
    time.sleep(2)
    print("I have chosen", computerChoice, "\n")
    time.sleep(2)
    choices = userChoice + computerChoice
    findWinner(choices)

def findWinner(choices):
    global cpuWins
    global humanWins
    global draws
    tieSayings = ["It's a tie", "Great minds think alike.", "A tie, wow that's boring.", "Tie rhymes with pie. Are you hungry? I am.", "A tie? But I wanted to crush you like an egg!", "Boo, it's a tie!", "A tie? How about I give you $5 and you declare me the winner instead... No? Fine.", "...great... a tie... boring"]
    if choices == "rockrock":
        print(random.choice(tieSayings))
        print("\n")
        draws += 1
        startGame()
    elif choices == "paperpaper":
        print(random.choice(tieSayings))
        print("\n")
        draws += 1
        startGame()
    elif choices == "scissorsscissors":
        print(random.choice(tieSayings))
        print("\n")
        draws += 1
        startGame()
    elif choices == "rockpaper":
        print("I win, paper covers rock.")
        print("\n")
        cpuWins += 1
        startGame()
    elif choices == "paperrock":
        print("You win, paper covers rock")
        print("\n")
        humanWins += 1
        startGame()
    elif choices == "rockscissors":
        print("You win, rock destroys scissors")
        print("\n")
        humanWins += 1
        startGame()
    elif choices == "scissorsrock":
        print("I win, rock destroys scissors")
        print("\n")
        cpuWins += 1
        startGame()
    elif choices == "paperscissors":
        print("I win, scissors cut paper!")
        print("\n")
        cpuWins += 1
        startGame()
    elif choices == "scissorspaper":
        print("You win, scissors cut paper")
        print("\n")
        humanWins += 1
        startGame()
    else:
        print("Something Went Wrong")

def scoreBoard():
    time.sleep(.5)
    totalScore = cpuWins + humanWins + draws
    testCondition = totalScore / 5
    if totalScore == 0:
        pass
    elif cpuWins - humanWins >= 2:
        quitNow = input("I am beating you pretty badly. Ready to quit? yes/no ")
        quitNow.lower()
        if quitNow == "yes" or quitNow == "y":
            print("\n")
            print("I win!!! Goodbye ", userName)
            sys.exit()
        elif quitNow == "no" or quitNow == "no":
            print("\n")
            print("I knew you weren't a quitter", userName)
            print("\n")
            print("Scoreboard:", userName, " ", humanWins, " Me ", cpuWins, " Draws ", draws)
            print("\n")
            return
        else:
            print("\n")
            print("I don't know what you are saying ", userName, " let's keep playing.")
            print("\n")
            print("Scoreboard:", userName, " ", humanWins, " Me ", cpuWins, " Draws ", draws)
            print("\n")
            return
    elif humanWins - cpuWins >= 3:
        print("You are beating me pretty badly ",userName, ". I quit")
        sys.exit()
    elif testCondition%1==0:
        quitNow = input("Tired of playing yet? yes/no ")
        quitNow.lower()
        if quitNow == "yes" or quitNow == "y":
            print("Then I win quitter!!! Goodbye ", userName)
            sys.exit()
        elif quitNow == "no" or quitNow == "no":
            print("\n")
            print("I knew you weren't a quitter", userName)
            print("\n")
            print("Scoreboard:", userName, " ", humanWins, " Me ", cpuWins, " Draws ", draws)
            print("\n")
            return
        else:
            print("\n")
            print("I don't know what you are saying ", userName, " let's keep playing.")
            print("\n")
            print("Scoreboard:", userName, " ", humanWins, " Me ", cpuWins, " Draws ", draws)
            print("\n")
            return
    else:
        print("Scoreboard:", userName, " ", humanWins, " Computer ", cpuWins, " Draws ", draws)
        print("\n")
        return

if __name__ == "__main__":
    wantToPlay()