import tkinter as tk
from tkinter import messagebox
import random

# -------------------- QUESTIONS (20) --------------------
questions = [
    {"question": "Who is known as 'Thala' of CSK?",
     "options": ["Virat Kohli", "MS Dhoni", "Rohit Sharma", "Raina"],
     "answer": "MS Dhoni"},

    {"question": "How many IPL titles has CSK won (till 2023)?",
     "options": ["3", "4", "5", "6"],
     "answer": "5"},

    {"question": "CSK's home ground is?",
     "options": ["Wankhede", "Chepauk", "Eden Gardens", "Chinnaswamy"],
     "answer": "Chepauk"},

    {"question": "Who is called 'Mr. IPL'?",
     "options": ["Dhoni", "Raina", "Jadeja", "Bravo"],
     "answer": "Raina"},

    {"question": "Which year CSK was banned?",
     "options": ["2014", "2015", "2016", "2017"],
     "answer": "2016"},

    {"question": "Who is CSK's all-time leading wicket-taker?",
     "options": ["Ashwin", "Bravo", "Jadeja", "Morkel"],
     "answer": "Bravo"},

    {"question": "Which player is known as 'Sir Jadeja'?",
     "options": ["Raina", "Jadeja", "Bravo", "Watson"],
     "answer": "Jadeja"},

    {"question": "Who was CSK's long-time coach?",
     "options": ["Ricky Ponting", "Stephen Fleming", "Kumble", "Dravid"],
     "answer": "Stephen Fleming"},

    {"question": "Who hit winning runs in IPL 2018 final?",
     "options": ["Dhoni", "Watson", "Raina", "Rayudu"],
     "answer": "Watson"},

    {"question": "CSK returned after suspension in which year?",
     "options": ["2017", "2018", "2019", "2020"],
     "answer": "2018"},

    {"question": "Who is known as 'DJ Bravo'?",
     "options": ["Bravo", "Pollard", "Gayle", "Russell"],
     "answer": "Bravo"},

    {"question": "Which player is famous for helicopter shot?",
     "options": ["Dhoni", "Raina", "Jadeja", "Rayudu"],
     "answer": "Dhoni"},

    {"question": "Which team defeated CSK in 2019 final?",
     "options": ["MI", "RCB", "KKR", "SRH"],
     "answer": "MI"},

    {"question": "What is CSK jersey color?",
     "options": ["Blue", "Yellow", "Red", "Green"],
     "answer": "Yellow"},

    {"question": "Who captained CSK briefly in 2022?",
     "options": ["Raina", "Jadeja", "Bravo", "Rayudu"],
     "answer": "Jadeja"},

    {"question": "Which England all-rounder played for CSK?",
     "options": ["Stokes", "Root", "Buttler", "Bairstow"],
     "answer": "Stokes"},

    {"question": "Which stadium is called 'Anbuden'?",
     "options": ["Chepauk", "Wankhede", "Eden Gardens", "Kotla"],
     "answer": "Chepauk"},

    {"question": "Who is CSK's highest run scorer?",
     "options": ["Dhoni", "Raina", "Jadeja", "Watson"],
     "answer": "Raina"},

    {"question": "Which bowler is famous for slower balls in CSK?",
     "options": ["Bravo", "Ashwin", "Deepak Chahar", "Hazlewood"],
     "answer": "Bravo"},

    {"question": "CSK is owned by which company?",
     "options": ["Reliance", "India Cements", "Tata", "Adani"],
     "answer": "India Cements"}
]

random.shuffle(questions)

# -------------------- APP --------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSK Quiz 💛")
        self.root.geometry("600x450")
        self.root.config(bg="#1e1e1e")

        self.q_index = 0
        self.score = 0
        self.time_left = 10

        tk.Label(root, text="🦁 CSK Quiz App",
                 font=("Arial", 20, "bold"),
                 fg="yellow", bg="#1e1e1e").pack(pady=10)

        self.q_label = tk.Label(root, text="", font=("Arial", 14),
                                fg="white", bg="#1e1e1e", wraplength=500)
        self.q_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12),
                            width=25, bg="yellow",
                            command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.timer = tk.Label(root, text="Time: 10",
                              font=("Arial", 12),
                              fg="red", bg="#1e1e1e")
        self.timer.pack(pady=10)

        self.load_question()
        self.countdown()

    def load_question(self):
        if self.q_index < len(questions):
            q = questions[self.q_index]
            self.q_label.config(text=q["question"])
            for i, opt in enumerate(q["options"]):
                self.buttons[i].config(text=opt)
            self.time_left = 10
        else:
            self.end_quiz()

    def check_answer(self, i):
        selected = self.buttons[i].cget("text")
        if selected == questions[self.q_index]["answer"]:
            self.score += 1
        self.q_index += 1
        self.load_question()

    def countdown(self):
        if self.time_left > 0:
            self.timer.config(text=f"Time: {self.time_left}")
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.q_index += 1
            self.load_question()
            self.countdown()

    def end_quiz(self):
        messagebox.showinfo("Quiz Over 🎉", f"Score: {self.score}/{len(questions)}")
        with open("leaderboard.txt", "a") as f:
            f.write(f"Score: {self.score}\n")
        self.root.destroy()

# -------------------- RUN --------------------
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
