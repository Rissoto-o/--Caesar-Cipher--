import tkinter.constants
from tkinter import *

def entry():
    tocesar = tekst.get("1.0", tkinter.constants.END).strip()
    key_str = tekst2.get().strip()

    if not key_str.isdigit():
        wynik.config(text= "Error - this is not a number")
        return

    key = int(key_str)

    k = ceraz(tocesar, key)

    wynik.config(text= k)


def ceraz(text, key):
    code = ""
    for char in text:
        if 97 <= ord(char) <= 122:  # małe litery a-z
            shifted = ((ord(char) - 97 + key) % 26) + 97
            code += chr(shifted)
        elif 65 <= ord(char) <= 90:  # duże litery A-Z
            shifted = ((ord(char) - 65 + key) % 26) + 65
            code += chr(shifted)
        else:
            code += char
    return code


screen = Tk()
screen.geometry("500x500")
screen.title("--Caesar Cipher--")


screen.configure(bg="black")
screen.configure(background="black")

napis1 =   Label(screen, text="Caesar Cipher", fg="black" , font=("Arial", 50))
napis2=Label(screen, text="Write your text: ")

napis1.pack()
napis2.pack()

tekst = Text(screen , width=30, height=10)
tekst.configure(background="black", fg="white")
tekst.pack(padx=10, pady=10)

napis3= Label(screen, text="Number to key: ")
napis3.pack()

#key logger
tekst2 = Entry(screen, width=30, bg="black", fg="white")
tekst2.pack(padx=10, pady=10)

button = Button(screen, text="Enter", fg="red", bg="white", command=entry)
button.pack(padx=20, pady=20)

wynik = Label(screen, bg="black", fg="white", font="bold", foreground="yellow")
wynik.pack(padx=10, pady=10)




screen.mainloop()


