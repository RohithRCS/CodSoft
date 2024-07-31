import tkinter as tk
import random

user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_score >= win_score or computer_score >= win_score:
        return ""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

def play_game(user_choice):
    if user_score >= win_score or computer_score >= win_score:
        return
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    if user_score >= win_score:
        result = "You win the game!"
    elif computer_score >= win_score:
        result = "Computer wins the game!"
    result_label.config(text=f"User: {user_choice} - Computer: {computer_choice}\n{result}")
    update_scores()

def update_scores():
    user_score_label.config(text=f"User Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()
    result_label.config(text="Choose Rock, Paper, or Scissors to start the game.")
    game_controls_frame.pack()
    win_score_frame.pack_forget()

def start_game():
    global win_score
    try:
        win_score = int(win_score_entry.get())
        if win_score <= 0:
            result_label.config(text="Please enter a positive integer for the win score.")
            return
        win_score_frame.pack_forget()
        game_controls_frame.pack()
        reset_game()
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

window = tk.Tk()
window.title("Rock, Paper, Scissors")

button_font = ('Arial', 16)

game_controls_frame = tk.Frame(window)
rock_button = tk.Button(game_controls_frame, text="Rock", width=10, height=2, font=button_font, bg='lightgrey', command=lambda: play_game("Rock"))
paper_button = tk.Button(game_controls_frame, text="Paper", width=10, height=2, font=button_font, bg='lightgrey', command=lambda: play_game("Paper"))
scissors_button = tk.Button(game_controls_frame, text="Scissors", width=10, height=2, font=button_font, bg='lightgrey', command=lambda: play_game("Scissors"))

rock_button.grid(row=0, column=0, padx=10, pady=20)
paper_button.grid(row=0, column=1, padx=10, pady=20)
scissors_button.grid(row=0, column=2, padx=10, pady=20)

result_label = tk.Label(game_controls_frame, text="Choose Rock, Paper, or Scissors to start the game.", font=('Arial', 14))
result_label.grid(row=1, column=0, columnspan=3, pady=10)

user_score_label = tk.Label(game_controls_frame, text="User Score: 0", font=('Arial', 14))
user_score_label.grid(row=2, column=0, pady=10)

computer_score_label = tk.Label(game_controls_frame, text="Computer Score: 0", font=('Arial', 14))
computer_score_label.grid(row=2, column=2, pady=10)

play_again_button = tk.Button(game_controls_frame, text="Play Again", width=10, height=2, font=button_font, bg='lightgreen', command=reset_game)
play_again_button.grid(row=3, column=0, columnspan=3, pady=20)

win_score_frame = tk.Frame(window)
tk.Label(win_score_frame, text="Enter win score:", font=('Arial', 14)).pack(side=tk.LEFT, padx=10)
win_score_entry = tk.Entry(win_score_frame, font=('Arial', 14))
win_score_entry.pack(side=tk.LEFT, padx=10)
start_button = tk.Button(win_score_frame, text="Start Game", width=10, height=1, font=button_font, bg='lightblue', command=start_game)
start_button.pack(side=tk.LEFT, padx=10, pady=10)

win_score_frame.pack()
game_controls_frame.pack_forget()

window.mainloop()