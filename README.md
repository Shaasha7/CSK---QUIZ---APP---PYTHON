# CSK---QUIZ---APP---PYTHON
An interactive desktop quiz application built using Python and Tkinter, inspired by the legendary Chennai Super Kings. This project tests users' knowledge of CSK through a fun, timer-based quiz experience with a graphical user interface.
🦁 CSK Quiz App (Python Tkinter)

An interactive desktop quiz application built using Python and Tkinter, inspired by the legendary Chennai Super Kings 💛.
This app tests your CSK knowledge with a timer-based quiz, score tracking, and leaderboard system.

🚀 Features
🎯 20 CSK-based questions
⏱️ Timer for each question
🏆 Score tracking system
📄 Leaderboard (saved locally)
🎲 Randomized question order
🖥️ GUI built using Tkinter
🧠 Tech Stack
Python 🐍
Tkinter (GUI)
File Handling
📂 Project Structure
CSK-Quiz-App/
│── app.py
│── leaderboard.txt
▶️ How to Run
Clone the repository:
git clone https://github.com/your-username/csk-quiz-app.git
Navigate into the folder:
cd csk-quiz-app
Run the app:
python app.py
💻 Full Code
import tkinter as tk
from tkinter import messagebox
import random

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

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
<img width="1916" height="908" alt="Screenshot 2026-04-05 182543" src="https://github.com/user-attachments/assets/88e83377-8116-46f1-8c12-0b8c7a5c5505" />
<img width="1907" height="928" alt="Screenshot 2026-04-05 182633" src="https://github.com/user-attachments/assets/70e6d54b-90f3-4922-8b3f-742b85826611" />
<img width="1918" height="817" alt="Screenshot 2026-04-05 182748" src="https://github.com/user-attachments/assets/5a615d62-e6ba-4bb0-bf50-c23699d3268d" />
<img width="782" height="638" alt="Screenshot 2026-04-05 182942" src="https://github.com/user-attachments/assets/fe207e6c-1c92-439c-9891-f5cf00da5f4f" />
<img width="831" height="628" alt="Screenshot 2026-04-05 183002" src="https://github.com/user-attachments/assets/bf21203d-c70b-4779-8d58-1bb6643af3bc" />
<img width="843" height="662" alt="Screenshot 2026-04-05 183018" src="https://github.com/user-attachments/assets/385b86e7-24a3-403c-a025-28d8b35046b1" />
<img width="786" height="657" alt="Screenshot 2026-04-05 183047" src="https://github.com/user-attachments/assets/2c761480-842c-410e-9791-1392af6136f2" />
<img width="1427" height="817" alt="Screenshot 2026-04-05 183200" src="https://github.com/user-attachments/assets/d303c488-1888-4023-98bc-4461ea6cdfcb" />

🎯 Future Improvements
🎵 Add CSK theme music
👤 Player name input
🧠 Difficulty levels
🌐 Convert to web app
📊 Live IPL stats integration
⭐ Support

If you like this project, give it a ⭐ on GitHub!
