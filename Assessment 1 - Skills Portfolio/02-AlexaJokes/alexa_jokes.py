# Exercise 2 - Alexa tell me a Joke
# Developed with help from Claude (AI), permitted for this module.
import os
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
    # Placeholder - the next step shows a real joke
    print("Button clicked")


# Build the path to the jokes file so it works on any computer
base_folder = os.path.dirname(os.path.abspath(__file__))
jokes_path = os.path.join(base_folder, "..", "A1 - Resources", "randomJokes.txt")
jokes = load_jokes(jokes_path)
print(len(jokes), "jokes loaded")

window = tk.Tk()
window.title("Alexa Joke Assistant")

setup_label = tk.Label(window, text="", font=("Arial", 14))
setup_label.pack(pady=10)

punchline_label = tk.Label(window, text="", font=("Arial", 14))
punchline_label.pack(pady=10)

joke_button = tk.Button(window, text="Alexa tell me a Joke", command=tell_joke)
joke_button.pack(pady=10)

window.mainloop()