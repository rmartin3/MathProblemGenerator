import numpy as np
import generate
import tkinter as tk
from tkinter import *

def main():
    def generate_caller():
        generate.worksheet(int(num_problem_text.get()), clicked.get(), int(range_text.get()))

    options = [
        "two_step",
        "two_step_whole",
        "two_step_frac",
    ]
    window = tk.Tk()
    title = tk.Label(text="Worksheet Generator").grid(row=0, column=1)
    # title.pack()

    clicked = StringVar()
    clicked.set("two_step")
    num_problem_text = StringVar()
    num_problem_text.set("10")
    range_text = StringVar()
    range_text.set("100")

    drop_label = Label(window, text="Type of problems: ").grid(row=1, column=0)
    # drop_label.pack(side=LEFT)
    drop = OptionMenu(window, clicked, *options).grid(row=1, column=2)
    # drop.pack(side=RIGHT)
    Label(window, text="Number of problems (1, 5, 10, 100...): ").grid(row=2, column=0)
    Entry(window, textvariable=num_problem_text, bd=5).grid(row=2, column=2)

    Label(window, text="Max number for coefficients (1, 5, 10, 100...): ").grid(row=3, column=0)
    Entry(window, textvariable=range_text, bd=5).grid(row=3, column=2)

    button = Button(window, text="Generate Worksheet", command=generate_caller).grid(row=4, column=1)
    label = Label(window, text = "")
    # label.pack(side=LEFT)
    window.mainloop()

if __name__ == "__main__":
    main()