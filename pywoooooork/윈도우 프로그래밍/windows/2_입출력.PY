#입력과 출력

from tkinter import *

# def click():
#     text = Entry.get()
#     output.delete(0, tkE
#                   )



# root = tk.Tk()

# root.title("입력과 출력")
# root.geometry("250x200+200+300")
# root.option_add("*font", "system 13")

# tk.Label(root, text = "이름: ",height = 3, font = ("system", 12)).grid(row = 0, column = 0)
# Entry  = tk.Entry(root).grid(row = 0, column = 1)
# Entry.grid(row = 0, column = 1)



# tk.Button(root, text = "확인").grid(row = 1, column= 2)
# tk.Label(root, text = "").grid(row = 2, column = 0)
# tk.Text(root, width = 20, height = 3).grid(row = 2, columnspan = 2)
# output = tk.Text(root, width=20, height=3)
# output.grid(row = 3, columnspan= 2)


# root.mainloop()

dic = {
    "이진수 : 그거"
    "코딩 : 이거"
}

def submit():
    try:
        word = entry.get()
        definition = dic[word]
        output.delete(0.0, END)
        output.insert(END, definition)
    except KeyError:
        output.delete(0.0, END)    
        output.insert(END, "단어를 찾을 수 없습니다.")    



root = Tk()
root.title("컴퓨터 용어 사전")

Label(root, text = "검색할 단어를 입력하세요").grid(row = 0, column = 0, sticky=W)
entry = Entry(root, width=20, bg = "skyblue")
entry.grid(row = 1, column = 0, sticky=W)



Button(root, text = "제출").grid(row = 2, column = 0, sticky=W)
Label(root, text = "정의").grid(row = 3, column = 0, sticky=W)
output = Text(root, width = 60, height = 10, bg = "yellow green")
output.grid(row = 4, column= 0, sticky= W)

submit()

root.mainloop()













