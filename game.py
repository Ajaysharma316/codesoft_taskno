import tkinter as tk
import random

# Available choices
choices = ["Rock", "Paper", "Scissors"]

# Score tracking
user_score = 0
computer_score = 0

# Game logic
def play(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)
    
    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    # Update GUI labels
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {comp_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

# GUI window setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x320")
root.resizable(False, False)

# Title label
tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold")).pack(pady=15)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Result labels
user_choice_label = tk.Label(root, text="Your Choice:", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's Choice:", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0  Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()

