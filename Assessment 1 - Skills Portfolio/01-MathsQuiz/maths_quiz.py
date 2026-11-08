# Exercise 1 - Maths Quiz
# Developed with help from Claude (AI), permitted for this module.
import random
import tkinter as tk

difficulty = 1


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
    global difficulty
    difficulty = level
    displayProblem()


def displayProblem():
    """Show one problem on screen."""
    clearWindow()
    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operation = decideOperation()
    tk.Label(window, text=f"{num1} {operation} {num2} =", font=("Arial", 24)).pack(pady=30)
    tk.Button(window, text="Back to menu", command=displayMenu).pack()


window = tk.Tk()
window.title("Maths Quiz")
window.geometry("500x400")
displayMenu()
window.mainloop()