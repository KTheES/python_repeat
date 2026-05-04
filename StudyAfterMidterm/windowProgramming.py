from tkinter import *


# window = Tk()

## 화면 구상 및 처리
# window.mainloop()



## 윈도창 조절
# window = Tk()
# window.title("2254667")
# window.geometry("400x100")
# window.resizable(width=FALSE, height=FALSE)

# window.mainloop()


## Label

# window = Tk()
# window.title("2254667")
# window.geometry("400x300")
# label1 = Label(window, text="파이썬 수업")
# label2 = Label(window, text="열심히", font=("궁서체",30),fg="blue")
# label3 = Label(window, text="공부 중입니다",bg = "magenta",width=20, height=5,anchor= SE)



# label1.pack()
# label2.pack()
# label3.pack()


# window.mainloop()  



## label에 글자 대신 이미지 넣기


###PhotoImage()는 GIF 파일만 지원, JPEG나 BMP 등은 지원하지 않음

# window = Tk()
# photo = PhotoImage(file="StudyAfterMidterm\gif\dog.gif")
# label1 = Label(window, image=photo)

# label1.pack()
# window.mainloop()



## 버튼


window = Tk()

button1 = Button(window,text="파이썬 종료",fg="red",command=quit)

button1.pack()


window.mainloop()



### 위젯 활용 - 함수형
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀여워요.")

window= Tk()


photo = PhotoImage(file="StudyAfterMidterm\gif\dog2.gif")
button1 = Button(window, image= photo, command=myFunc)

button1.pack()

window.mainloop()


### 체크버튼



from tkinter import messagebox
window = Tk()


def myFunc():
    if chk.get() == 0 :
        messagebox.showinfo("","체크버튼이 꺼졌어요")
    else:
        messagebox.showinfo("","체크버튼이 켜졌어요")
        
chk = IntVar()

cb1 = Checkbutton(window,text="클릭하세요",variable=chk,command=myFunc)

cb1.pack()

window.mainloop()



## 라디오버튼