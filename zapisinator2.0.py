from tkinter import *


root = Tk() #tworzenie okna


root.title("zapisinator v2")
f = open("save.txt", "r")
e = Entry(root, width=120)
e.insert(0, f.read())
e.pack(ipady=6)


def klik():
	wpisanytekst = e.get()
	zapis = open("save.txt", "w")
	zapis.write(wpisanytekst)


	

button1 = Button(root, text="Save", command=klik, fg="blue", bg="green")
button1.pack()


root.mainloop()