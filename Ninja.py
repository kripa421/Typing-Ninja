import tkinter as tk
import random
import time
import os


WORDS = ["python", "java", "computer science","representation","imagination","swift", "keyboard","extraordinary", "conversation", "laptop", "coding", "developer", "screen", "mouse", "project"]
TIME_LIMITS = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10}  # seconds based on difficulty
HIGHSCORE_FILE = "highscore.txt"


def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read().strip() or 0)
    return 0

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))

def start_game():
    global score, time_left, running, current_word
    score = 0
    time_left = TIME_LIMITS[difficulty.get()]
    running = True
    score_label.config(text=f"Score: {score}")
    timer_label.config(text=f"Time: {time_left}")
    word_label.config(text=random.choice(WORDS))
    entry.delete(0, tk.END)
    update_timer()

def update_timer():
    global time_left, running
    if running:
        if time_left > 0:
            time_left -= 1
            timer_label.config(text=f"Time: {time_left}")
            root.after(1000, update_timer)
        else:
            running = False
            word_label.config(text="⏳ Time Up! Game Over!", fg="yellow")
            if score > highscore[0]:
                highscore[0] = score
                save_highscore(score)
                hs_label.config(text=f"🏆 High Score: {highscore[0]}")
                word_label.config(text="🎉 New High Score! Game Over!", fg="gold")

def check_word(event=None):
    global score
    if running:
        typed = entry.get().strip()
        if typed == word_label.cget("text"):
            score += 1
            score_label.config(text=f"Score: {score}")
        else:
            score_label.config(text=f"Score: {score} ❌ Incorrect!")
        word_label.config(text=random.choice(WORDS))
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Typing Ninja")


root.attributes("-fullscreen", True)


root.configure(bg="#222")

score = 0
time_left = 0
running = False
current_word = ""
highscore = [load_highscore()]


tk.Label(root, text="Typing Ninja", font=("Arial", 60, "bold"), bg="#222", fg="white").pack(pady=40)


hs_label = tk.Label(root, text=f"🏆 High Score: {highscore[0]}", font=("Arial", 40), bg="#222", fg="gold")
hs_label.pack()


score_label = tk.Label(root, text="Score: 0", font=("Arial", 40), bg="#222", fg="white")
score_label.pack()


timer_label = tk.Label(root, text="Time: 0", font=("Arial", 40), bg="#222", fg="white")
timer_label.pack()


word_label = tk.Label(root, text="", font=("Arial", 80, "bold"), bg="#222", fg="#0f0")
word_label.pack(pady=40)


entry = tk.Entry(root, font=("Arial", 50), justify="center")
entry.pack(pady=20, ipadx=20, ipady=10)
entry.bind("<Return>", check_word)


difficulty = tk.IntVar(value=1)
tk.Label(root, text="Select Difficulty (1-6):", font=("Arial", 30), bg="#222", fg="white").pack(pady=10)
tk.Spinbox(root, from_=1, to=6, width=5, font=("Arial", 30), textvariable=difficulty).pack()


tk.Button(root, text="Start Game", font=("Arial", 30, "bold"), command=start_game, bg="#0a0", fg="white").pack(pady=40)


tk.Button(root, text="Exit", font=("Arial", 20), command=lambda: root.destroy(), bg="red", fg="white").pack(side="bottom", pady=20)

root.mainloop()







