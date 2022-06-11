BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIME =2000

from tkinter import *
import pandas, random
#Load csv data------------------------------------------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
dic_data= data.to_dict(orient="records")
word= None
#next_word-----------------------------------------------
def next_word():
    global word, timer
    window.after_cancel(timer)
    word = random.choice(dic_data)
    card.itemconfig(card_bg, image=card_front)
    card.itemconfig(title_text, text="French")
    card.itemconfig(word_text,text=word["French"])
    timer = window.after(FLIP_TIME, flip)

#flip_word-----------------------------------------------
def flip():
    card.itemconfig(card_bg,image=card_back)
    card.itemconfig(title_text, text="English")
    card.itemconfig(word_text, text=word["English"])

#Save_Progress/delete word-----------------------------------------------
def learnt():
    global data
    data = data.drop(data[data["French"] == word["French"]].index)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_word()
#UI
window = Tk()
window.title("Password Manager")
window.config(pady=20,padx=20,bg=BACKGROUND_COLOR)
timer= window.after(3000, flip)

#Card canvas
card = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_bg= card.create_image(400,263,image= card_front)
card.grid(row=1,column=1,columnspan=2)
#Title Label
title_text = card.create_text(400,150,text="title",font=("Ariel",40,"italic"))

#Word label
word_text = card.create_text(400,263,text="title",font=("Ariel",60,"bold"))



# Check Button
check_button_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_img,bd=0,bg=BACKGROUND_COLOR,command=learnt)
check_button.grid(row=2,column=1)


# Check Button
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img,bd=0,bg=BACKGROUND_COLOR,command=next_word)
wrong_button.grid(row=2,column=2)

next_word()



window.mainloop()
