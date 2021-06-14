#code

import time  # imports: time is imported for the ability to add delays
import random  # to randomize dice
import math  # some math calculations
import sys

user1 = ["user1", "password1"]  # Users and their passwords
user2 = ["user2", "password2"]

user1auth = False  # Users are not authenticated yet
user2auth = False

user1score = 0  # set global variables for later use
user2score = 0

winner = 0  # no winner yet

Turn = 1
 
 
def login():  # authentication algorithm
    print("\r\n")
    inputusername = str(input("Enter Username:"))  # checks username
    if inputusername == user1[0]:
        print("Welcome Back User 1!")
        inputpassword = str(input("Enter Password:"))  # checks password
        if inputpassword == user1[1]:
            print("Successfully Logged in")
            global user1auth
            user1auth = True  # authenticates user1
        else:
          
            print("Login Failed, Try Again")
    elif inputusername == user2[0]:
        print("Welcome Back User 2!")
        inputpassword = str(input("Enter Password:"))  # checks password
        if inputpassword == user2[1]:
            print("Successfully Logged in")
            global user2auth
            user2auth = True  # authenticates user1

        else:
            print("Login Failed, Try Again")  # displays error messages
    else:
        print("Username not found, try again")


def diceroll():  # random dice algorithm
    num = (random.randint(1, 6))  # rolls dice 1
    num2 = (random.randint(1, 6))  # rolls dice 2
    sys.stdout.write("Dice 1: ")  # outputs results slowly
    time.sleep(0.75)
    sys.stdout.write(str(num))
    print("")
    time.sleep(0.5)
    sys.stdout.write("Dice 2: ")
    time.sleep(0.75)
    sys.stdout.write(str(num2))
    print("")
    time.sleep(0.5)
    if ((num + num2) % 2) == 0:
        print("The Total Is An Even Number! + 10 Score")  # the total is an even number, notifies the user
        score = num + num2 + 10
    else:
        print("The total is an odd number -5 Score!")  # the total is an odd number, notifies the user
        score = num + num2 - 5

    if num == num2:
        print("")
        input("*****Double Dice! Press Enter To Roll An Extra Die*****")  # Prompts user to claim their extra die roll
        num3 = (random.randint(1, 6))
        time.sleep(0.5)
        sys.stdout.write("The extra dice scored a ")  # tells the user what they got
        time.sleep(0.75)
        sys.stdout.write(str(num3))
        score = score + num3
    return score  # returns the total score


