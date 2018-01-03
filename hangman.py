#This was made by the dankest of the dank, Brandon H, AKA: Brandank, AKA, Trap Ketchum, AKA, The Don, 
import os
import random
name = input("What's your name, vro?")    
    
strikes = 0

def start():
    print("""
 _       ____          __ _          __  __                  _            
| |     / / /_  ____ _/ /( )_____   / / / /___ _____  ____ _(_)___  ____ _
| | /| / / __ \/ __ `/ __/// ___/  / /_/ / __ `/ __ \/ __ `/ / __ \/ __ `/
| |/ |/ / / / / /_/ / /_  (__  )  / __  / /_/ / / / / /_/ / / / / / /_/ / 
|__/|__/_/ /_/\__,_/\__/ /____/  /_/ /_/\__,_/_/ /_/\__, /_/_/ /_/\__, /  
                                                   /____/        /____/ """)

def get_puzzle():
    file_names = os.listdir("topics")

    for i, f in enumerate(file_names):
        print(str(i) + ") " + f)

    choice = input("which one? ")
    choice = int(choice)

    file = "topics/" + file_names[choice]

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    

    category = lines[0]
    puzzle = random.choice(lines[1:])

    return(puzzle)


    
def show_credits():
    print("This game was made by ya boi, BagelBrandon")

def get_solved(puzzle, guesses):

    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"
            
    return solved

def get_guess():
    guess = input("Enter a letter, " + name + ": ")
    return guess

def display_board(solved):
    print(solved)

def show_result():

    if playing == False:
        print ("You suck")
        print("""
         __ __   __    __ __      __    __   ___   ____  
        |  |  | /   \ |  |  |    |  |__|  | /   \ |    \ 
        |  |  ||     ||  |  |    |  |  |  ||     ||  _  |
        |  ~  ||  O  ||  |  |    |  |  |  ||  O  ||  |  |
        |___, ||     ||  :  |    |  `  '  ||     ||  |  |
        |     ||     ||     |     \      / |     ||  |  |
        |____/  \___/  \__,_|      \_/\_/   \___/ |__|__|
                                                         
        """)

   
def play_again():
    while True:
        decision = input("Wanna play again, " + name + "(y/n)")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Enter 'y' or 'n' please.")
            
    
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    strikes = 0

    print(solved)


    while solved != puzzle and strikes < 12:
        guess = get_guess()
        if guess not in puzzle:
            strikes += 1
        
        guesses += guess
        solved = get_solved(puzzle, guesses)
        display_board(solved)
        if guess not in puzzle:
            strikes += 1
    
    show_result()

# go!
playing = True
start()

while playing == True:
    play()
    playing = play_again()

show_credits()


