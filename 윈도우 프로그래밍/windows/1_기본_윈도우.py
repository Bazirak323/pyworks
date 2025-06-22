from tkinter import *

def click():
    print("안녕 파이썬")


root = Tk()
root.title("첫 윈도우")
root.geometry("250x50")


Label(root, text = "Hello Python").pack()
Button(root, text="확인", command=click).pack()

click()


root.mainloop()