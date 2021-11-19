import bs4
import requests
import time
from random import randint
from random import choice
from random import sample
import sqlite3 as sq
import pandas as pd

letters = ["a","b","c","d"]


def BaseQuizController():

    def __init__(self):
        # Get all vocabulary from external source.

    def __call__(self):
        # Game play logic happens here.


def NotebookQuizController(BaseQuizController):
    pass


def FlaskQuizController(BaseQuizController):
    pass


def Quiz(self):
    
        # Init variables 
        play = True
        ques = 1
        points = 0
        name = input("Please enter your name: ")
        print("\nGathering words, just a moment please....")


        # Get all the words
        quiz_words = Spanish.get_words(" ")

        # Interactive loop while condition true
        while play is True:

            # Pulls 4 random words as quiz choices 
            for x in range(1):
                choices = sample(list(quiz_words),4)
                rword = choice(choices)

                question = "What is the correct translation?"

                print(f"Total Points:{points}\n")
                print(f"Question {ques}) {question}\nWord: {rword}\n\n")
                print("Choices: ")

            # Gather reference to words based on strings
            options = list(quiz_words[x] for x in choices)

            # String formatting for screen
            for i in range(len(options)):
                op = str(letters[i]) + ")" + str(options[i])
                print(op)

            answer = input("\nEnter answer a,b,c or d:\nYour answer:")
            print("\n")

            # Ensure answer could be valid
            if answer.lower() in letters:
                # Ensure answer matches
                if quiz_words[rword] == options[letters.index(answer.lower())]:
                    # Add points to user score
                    points += 1

                    print("Correct, plus 1 point!")

                else:
                    print("Incorrect\n")
                    print(f"The correct answer is '{quiz_words[rword]}'") 

            else:
                print("Enter a valid input")

            # Print score and prompt to continue
            print(f"Total Points:{points}\n")
            again = input("Play again? y/n: ")
            print("\n\n")

            if again == 'y' or again == 'Y' or again == 'yes' or again == 'Yes':
                ques += 1
                continue

            elif again == 'n' or again == 'N' or again == 'no' or again == 'No':
                perc = round(((int(points)/int(ques))*100),2)
                new_row = [name,points,ques,perc]
                
                # Connect to score database
                conn = sq.connect('hiscores.db')
                c = conn.cursor()
                c.execute("""CREATE TABLE if not exists hiscores (Name text, Points int, Questions int, Percent real)""")
                c.execute("INSERT INTO hiscores VALUES (?, ?, ?, ?)", (new_row))
                conn.commit()
                conn.close()

                # Final message
                print(f"{name} scored {points} point(s) off of {ques} question(s)\n")
                print(f"Percent Correct:{perc}%\n")
                print("Saving score...\n")
                time.sleep(1)
                print("Thanks for playing")
                play = False