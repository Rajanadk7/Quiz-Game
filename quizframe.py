import random
import tkinter as tk
from tkinter import messagebox

# Questions for the KBC program
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Silver", "D. Hydrogen"],
        "answer": "B"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    }
]

class KBCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")

        self.score = 0
        self.question_asked = 0
        random.shuffle(questions)
        self.current_question = None

        self.question_label = tk.Label(root, text="", wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", width=50, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=20)
        self.next_button.config(state=tk.DISABLED)

        self.next_question()

    def next_question(self):
        if self.question_asked < len(questions):
            self.current_question = questions[self.question_asked]
            self.question_label.config(text=self.current_question["question"])
            for i, option in enumerate(self.current_question["options"]):
                self.option_buttons[i].config(text=option)
            self.next_button.config(state=tk.DISABLED)
            self.question_asked += 1
        else:
            messagebox.showinfo("Game Over", f"Congratulations! You scored {self.score} rupees.")
            self.root.quit()

    def check_answer(self, selected_option_index):
        selected_option = self.option_buttons[selected_option_index].cget("text")[0]
        if selected_option == self.current_question["answer"]:
            self.score += 2000000
            messagebox.showinfo("Correct!", "Correct! The next question is on the way.")
        else:
            messagebox.showinfo("Wrong!", f"Wrong! The correct answer was {self.current_question['answer']}.")
            self.root.quit()
        self.next_button.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    app = KBCApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()