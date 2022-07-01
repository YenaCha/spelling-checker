from tkinter import *
import textblob
from textblob import TextBlob


def correctword():
    inputword = word1.get()
    tb = TextBlob(inputword)
    correctedword = tb.correct()
    word2.delete(0,END)
    word2.insert(10, correctedword)


def clearall():
    word1.delete(0,END)
    word2.delete(0,END)


tk = Tk()
tk.configure(background='lightgreen')
tk.geometry('400x250')
tk.title('Spelling Correction')
header = Label(tk, text='Welcome to the spelling correction app',
               font=('bold', 15)).place(x=25, y=30)
inputlabel = Label(tk, text='Input word :',
                   font=('bold', 15)).place(x=20, y=80)
word1 = Entry()
word1.place(x=200, y=85)
correctionlabel = Label(tk, text='Corrected word :',
                        font=('bold', 15)).place(x=20, y=150)
word2 = Entry()
word2.place(x=200, y=155)
correction = Button(tk, text='Correction', bg='blue',
                    fg='white', command=correctword).place(x=150, y=120)
clear = Button(tk, text='Clear All', bg='blue', fg='white',
               command=clearall).place(x=150, y=190)

tk.mainloop()
