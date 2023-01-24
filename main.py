import sys
from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def read_words():
    """Reads csv file with words to learn (if exists) or original word bank and returns a list of dictionaries"""
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        pass
    else:
        return data.to_dict(orient="records")

    try:
        data = pandas.read_csv("data/german_words.csv")
    except FileNotFoundError as e:
        messagebox.showerror(title="FileNotFound", message=f"Word bank file does not exist. Details:\n{e}")
        sys.exit()
    else:
        return data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image=card_front_img)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Niemiecki", fill="black")
    canvas.itemconfig(card_word, font=("Ariel", 60, "bold"))
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    flip_timer = window.after(1000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text="Polski", fill="white")
    print(len(current_card["Polish"]))
    if len(current_card["Polish"]) >= 20:
        canvas.itemconfig(card_word, font=("Ariel", 44, "bold"))
    canvas.itemconfig(card_word, text=current_card["Polish"], fill="white")


def word_is_known():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# --------------------IMPORT WORDS TO LEARN--------------------
to_learn = read_words()

# --------------------UI DESIGN--------------------
window = Tk()
window.minsize(width=900, height=726)
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

# Import pictures
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_icon = PhotoImage(file="images/right.png")
wrong_icon = PhotoImage(file="images/wrong.png")

# Create canvas with card and text
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 130, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", width=700, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Add buttons
wrong_button = Button(image=wrong_icon, command=next_card, highlightthickness=0, border=0,
                      activebackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_icon, command=word_is_known, highlightthickness=0, border=0,
                      activebackground=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)

# After UI set up, show first card
next_card()

window.mainloop()
