#단위 변환기 - MB -> KB 로 변환

from tkinter import *

def convert():
    try :
        byte_mb = int(ent_mb.get())
        out_kb.delete(0.0, END)
        byte_kb = byte_mb * 1024
        out_kb.insert(END, byte_kb)
    except ValueError:
        out_kb.delete(0.0, END)
        out_kb.insert("Error")

window = Tk()

window.title("단위 변환기")
window.geometry("250x100+200+200")
frame = Frame(window) # 프레임 생성

frame.pack() #가운데 배치

Label(frame, text = "byte MB").grid(row = 0, column=0)

entry = Entry(frame, width=15)

entry.grid(row=0, column=1)




Label(frame, text = "byte KB").grid(row = 1, column=0)
ent_mb = Text(frame, width = 15, height = 1)
ent_mb.grid(row=1, column=1)
out_kb = Text(frame, width=15, height = 1)
out_kb.grid(row = 1, column = 1)

Button(frame, text = "변환", command=convert).grid(row = 2, columnspan=2)
































window.mainloop()











































































