from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
word = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


# -------------------------------Create Function for button------------------------------------------#


def know_words():
    data_dict.remove(word)
    learn_word = pd.DataFrame(data_dict)
    learn_word.to_csv("data/words_to_learn.csv", index=False)
    random_word_french()


def dont_now_words():
    random_word_french()


def random_word_french():
    global word, change_language
    window.after_cancel(change_language)
    word = random.choice(data_dict)
    canvas.itemconfig(language_lab, text="French", fill="black")
    canvas.itemconfig(translate_lab, text=word["French"], fill="black")
    canvas.itemconfig(images_card, image=picture_front)
    change_language = window.after(3000, func=change_front_card)


def change_front_card():
    canvas.itemconfig(images_card, image=picture_back)
    canvas.itemconfig(language_lab, text="English", fill="white")
    canvas.itemconfig(translate_lab, text=word["English"], fill="white")


# -------------------------------Crate Ui ---------------------------------------------------------#


window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

change_language = window.after(3000, func=change_front_card)

canvas = Canvas(width=800, height=600, )
picture_front = PhotoImage(file='images/card_front.png')
picture_back = PhotoImage(file='images/card_back.png')
images_card = canvas.create_image(400, 275, image=picture_front)
language_lab = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
translate_lab = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=2, row=2, columnspan=2)

# -------------------------------Create Button ---------------------------------------------------#
picture_right = PhotoImage(file="images/right.png")
button_right = Button(image=picture_right, highlightthickness=0, command=know_words)
button_right.grid(column=3, row=3)
picture_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=picture_wrong, highlightthickness=0, command=dont_now_words)
button_wrong.grid(column=2, row=3)

# -------------------------------Create text-----------------------------------------------------#


random_word_french()

window.mainloop()
