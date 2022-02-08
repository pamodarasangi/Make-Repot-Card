from tkinter import *

UI = Tk()
UI.title('Welcome..')
UI.minsize(width=300, height=380)
UI.maxsize(width=600, height=800)
UI.configure(background="#97cf8a")
Label(UI, width=5, background="#97cf8a").grid(row=0, column=0)
Label(UI, text="Create Report Card", fg='black', font="cursive 18 bold", background="#97cf8a").grid(row=1, column=1)
Label(UI, background="#97cf8a").grid(row=2, column=0)
photo1 = PhotoImage(file="photo.png")
Label(UI, image=photo1).grid(row=3, column=1)

Label(UI, width=5, background="#97cf8a").grid(row=4, column=2)


def page():
    UI.destroy()
    import page2


B1 = Button(text='Make Report', bd='2', width=15, height=2, activebackground='#97cf8a', command=page)
B1.grid(row=5, column=1)
Label(UI, background="#97cf8a").grid(row=6, column=0)

UI.mainloop()
