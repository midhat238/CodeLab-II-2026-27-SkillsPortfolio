# Exercise 2 - Alexa tell me a Joke
import tkinter as tk


def tell_joke():
    # Placeholder for now - we will load real jokes in the next step
    print("Button clicked")


window = tk.Tk()
window.title("Alexa Joke Assistant")

# Label that will show the joke setup
setup_label = tk.Label(window, text="", font=("Arial", 14))
setup_label.pack(pady=10)

# Label that will show the punchline
punchline_label = tk.Label(window, text="", font=("Arial", 14))
punchline_label.pack(pady=10)

# Button that runs tell_joke() when clicked
joke_button = tk.Button(window, text="Alexa tell me a Joke", command=tell_joke)
joke_button.pack(pady=10)

window.mainloop()