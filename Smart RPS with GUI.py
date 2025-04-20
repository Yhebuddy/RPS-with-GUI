import tkinter as tk
import random
from collections import Counter

# Core data
options = ['rock', 'paper', 'scissors']
user_history = []
wins = losses = draws = 0

# AI prediction
def predict_user_move(history):
    if len(history) < 5:
        return random.choice(options)
    counts = Counter(history)
    most_common = counts.most_common(1)[0][0]
    return {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }[most_common]

# Game logic
def play(user_choice):
    global wins, losses, draws
    user_history.append(user_choice)
    comp_choice = predict_user_move(user_history)
    
    comp_label.config(text=f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        result = "Draw!"
        draws += 1
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'paper' and comp_choice == 'rock') or \
         (user_choice == 'scissors' and comp_choice == 'paper'):
        result = "You win!"
        wins += 1
    else:
        result = "You lose!"
        losses += 1

    result_label.config(text=result)
    score_label.config(text=f"Wins: {wins}  Losses: {losses}  Draws: {draws}")

# GUI setup
root = tk.Tk()
root.title("Smart Rock Paper Scissors")

tk.Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

for choice in options:
    btn = tk.Button(frame, text=choice.capitalize(), width=12, height=2,
                    command=lambda c=choice: play(c))
    btn.pack(side=tk.LEFT, padx=10)

comp_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
comp_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, 'bold'))
result_label.pack(pady=5)

score_label = tk.Label(root, text="Wins: 0  Losses: 0  Draws: 0", font=("Arial", 12))
score_label.pack(pady=10)

tk.Button(root, text="Quit", command=root.destroy).pack(pady=10)

root.mainloop()