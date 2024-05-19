import random
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

# Function to ask a question and take answer input from the user
def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    return answer

# Function to check the answer given by the user
def check_answer(question, answer):
    return question["answer"] == answer

# Function to play the game and add scores to the user according to the answer given
def play_game():
    score = 0
    question_asked = 0
    # Shuffle the questions randomly for the user
    random.shuffle(questions)
    for question in questions:
        answer = ask_question(question)
        if check_answer(question, answer):
            score += 2000000
            print("Correct! The next question is on the way.")
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
            break  # Exit the loop if the answer is wrong
        question_asked += 1
        # If player wants to quit the game after a question
        if input("Do you want to continue the game? (yes/no): ").strip().lower() != "yes":
            break
    print(f"Game over! You scored {score} rupees.")

if __name__ == "__main__":
    play_game()