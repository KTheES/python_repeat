from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀여워요.")

window = Tk()

window.title("2254667")
window.geometry("400x300")
photo = PhotoImage(file="StudyAfterMidterm\gif\dog.gif")

button1 = Button(window,text="종료",fg="blue",command=quit)
# button2 = Button(window,text="강아지 버튼",fg="blue",command=myFunc)

label1 = Label(window, text="파이썬 수업",bg = "green",width=10, height=5)
label2 = Label(window, image=photo)

button1.pack()
# button2.pack()
## 수평 정렬 방법. 리스트-for 문으로도 가능함.
label1.pack(side = LEFT)
label2.pack(side = RIGHT)

window.mainloop()

## 수직 정렬 방법. 
# label2.pack(side = TOP)
# label2.pack(side = BOTTOM)
# 폭 조정 - fill =x ->  윈도창 폭에 맞춤
# label2.pack(side = TOP, fill = X)
# 위젯 사이 여백 조절
# label2.pack(side = TOP, fill = X, padx=10, pady=10)
# 위젯 내부 여백 조절
# label2.pack(side = TOP, fill = X, ipadx=10, ipady=10)
## 위젯 내부와 외부에 모두 여백
# btn-pack(side =TOP, fill = X,  ipadx=10, ipady=10,padx=10,pady=10)
## 고정 위치에 배치 : pack() 대신 place() 함수 사용





# window = Tk()
# window.title("2254667")
# window.geometry("400x300")

# def myFunc():
#     if var.get() ==1:
#         label1.configure(text="1학년")
#     elif var.get() == 2:
#         label1.configure(text = "2학년")
#     elif var.get() == 3:
#         label1.configure(text = "3학년")
#     else :
#         label1.configure(text = "4학년")
        
# var = IntVar()
# rb1 = Radiobutton(window,text="1학년",variable=var,value=1,command=myFunc)
# rb2 = Radiobutton(window,text="2학년",variable=var,value=2,command=myFunc)
# rb3 = Radiobutton(window,text="3학년",variable=var,value=3,command=myFunc)
# rb4 = Radiobutton(window,text="4학년",variable=var,value=4,command=myFunc)

# label1 = Label(window,text="학년: ",fg = "red")

# rb1.pack()
# rb2.pack()
# rb3.pack()
# rb4.pack()
# label1.pack()

# window.mainloop()




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


#