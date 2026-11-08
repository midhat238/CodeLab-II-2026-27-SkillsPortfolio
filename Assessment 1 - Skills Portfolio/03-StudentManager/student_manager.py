# Exercise 3 - Student Manager
# Developed with help from Claude (AI), permitted for this module.
import os
import tkinter as tk
from tkinter import messagebox


class Student:
    """Holds one student's data and works out their results."""

    def __init__(self, code, name, mark1, mark2, mark3, exam):
        self.code = code
        self.name = name
        self.marks = [mark1, mark2, mark3]
        self.exam = exam

    def coursework_total(self):
        return sum(self.marks)

    def percentage(self):
        # Marks available: 60 coursework + 100 exam = 160
        return (self.coursework_total() + self.exam) / 160 * 100

    def grade(self):
        pct = self.percentage()
        if pct >= 70:
            return "A"
        elif pct >= 60:
            return "B"
        elif pct >= 50:
            return "C"
        elif pct >= 40:
            return "D"
        else:
            return "F"

    def summary(self):
        """Return this student's results as text for the output box."""
        return (f"Student name:      {self.name}\n"
                f"Student number:    {self.code}\n"
                f"Coursework total:  {self.coursework_total()} / 60\n"
                f"Exam mark:         {self.exam} / 100\n"
                f"Overall:           {self.percentage():.1f}%\n"
                f"Grade:             {self.grade()}\n")


def load_students(path):
    """Read the marks file and return a list of Student objects."""
    students = []
    with open(path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    # The first line is the number of students, so skip it
    for line in lines[1:]:
        if line.strip() == "":
            continue
        parts = line.split(",")
        students.append(Student(parts[0].strip(), parts[1].strip(),
                                int(parts[2]), int(parts[3]),
                                int(parts[4]), int(parts[5])))
    return students


def show_text(text):
    """Put text into the output box, replacing what was there."""
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, text)
    output_box.config(state="disabled")


def view_all():
    """Menu item 1: every student, then a class summary."""
    text = ""
    for student in students:
        text += student.summary() + "\n"
    average = sum(s.percentage() for s in students) / len(students)
    text += f"Number of students in class: {len(students)}\n"
    text += f"Average percentage mark:     {average:.1f}%\n"
    show_text(text)


def view_one():
    """Menu item 2: find a student by number or by name."""
    search = search_entry.get().strip().lower()
    if search == "":
        messagebox.showwarning("Search", "Enter a student name or number first.")
        return
    matches = [s for s in students
               if search == s.code or search in s.name.lower()]
    if not matches:
        show_text("No student found.")
    else:
        show_text("\n".join(s.summary() for s in matches))


def view_highest():
    """Menu item 3: the student with the highest overall mark."""
    best = max(students, key=lambda s: s.percentage())
    show_text("HIGHEST SCORE\n\n" + best.summary())


def view_lowest():
    """Menu item 4: the student with the lowest overall mark."""
    worst = min(students, key=lambda s: s.percentage())
    show_text("LOWEST SCORE\n\n" + worst.summary())


# Build the path to the marks file so it works on any computer
base_folder = os.path.dirname(os.path.abspath(__file__))
marks_path = os.path.join(base_folder, "..", "A1 - Resources", "studentMarks.txt")
students = load_students(marks_path)

window = tk.Tk()
window.title("Student Manager")
window.geometry("600x600")

tk.Label(window, text="STUDENT MANAGER", font=("Arial", 18, "bold")).pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack()
tk.Button(button_frame, text="1. View all students", width=22, command=view_all).grid(row=0, column=0, padx=5, pady=3)
tk.Button(button_frame, text="3. Highest score", width=22, command=view_highest).grid(row=0, column=1, padx=5, pady=3)
tk.Button(button_frame, text="4. Lowest score", width=22, command=view_lowest).grid(row=1, column=1, padx=5, pady=3)

search_frame = tk.Frame(window)
search_frame.pack(pady=8)
tk.Label(search_frame, text="Name or number:").pack(side="left")
search_entry = tk.Entry(search_frame, width=18)
search_entry.pack(side="left", padx=5)
tk.Button(search_frame, text="2. View student", command=view_one).pack(side="left")

output_box = tk.Text(window, width=65, height=22, font=("Courier", 11), state="disabled")
output_box.pack(padx=10, pady=10)

window.mainloop()