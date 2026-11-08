# Exercise 1 - Maths Quiz
# Developed with help from Claude (AI), permitted for this module.
import random
import tkinter as tk
from tkinter import messagebox

QUESTIONS_PER_QUIZ = 10

# These variables remember where the player is in the quiz
difficulty = 1
question_number = 0
score = 0
attempt = 1
correct_answer = 0
answer_entry = None


def clearWindow():
    """Remove everything from the window so a new screen can be drawn."""
    for widget in window.winfo_children():
        widget.destroy()


def displayMenu():
    """Show the difficulty level menu."""
    clearWindow()
    tk.Label(window, text="MATHS QUIZ", font=("Arial", 20, "bold")).pack(pady=15)
    tk.Label(window, text="DIFFICULTY LEVEL", font=("Arial", 14)).pack(pady=5)
    tk.Button(window, text="1. Easy", width=20, command=lambda: startQuiz(1)).pack(pady=5)
    tk.Button(window, text="2. Moderate", width=20, command=lambda: startQuiz(2)).pack(pady=5)
    tk.Button(window, text="3. Advanced", width=20, command=lambda: startQuiz(3)).pack(pady=5)


def randomInt(level):
    """Return a random number with 1, 2 or 4 digits depending on the level."""
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)


def decideOperation():
    """Randomly choose addition or subtraction and return '+' or '-'."""
    return random.choice(["+", "-"])


def startQuiz(level):
    """Reset the score and begin a new quiz at the chosen level."""
    global difficulty, score, question_number
    difficulty = level
    score = 0
    question_number = 0
    nextQuestion()


def nextQuestion():
    """Move to the next question, or show the results after question 10."""
    global question_number, attempt
    if question_number >= QUESTIONS_PER_QUIZ:
        displayResults()
    else:
        question_number += 1
        attempt = 1
        displayProblem()


def displayProblem():
    """Show one problem and a box for the answer."""
    global correct_answer, answer_entry
    clearWindow()
    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operation = decideOperation()
    if operation == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    tk.Label(window, text=f"Question {question_number} of {QUESTIONS_PER_QUIZ}",
             font=("Arial", 12)).pack(pady=5)
    tk.Label(window, text=f"Score: {score}", font=("Arial", 12)).pack()
    tk.Label(window, text=f"{num1} {operation} {num2} =", font=("Arial", 24)).pack(pady=20)
    answer_entry = tk.Entry(window, font=("Arial", 16), width=10, justify="center")
    answer_entry.pack()
    answer_entry.focus()
    answer_entry.bind("<Return>", lambda event: checkAnswer())
    tk.Button(window, text="Submit", command=checkAnswer).pack(pady=15)


def isCorrect(user_answer, correct, attempt_number):
    """Check the answer, show a message and return True or False."""
    if user_answer == correct:
        messagebox.showinfo("Correct!", "Well done, that is right!")
        return True
    if attempt_number == 1:
        messagebox.showinfo("Not quite", "That is wrong. You have one more try.")
    else:
        messagebox.showinfo("Wrong", f"Sorry, the correct answer was {correct}.")
    return False


def checkAnswer():
    """Runs when Submit is clicked: marks the answer and moves on."""
    global score, attempt
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid answer", "Please enter a whole number.")
        return

    if isCorrect(user_answer, correct_answer, attempt):
        if attempt == 1:
            score += 10
        else:
            score += 5
        nextQuestion()
    elif attempt == 1:
        attempt = 2
        answer_entry.delete(0, tk.END)
    else:
        nextQuestion()


def displayResults():
    """Show the final score out of 100, a rank, and the play again option."""
    clearWindow()
    if score > 90:
        rank = "A+"
    elif score >= 80:
        rank = "A"
    elif score >= 70:
        rank = "B"
    elif score >= 60:
        rank = "C"
    elif score >= 50:
        rank = "D"
    else:
        rank = "F"

    tk.Label(window, text="Quiz complete!", font=("Arial", 20, "bold")).pack(pady=15)
    tk.Label(window, text=f"Your score: {score} out of 100", font=("Arial", 16)).pack(pady=5)
    tk.Label(window, text=f"Your rank: {rank}", font=("Arial", 16)).pack(pady=5)
    tk.Label(window, text="Would you like to play again?", font=("Arial", 12)).pack(pady=10)
    tk.Button(window, text="Play Again", width=15, command=displayMenu).pack(pady=5)
    tk.Button(window, text="Quit", width=15, command=window.destroy).pack(pady=5)


window = tk.Tk()
window.title("Maths Quiz")
window.geometry("500x400")
displayMenu()
window.mainloop()