def play():
    if not user1auth:  # checks if users are authenticated
        print("User 1 not logged in, login first to play")  # shows error message
    elif not user2auth:
        print("User 2 not logged in, login first to play")
    else:
        print("Starting Game...")
        global Turn  # imports global variables for later modification
        global user1score
        global user2score
        global winner
        roundsplayed = 0  # resets variables before game start
        Turn = 1
        user1score = 0
        user2score = 0
        winner = 0
        time.sleep(0.5)
        while roundsplayed < 5:  # lets the users play 5 rounds max
            print("\r\n\r\n")
            input("It's User " + str(Turn) + "'s Turn Press Enter To Roll The Dice")  # prompts user to roll dice
            thescore = diceroll()  # uses algorithm to randomize scores
            if Turn == 1:  # checks whos turn it is
                Turn = 2  # changes turn to other players turn for the next game
                olduser1score = user1score  # store old score for later use
                user1score = user1score + thescore  # add the diceroll score to total score of user 1
                print("")
                time.sleep(0.75)
                sys.stdout.write("User 1 Score: ")  # display scores of users
                time.sleep(1.25)
                sys.stdout.write(str(user1score) + " (" + str(
                    user1score - olduser1score) + ")")  # uses the old score to calculate and display the change of the score
                print("")
                time.sleep(0.75)
                sys.stdout.write("User 2 Score: ")
                time.sleep(1.25)
                sys.stdout.write(str(user2score))
                print("")
                time.sleep(0.75)
                print("Rounds Played: " + str(math.floor(roundsplayed)))  # display rounds played
            else:
                Turn = 1  # EVERYTHING IS THE SAME EXCEPT ITS USER2
                olduser2score = user2score
                user2score = user2score + thescore
                print("")
                time.sleep(1)
                sys.stdout.write("User 1 Score: ")
                time.sleep(1.25)
                sys.stdout.write(str(user1score))
                print("")
                time.sleep(1)
                sys.stdout.write("User 2 Score: ")
                time.sleep(1.25)
                sys.stdout.write(str(user2score) + " (" + str(user2score - olduser2score) + ")")
                print("")
                time.sleep(1)
                print("Rounds Played: " + str(math.floor(roundsplayed)))

            roundsplayed = roundsplayed + 0.5  # only 0.5 rounds are played because player 2 hasnt played their turn yet
        if user1score == user2score:  # end of the game does both users have same score?
            print("Well Well Well, Both Players Have The Same Score, You know what this means.")
            Turn = 1  # sets variables
            user1luck = 0  # create new variables for later use
            user2luck = 0
            while user1score == user2score:  # repeat until one of the players win
                if Turn == 1:
                    input("User 1 Press Enter To Roll A Die")  # prompts to roll dice
                    luckyscore = random.randint(1, 6)  # calculates score randomly
                    user1luck = luckyscore  # adds to user1 score
                    print("")
                    time.sleep(0.5)
                    sys.stdout.write("Dice 1: ")
                    time.sleep(2)
                    sys.stdout.write(luckyscore)  # displays score
                    print("")
                else:
                    input("User 2 Press Enter To Roll A Die")  # prompts user 2 to roll a die
                    luckyscore = random.randint(1, 6)  # calculates score randomly
                    user2luck = luckyscore  # adds to user2 score
                    print("")
                    time.sleep(0.5)
                    sys.stdout.write("Dice 1: ")
                    time.sleep(2)
                    sys.stdout.write(luckyscore)  # displays score
                    print("")
                if user1luck > user2luck and user1luck != user2luck:  # if user 1 has a higher score and user 2 and user 1 doesnt have the same scores then
                    winner = 1  # user1 is winner
                    time.sleep(0.5)
                    sys.stdout.write("User 1 WINS With a Score OF: ")  # code displays user 1's win
                    time.sleep(0.7)
                    sys.stdout.write(str(user1luck + user1score))  # the last die is added to final score
                else:
                    winner = 2  # winner is user 2
                    time.sleep(0.5)
                    sys.stdout.write("User 2 WINS With a Score OF: ")  # user2's win is displayed
                    time.sleep(0.7)
                    sys.stdout.write(str(user2luck + user2score))  # user2's last die is added to final score
        else:  # if the players didnt have the same score
            if (user1score > user2score):  # if user 1 has a higher score and user 2 and user 1 doesnt have the same scores then
                winner = 1
                time.sleep(0.5)
                sys.stdout.write("User 1 WINS With a Score OF: ")  # code displays user 1's win
                time.sleep(0.7)
                sys.stdout.write(str(user1score))
            else:
                winner = 2
                time.sleep(0.5)
                sys.stdout.write("User 2 WINS With a Score OF: ")  # user2's win is displayed
                time.sleep(0.7)
                sys.stdout.write(str(user2score))

        print("")
        command1 = str(
            input("Do You Want To Save Score? (Y)es or (N)o >"))  # prompts user if they want to save the score
        if command1.lower() == "y":  # if they do
            filename = "saves.txt"
            yourname = input("Your Name:")  # prompts users name
            if len(yourname) < 15:  # makes sure users name isnt too long
                if winner == 1:
                    with open(filename, "a") as myfile:  # opens saves.txt
                        myfile.write("\r\n" + yourname + " :" + str(user1score))  # appends the score
                        myfile.close()  # closes file
                elif winner == 2:
                    with open(filename, "a") as myfile:  # appens the score
                        myfile.write("\r\n" + yourname + " :" + str(user2score))  # appends score
                        myfile.close()  # closes file
            else:
                print(
                    "Your name is too long, make sure it isnt more than 15 characters")  # warns the user that their name is too long
                yourname = input("Your Name:")  # prompts users name
                if len(yourname) < 15:  # makes sure users name isnt too long
                    if winner == 1:
                        with open(filename, "a") as myfile:  # opens saves.txt
                            myfile.write("\r\n" + yourname + " :" + str(user1score))  # appends the score
                            myfile.close()  # closes file
                    elif winner == 2:
                        with open(filename, "a") as myfile:  # appens the score
                            myfile.write("\r\n" + yourname + " :" + str(user2score))  # appends score
                            myfile.close()  # closes file


file = open("saves.txt", "r") #opens the file for reading
thefilecontents = file.read()
file.close()
theresults = thefilecontents.splitlines() #reads the file and splits by newline
scoresofpeople = [] #create variables for later use
namesofpeople = []

for i in theresults: #every result will be categorized
    category0 = i.split(":")[0]
    category1 = i.split(":")[1]
    namesofpeople.append(category0)
    scoresofpeople.append(category1)

scoresofpeoplee = [] #make the list an integer
for i in range(len(scoresofpeople)):
  scoresofpeoplee.append(int(scoresofpeople[i]))

scoresofpeoplee, namesofpeople = zip(*sorted(zip(scoresofpeoplee, namesofpeople))) #sort the lists together
scoresofpeoplee = scoresofpeoplee[::-1]
namesofpeople = namesofpeople[::-1]


print("========TOP 5 PLAYERS OF ALL TIME========") #list top 5 players
for i in range(len(scoresofpeoplee)):
    print(namesofpeople[i] + ": " + str(scoresofpeoplee[i]))

while True:
    command = str(input("(L)ogin or (P)lay: ")) #let the players login
    if command.lower() == "l":
        login()
    elif command.lower() == "p":
        play()
