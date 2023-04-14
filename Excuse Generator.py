# Made my Micah Ta
# PS im super cool

# Also just becuse I'm sharing this code dosn't meen I'm adding all these notes
from tkinter import *
import tkinter as tk
import random
import subprocess


def open_script_directory():
    subprocess.Popen(f'explorer "ExcusesAndMore"')
    subprocess.Popen(f'notepad "ExcusesAndMore\READ ME!!!.txt"')


def excuse(situation):
    quote = ""
    with open(f'ExcusesAndMore\{situation}.txt') as f:
        lines = f.readlines()

    while "" == quote.replace(" ", "").replace("\n", "") or len(quote) < 5:
        quote = random.choice(lines).strip()
    label.config(text = quote)



root = tk.Tk()
root.title('Excuse Generator')
root.geometry("815x100")
root.resizable(False, False)

label = tk.Label(root, text="What situation are you in", font=('Times', 16))
label.grid(row=0, column=0, columnspan=1000, pady=10)

start_button = tk.Button(root, text="You're late", font=('Times', 13), command=lambda: excuse("late"))
start_button.grid(row=1, column=0, padx=10)

start_button = tk.Button(root, text="Bad grade", font=('Times', 13), command=lambda: excuse("Grade"))
start_button.grid(row=1, column=1, padx=10)

start_button = tk.Button(root, text="You lost something", font=('Times', 13), command=lambda: excuse("lost"))
start_button.grid(row=1, column=2, padx=10)

start_button = tk.Button(root, text="Missed deadline", font=('Times', 13), command=lambda: excuse("dead"))
start_button.grid(row=1, column=3, padx=10)

start_button = tk.Button(root, text="Flaked on plans", font=('Times', 13), command=lambda: excuse("Flake"))
start_button.grid(row=1, column=4, padx=10)

start_button = tk.Button(root, text="Add/Edit Excuses", font=('Times', 13), command=open_script_directory)
start_button.grid(row=1, column=5, padx=10)

root.mainloop()