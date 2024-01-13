import tkinter as tk
import random

def on_choice(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    update_result(player_choice, computer_choice)
    update_score(determine_winner(player_choice, computer_choice))

def update_result(player_choice, computer_choice):
    result_text.set(f"Your choice: {player_choice.capitalize()}\nComputer's choice: {computer_choice.capitalize()}")

def determine_winner(player_choice, computer_choice):
    outcomes = {
        ('rock', 'scissors'): 'win',
        ('paper', 'rock'): 'win',
        ('scissors', 'paper'): 'win',
        ('scissors', 'rock'): 'lose',
        ('rock', 'paper'): 'lose',
        ('paper', 'scissors'): 'lose'
    }
    if player_choice == computer_choice:
        return 'tie'
    return outcomes.get((player_choice, computer_choice))

def update_score(result):
    global player_score, computer_score
    if result == 'win':
        player_score += 1
    elif result == 'lose':
        computer_score += 1
    score_text.set(f"Score - You: {player_score}, Computer: {computer_score}")

# Setting up the GUI window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

player_score, computer_score = 0, 0

# Text for displaying results and score
result_text = tk.StringVar()
score_text = tk.StringVar()

# Creating buttons and labels
rock_button = tk.Button(root, text="Rock", command=lambda: on_choice("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: on_choice("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: on_choice("scissors"))
result_label = tk.Label(root, textvariable=result_text)
score_label = tk.Label(root, textvariable=score_text)

# Placing buttons and labels in the window
rock_button.pack()
paper_button.pack()
scissors_button.pack()
result_label.pack()
score_label.pack()

# Initialize score display
score_text.set("Score - You: 0, Computer: 0")

# Start the GUI event loop
root.mainloop()
