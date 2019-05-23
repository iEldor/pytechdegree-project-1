"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
import random

def print_header(message):
    print("\n")
    print("#" * (len(message)+8))
    print("##  {}  ##".format(message))
    print("#" * (len(message)+8))
    print("\n")

def set_highest_score(old_score, new_score):
    if old_score == 0 or new_score < old_score:
        return new_score
    else:
        return old_score

def start_game():
      
    # initialize a counter for number of tries
    attempts = 0
    
    # initialize highest score tracker
    highest_score = 0
    
    # greet the user
    print_header("Welcome to the Number Guessing Game!")

    # generate a random number in a given range 1-10
    find_me = random.randint(1,10)
    
    while True:
        guess = input("Pick a number between 1 and 10:  ")
        try:
            guess = int(guess)
            if guess < 1 or guess > 10:
                print("Numbers from 1 to 10 are accepted only")
                continue
        except ValueError as err:
            print("Oh no! [{}] is not a valid value. Please try again...".format(guess))
            continue
        else:
            attempts += 1
            if guess < find_me:
                print("It's higher!")
            elif guess > find_me:
                print("It's lower!")
            else:
                print("You got it! It took you {} tries.".format(attempts))
                highest_score = set_highest_score(highest_score, attempts)
                attempts = 0
                
                try_again = input("Do you want to play again? [Y]es, [N]o: ")
                while try_again.lower() not in ['y','n','yes','no']:
                    try_again = input("Whoops! [{}] is an invalid input. Do you want to play again? To continue playing enter 'Y' or 'Yes'. To end the game enter 'N' or 'No' """.format(try_again))
                if try_again.lower() in ['y','yes']:
                    print_header("HIGHEST SCORE IS {}".format(highest_score))
                    find_me = random.randint(1,10)
                    continue
                elif try_again.lower() in ['n','no']:
                    print_header("Closing game, see you next time!")
                    break
                    
        
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
