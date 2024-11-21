import random
import time


# item options in list 
choices = ["ROCK", "PAPER", "SCISSORS"]
opponents = ["'Iron' Mike Tyson", "Donald 'The Don' Trump", "Sponge 'crabby patty' bob"]

# pause between certain events
def pause():
    time.sleep(1.5)

# function to show instructions
def game_instructions():
    print("-- ROCK | PAPER | SCISSORS --")
    print("Rules \nRock beats Scissors \nScissors beats Paper \nPaper beats rock")


# generate a random opponent from the list
#def generate_opponent():
#    num = random.randint(0, 2)
#    opponent = opponents[num]
#    return opponent


# beginning of each round 
def startRound(player_name, opponent):
    random_choice_num = random.randint(0, 2)
    opponent_choice = choices[random_choice_num]
    pause()
    print(player_name +" v "+ opponent)
    pause()
    print("May the best player win")
    print("--------------------------")
    pause()
    print("If you can guess the number I am thinking of between 0-10 you can see your opponent's choice before you chose!")
    pause()
    actual_num = random.randint(0,10)
    guess = input("Make your guess: ")
    if (guess == actual_num):
        pause()
        print(opponent + " chose... "+opponent_choice)
    else:
        print("Wrong guess!")

    player_choice = input("Type rock paper or scissors IN BLOCK CAPITALS: ")
    winner = outcome(player_choice, opponent_choice, player_name, opponent)
    print("The...")
    pause()
    print("winner...")
    pause()
    print("is...")
    pause()
    print(winner)


# game outcome logic
def outcome(player_choice, opponent_choice, player_name, opponent):
    pause()
    print("You chose... "+player_choice)
    pause()
    print(opponent + " chose... "+opponent_choice)
    pause()
    winner = ""
    if(
        player_choice == "ROCK" and opponent_choice == "SCISSORS" or
        player_choice == "SCISSORS" and opponent_choice == "PAPER" or
        player_choice == "PAPER" and opponent_choice == "ROCK"
        ): 
          winner = player_name
    elif(
        opponent_choice == "ROCK" and player_choice == "SCISSORS" or
        opponent_choice == "SCISSORS" and player_choice == "PAPER" or
        opponent_choice == "PAPER" and player_choice == "ROCK"
        ): 
          winner = opponent

    elif(opponent_choice == player_choice):
        winner = "No one!"
    else:
        print("Incorrect input try again\n" + startRound())
        winner = ""

    return winner
    

# function to end game 
def endGame():
    print("----------Bye-----------")
    print("------------------------")

def playerInfo():
    player_name = input("Choose your username: ")
    pause()
    print("Hello " + player_name)
    pause()

# check if player wants to play
def playGame():
    print("------------------------")
    print("--------Welcome---------")
    pause()
    play = input("Do you want to play? type Y or N ")
    if(play == "Y"):
        game_status = True
        player_name = input("Choose your username: ")
        pause()
        print("Hello " + player_name)
        pause()
        startGame(game_status, player_name)
    elif play == "N":
        print("Bye")
        game_status = False
    else:
        print("Incorrect input")
        game_status = ""
        playGame()

    return game_status

# function to start game
def startGame(game_status, player_name):
    while(game_status):
        pause()
        input("Hit enter to reveal your opponent")
        num = random.randint(0, 2)
        opponent = opponents[num]
        # opponent = generate_opponent()
        pause()
        print("Your opponent is... " + opponent)
        pause()
        startRound(player_name, opponent)

playGame()