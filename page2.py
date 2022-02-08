from tkinter import *

pageUi = Tk()
pageUi.title('Create Report Card')
pageUi.configure(background="#A7DB42")  # #7fb05b
pageUi.minsize(width=450, height=600)
pageUi.maxsize(width=800, height=700)

Label(pageUi, bg="#A7DB42").grid(row=0, column=0)
Label(pageUi, text=" Report Card ", fg='black', font="cursive 19 bold", bg="#A7DB42") \
    .grid(row=1, column=1)

Label(pageUi, text=" Student Name", font="cursive 12", bg="#A7DB42").grid(row=1, column=2)
name = Entry(pageUi, width=25)
name.grid(row=2, column=2)

photo1 = PhotoImage(file="pic1.png")
pic = photo1.subsample(2, 2)
Label(pageUi, image=pic).grid(rowspan=6, column=2)

Label(pageUi, height=4, width=30, bg="#A7DB42").grid(row=2, column=0)
Label(pageUi, text="Buddhist", font="cursive 12", bg="#A7DB42").grid(row=2, column=0)
Entry1 = Entry(pageUi, width=20)
Entry1.grid(row=2, column=1, sticky=W)

Label(pageUi, text="Sinhala", font="cursive 12", bg="#A7DB42").grid(row=3, column=0)
Entry2 = Entry(pageUi, width=20)
Entry2.grid(row=3, column=1, sticky=W)

Label(pageUi, height=5, bg="#A7DB42").grid(row=4, column=0)
Label(pageUi, text="English", font="cursive 12", bg="#A7DB42").grid(row=4, column=0)
Entry3 = Entry(pageUi, width=20)
Entry3.grid(row=4, column=1, sticky=W)

Label(pageUi, text="Science", font="cursive 12", bg="#A7DB42").grid(row=5, column=0)
Entry4 = Entry(pageUi, width=20)
Entry4.grid(row=5, column=1, sticky=W)

Label(pageUi, height=5, bg="#A7DB42").grid(row=6, column=0)
Label(pageUi, text="History", font="cursive 12", bg="#A7DB42").grid(row=6, column=0)
Entry5 = Entry(pageUi, width=20)
Entry5.grid(row=6, column=1, sticky=W)

Label(pageUi, text="Mathmatics", font="cursive 12", bg="#A7DB42").grid(row=7, column=0)
Entry6 = Entry(pageUi, width=20)
Entry6.grid(row=7, column=1, sticky=W)

Label(pageUi, height=5, bg="#A7DB42").grid(row=8, column=0)
Label(pageUi, text="Group 1 Subjects", font="cursive 12", bg="#A7DB42").grid(row=8, column=0)
Entry7 = Entry(pageUi, width=20)
Entry7.grid(row=8, column=1, sticky=W)

Label(pageUi, text="Group 2 Subjects", font="cursive 12", bg="#A7DB42").grid(row=9, column=0)
Entry8 = Entry(pageUi, width=20)
Entry8.grid(row=9, column=1, sticky=W)

Label(pageUi, height=5, bg="#A7DB42").grid(row=10, column=0)
Label(pageUi, text="Group 3 Subjects", font="cursive 12", bg="#A7DB42").grid(row=10, column=0)
Entry9 = Entry(pageUi, width=20)
Entry9.grid(row=10, column=1, sticky=W)


