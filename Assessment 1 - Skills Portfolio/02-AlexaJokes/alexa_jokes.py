# Exercise 2 - Alexa tell me a Joke
# Developed with help from Claude (AI), permitted for this module.
import os
import random
import tkinter as tk


def load_jokes(path):
    """Read the jokes file and return a list of (setup, punchline) pairs."""
    jokes = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if "?" in line:
                setup, punchline = line.split("?", 1)
                jokes.append((setup + "?", punchline))
    return jokes


def tell_joke():
    """Pick a random joke, show its setup and clear the old punchline."""
    global current_joke
    current_joke = random.choice(jokes)
    setup_label.config(text=current_joke[0])
    punchline_label.config(text="")


def show_punchline():
    """Show the punchline of the current joke, if there is one."""
    if current_joke is not None:
        punchline_label.config(text=current_joke[1])


def quit_app():
    window.destroy()


# Build the path to the jokes file so it works on any computer
base_folder = os.path.dirname(os.path.abspath(__file__))
jokes_path = os.path.join(base_folder, "..", "A1 - Resources", "randomJokes.txt")
jokes = load_jokes(jokes_path)
current_joke = None

window = tk.Tk()
window.title("Alexa Joke Assistant")
window.geometry("500x300")

setup_label = tk.Label(window, text="", font=("Arial", 14), wraplength=450)
setup_label.pack(pady=10)

punchline_label = tk.Label(window, text="", font=("Arial", 14), wraplength=450)
punchline_label.pack(pady=10)

tk.Button(window, text="Alexa tell me a Joke", command=tell_joke).pack(pady=5)
tk.Button(window, text="Show Punchline", command=show_punchline).pack(pady=5)
tk.Button(window, text="Next Joke", command=tell_joke).pack(pady=5)
tk.Button(window, text="Quit", command=quit_app).pack(pady=5)

window.mainloop()