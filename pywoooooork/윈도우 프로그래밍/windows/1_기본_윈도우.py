from tkinter import *




# def click():
#     pass

# root = Tk()
# root.title("첫 윈도우")
# root.geometry("250x80+200+100")


# Label(root, text = "Hello Python").pack()
# Button(root, text="확인", command=click).pack()






# root.mainloop()


#레이아웃(배치) - grid() 함수

window = Tk()
window.title('배치-grid')
window.geometry("300x300")
#grid(행, 열)
Label(window, text="오늘도 좋은 하루 되세요", font=("돋움", 13)).grid(row=0,column=0)
Button(window, text="동", width=5, height=2).grid(row = 1, column = 0, sticky=E)
Button(window, text="서", width=5, height=2).grid(row = 1, column = 0, sticky=W)
Button(window, text="북", width=5, height=2).grid(row = 2, column = 0, sticky=N)
Button(window, text="남", width=5, height=2).grid(row = 3, column = 0, sticky=S)




window.mainloop()