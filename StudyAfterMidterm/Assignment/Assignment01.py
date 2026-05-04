from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀여워요.")

window = Tk()

window.title("2254667")
window.geometry("400x300")
photo = PhotoImage(file="StudyAfterMidterm\gif\dog.gif")

button1 = Button(window,text="종료",fg="blue",command=myFunc)
# button2 = Button(window,text="강아지 버튼",fg="blue",command=myFunc)

label1 = Label(window, text="파이썬 수업",bg = "green",width=10, height=50)
label2 = Label(window, image=photo)

button1.pack()
# button2.pack()
label1.pack(side = LEFT)
label2.pack(side = RIGHT)

window.mainloop()




# window = Tk()

# window.title("오늘의일기")
# window.geometry("400x400")
# photo = PhotoImage(file="StudyAfterMidterm\gif\icecream.gif")

# label1 = Label(window, text="오늘은 국제시장에갑니다", bg = "yellow")
# label2 = Label(window, image=photo)
# label3 = Label(window, text="좋았어!", bg = "skyblue", width=20, height=5)

# label1.pack()
# label2.pack()
# label3.pack()
# window.mainloop()