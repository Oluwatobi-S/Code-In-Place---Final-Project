# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import turtle
import random

# Announcers' reactions
announcers_reactions_good = [
    "Steph Curry in the building", "K-O-O-O-O-B-E-E-E!!!!!!", "Too Easy Man",
    "Dirt Off Your Shoulders Celebration", "MJ Shrug Celebration", "Mamba Mentality"
]

announcers_reactions_bad = [
    "Hell no boi!", "Shaqtin a Fool Highlight Reel", "Airrrrrrr-ballllllll",
    "Better luck next time mate hahahaha", "Not in my house!", 
    "Get that sh*t outta here", "No no no, not today hehehe (Cookie Monster Voice) - Mutombo Voice"
]

# NBA trivia questions
trivia_questions = [
    # Easy Questions
    {"Question 1": "Who has the most NBA championships?", 
     "choices": ["1. Michael Jordan", "2. Bill Russell", "3. LeBron James", "4. Kobe Bryant"], 
     "answer": 2},
    {"Question 2": "Who holds the record for the most points in a single game?", 
     "choices": ["1. Michael Jordan", "2. Wilt Chamberlain", "3. Kobe Bryant", "4. LeBron James"], 
     "answer": 2},
    {"Question 3": "Which team won the first NBA championship?", 
     "choices": ["1. Boston Celtics", "2. New York Knicks", "3. Philadelphia Warriors", "4. Los Angeles Lakers"], 
     "answer": 3},
    {"Question 4": "Who is known as 'The King'?", 
     "choices": ["1. Michael Jordan", "2. Bill Russell", "3. LeBron James", "4. Kobe Bryant"], 
     "answer": 3},
    {"Question 5": "Which team is known as the 'Lakers'?", 
     "choices": ["1. Los Angeles", "2. Boston", "3. New York", "4. Chicago"], 
     "answer": 1},
    # Medium Questions
    {"Question 6": "Who is the NBA's all-time leading scorer (as of 2023)?", 
     "choices": ["1. Kareem Abdul-Jabbar", "2. Karl Malone", "3. LeBron James", "4. Michael Jordan"], 
     "answer": 3},
    {"Question 7": "Which player has the most career assists in NBA history?", 
     "choices": ["1. John Stockton", "2. Jason Kidd", "3. Steve Nash", "4. Magic Johnson"], 
     "answer": 1},
    {"Question 8": "Which team has the most NBA championships?", 
     "choices": ["1. Chicago Bulls", "2. Los Angeles Lakers", "3. Boston Celtics", "4. Golden State Warriors"], 
     "answer": 3},
    {"Question 9": "Who was the youngest player to score 10,000 points in the NBA?", 
     "choices": ["1. Michael Jordan", "2. Kobe Bryant", "3. LeBron James", "4. Kevin Durant"], 
     "answer": 3},
    {"Question 10": "Who won the NBA MVP award in 2021?", 
     "choices": ["1. Giannis Antetokounmpo", "2. LeBron James", "3. Nikola Jokic", "4. Kevin Durant"], 
     "answer": 3},
    # Hard Questions
    {"Question 11": "Who was the first player to be drafted number one without playing college or high school basketball in the USA?", 
     "choices": ["1. Dirk Nowitzki", "2. Yao Ming", "3. Pau Gasol", "4. Andrea Bargnani"], 
     "answer": 2},
    {"Question 12": "Which NBA player was nicknamed 'The Round Mound of Rebound'?", 
     "choices": ["1. Shaquille O'Neal", "2. Charles Barkley", "3. Dennis Rodman", "4. Karl Malone"], 
     "answer": 2},
    {"Question 13": "Who was the first player in NBA history to be elected league MVP by a unanimous vote?", 
     "choices": ["1. Michael Jordan", "2. LeBron James", "3. Stephen Curry", "4. Shaquille O'Neal"], 
     "answer": 3},
    {"question": "Which team did Wilt Chamberlain play for when he scored 100 points in a single game?", 
     "choices": ["1. Los Angeles Lakers", "2. Philadelphia Warriors", "3. Golden State Warriors", "4. Philadelphia 76ers"], 
     "answer": 2},
    {"question": "Which player has the highest career free throw percentage?", 
     "choices": ["1. Stephen Curry", "2. Steve Nash", "3. Mark Price", "4. Ray Allen"], 
     "answer": 2},
    # NBA Fan HARD Questions
    {"question": "Who was the first foreign-born player to be inducted into the Naismith Memorial Basketball Hall of Fame?", 
     "choices": ["1. Hakeem Olajuwon", "2. Dražen Petrović", "3. Arvydas Sabonis", "4. Dirk Nowitzki"], 
     "answer": 3},
    {"question": "Who was the first player to record a quadruple-double in NBA history?", 
     "choices": ["1. Hakeem Olajuwon", "2. David Robinson", "3. Nate Thurmond", "4. Alvin Robertson"], 
     "answer": 3},
    {"question": "Which player was known as 'The Iceman'?", 
     "choices": ["1. George Gervin", "2. Walt Frazier", "3. Earl Monroe", "4. Elgin Baylor"], 
     "answer": 1},
    {"question": "Which NBA coach has the most career wins?", 
     "choices": ["1. Phil Jackson", "2. Pat Riley", "3. Gregg Popovich", "4. Don Nelson"], 
     "answer": 4},
    {"question": "Which team holds the record for the longest winning streak in NBA history?", 
     "choices": ["1. Miami Heat", "2. Golden State Warriors", "3. Los Angeles Lakers", "4. Chicago Bulls"], 
     "answer": 3}
]

def draw_court():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Tobi's Basketball Game")

    hoop = turtle.Turtle()
    hoop.color("white")
    hoop.penup()
    hoop.goto(0, 250)
    hoop.pendown()
    hoop.circle(30)
    hoop.hideturtle()

    return screen

def ask_trivia(player, question_index):
    question = trivia_questions[question_index]
    print(f"\n{player}, it's your turn to answer a trivia question!")
    print(question["question"])
    for choice in question["choices"]:
        print(choice)

    answer = int(input("Enter the number of your answer: "))
    return answer == question["answer"]

def main():
    print("Welcome to Code in Place Final Project - Tobi’s Basketball Game")
    print("\nThis game will test your ability to make consistent plays, keep your composure, and most of all, ACCURACY!")

    player1 = input("\nPlayer Number 1 - Enter your name here: ")
    player2 = input("Player Number 2 - Enter your name here: ")
    
    print("\nFirst to 21.\nLet’s go!\n")

    screen = draw_court()

    scores = {player1: 0, player2: 0}
    current_player = player1
    question_index = 0

    while scores[player1] < 21 and scores[player2] < 21:
        correct_answer = ask_trivia(current_player, question_index)

        if correct_answer:
            print(random.choice(announcers_reactions_good))
            scores[current_player] += 2
        else:
            print(random.choice(announcers_reactions_bad))

        print(f"\nScore - {player1}: {scores[player1]}, {player2}: {scores[player2]}")
        
        current_player = player2 if current_player == player1 else player1
        question_index = (question_index + 1) % len(trivia_questions)

    winner = player1 if scores[player1] >= 21 else player2
    print(f"\nCongratulations {winner}! You won the game with a score of 21!")

    screen.bye()

if __name__ == "__main__":
    main()