def result():
    # pageUi.destroy()
    re = Tk()

    re.title('Report Card')
    re.minsize(width=480, height=500)

    Label(re).grid(row=0, column=0)
    Label(re, text=" Student Report Card ", font="cursive 18 bold").grid(row=1, column=1)
    Label(re).grid(row=2, column=0)
    Label(re, text=" Student Name :- ", font="cursive 12").grid(row=3, column=0)
    e_text = name.get()
    Label(re, text=e_text, font="cursive 12").grid(row=3, column=1)
    Label(re).grid(row=4, column=0, sticky=W)

    Label(re, text="Sub. Name", font="cursive 12 bold", fg="brown").grid(row=5, column=0)
    Label(re, text="Marks", font="cursive 12 bold", fg="brown").grid(row=5, column=1)
    Label(re, text="Grade", font="cursive 12 bold", fg="brown").grid(row=5, column=2)

    Label(re).grid(row=6, column=0)
    Label(re, text="Buddhist", font="cursive 12").grid(row=7, column=0)
    Sub1 = Entry1.get()
    Label(re, text=Sub1, font="cursive 12").grid(row=7, column=1)
    if int(Sub1) >= 75:
        R = "A"
    elif int(Sub1) >= 65:
        R = "B"
    elif int(Sub1) >= 55:
        R = "C"
    elif int(Sub1) >= 35:
        R = "S"
    else:
        R = "F"
    Label(re, text=R, font="cursive 12").grid(row=7, column=2)

    Label(re, text="Sinhala", font="cursive 12").grid(row=8, column=0)
    Sub2 = Entry2.get()
    Label(re, text=Sub2, font="cursive 12").grid(row=8, column=1)
    if int(Sub2) >= 75:
        R = "A"
    elif int(Sub2) >= 65:
        R = "B"
    elif int(Sub2) >= 55:
        R = "C"
    elif int(Sub2) >= 35:
        R = "S"
    else:
        R = "F"
    Label(re, text=R, font="cursive 12").grid(row=8, column=2)

    Label(re, text="English", font="cursive 12").grid(row=9, column=0)
    Sub3 = Entry3.get()
    Label(re, text=Sub3, font="cursive 12").grid(row=9, column=1)
    if int(Sub3) >= 75:
        R = "A"
    elif int(Sub3) >= 65:
        R = "B"
    elif int(Sub3) >= 55:
        R = "C"
    elif int(Sub3) >= 35:
        R = "S"
    else:
        R = "F"
    Label(re, text=R, font="cursive 12").grid(row=9, column=2)

    Label(re, text="Science", font="cursive 12").grid(row=10, column=0)
    Sub4 = Entry4.get()
    Label(re, text=Sub4, font="cursive 12").grid(row=10, column=1)
    if int(Sub4) >= 75:
        R = "A"
    elif int(Sub4) >= 65:
        R = "B"
    elif int(Sub4) >= 55:
        R = "C"
    elif int(Sub4) >= 35:
        R = "S"
    else:
        R = "F"
    Label(re, text=R, font="cursive 12").grid(row=10, column=2)

    Label(re, text="History", font="cursive 12").grid(row=11, column=0)
    Sub5 = Entry5.get()
    Label(re, text=Sub5, font="cursive 12").grid(row=11, column=1)
    if int(Sub5) >= 75:
        R = "A"
    elif int(Sub5) >= 65:
        R = "B"
    elif int(Sub5) >= 55:
        R = "C"
    elif int(Sub5) >= 35:
        R = "S"
    else:
        R = "F"
    Label(re, text=R, font="cursive 12").grid(row=11, column=2)

    Label(re, text="Mathmatics", font="cursive 12").grid(row=12, column=0)
    Sub6 = Entry6.get()
    Label(re, text=Sub6, font="cursive 12").grid(row=12, column=1)
    if int(Sub6) >= 75:
        R = "A"
    elif int(Sub6) >= 65:
        R = "B"
    elif int(Sub6) >= 55:
        R = "C"
    elif int(Sub6) >= 35:
        R = "S"
    else:
        R = "F"
    Label(re, text=R, font="cursive 12").grid(row=12, column=2)

    Label(re, text="Group 1 Subjects", font="cursive 12").grid(row=13, column=0)
    Sub7 = Entry7.get()
    Label(re, text=Sub7, font="cursive 12").grid(row=13, column=1)
    if int(Sub7) >= 75:
        R = "A"
    elif int(Sub7) >= 65:
        R = "B"
    elif int(Sub7) >= 55:
        R = "C"
    elif int(Sub7) >= 35:
        R = "S"
    else:
        R = "F"
    Label(re, text=R, font="cursive 12").grid(row=13, column=2)

    Label(re, text="Group 2 Subjects", font="cursive 12").grid(row=14, column=0)
    Sub8 = Entry8.get()
    Label(re, text=Sub8, font="cursive 12").grid(row=14, column=1)
    if int(Sub8) >= 75:
        R = "A"
    elif int(Sub8) >= 65:
        R = "B"
    elif int(Sub8) >= 55:
        R = "C"
    elif int(Sub8) >= 35:
        R = "S"
    else:
        R = "F"
    Label(re, text=R, font="cursive 12").grid(row=14, column=2)

    Label(re, text="Group 3 Subjects", font="cursive 12").grid(row=15, column=0)
    Sub9 = Entry9.get()
    Label(re, text=Sub9, font="cursive 12").grid(row=15, column=1)
    if int(Sub9) >= 75:
        R = "A"
    elif int(Sub9) >= 65:
        R = "B"
    elif int(Sub9) >= 55:
        R = "C"
    elif int(Sub9) >= 35:
        R = "S"
    else:
        R = "F"
    Label(re, text=R, font="cursive 12").grid(row=15, column=2)

    Label(re).grid(row=16, column=0)
    Label(re, text=" Total :- ", font="cursive 12").grid(row=17, column=0)
    T = int(Sub1) + int(Sub2) + int(Sub3) + int(Sub4) + int(Sub5) + int(Sub6) + int(Sub7) + int(Sub8)
    Label(re, text=T, font="cursive 12").grid(row=17, column=1)

    Label(re, text=" Average :- ", font="cursive 12").grid(row=18, column=0)
    Avg = int(T)/8
    Label(re, text=Avg, font="cursive 12").grid(row=18, column=1)

    def close():
        re.destroy()

    Label(re, width=15).grid(row=19, column=0)
    B2 = Button(re, text=" Print ", bd='3', bg='white', fg='black', width=8, height=2, command=close)
    B2.grid(row=20, column=2)
    Label(re).grid(row=21, column=0)

    name.delete(0, END)
    Entry1.delete(0, END)
    Entry2.delete(0, END)
    Entry3.delete(0, END)
    Entry4.delete(0, END)
    Entry5.delete(0, END)
    Entry6.delete(0, END)
    Entry7.delete(0, END)
    Entry8.delete(0, END)
    Entry9.delete(0, END)
    re.mainloop()


B1 = Button(text=' Report ', bd='2', bg='white', fg='black', width=10, height=2, command=result)
B1.grid(row=11, column=2)
Label(pageUi, bg="#A7DB42").grid(row=12, column=0)

pageUi.mainloop()
