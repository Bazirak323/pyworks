# 체크 버튼 만들기

# 목록 버튼 -checkbutton()
import tkinter as tk




# 체크 버튼 동작 구현 

# def click():
#     if ck_val.get() == True:
#         print("췍")

#     else:
#         print("체크가 되지 않았습니다.")    


# window = tk.Tk() # tk 클래스의 인스턴스 생성(window)

# window.title("목록 버튼")
# window.geometry("250x200")
# ck_val = tk.BooleanVar() # 트루나 펄스를 저장함(체크 했을 때와 그렇지 않을 때)
# ck_val.set(False) # 기본적으로 체크가 되있게 함


# tk.Checkbutton(text = "체크 버튼", font=("system", 13), variable = ck_val, command=click).pack()

# window.mainloop()



#목록 만들기

def click():
    result = "* 선택된 취미\n\n"
    result = ""
    for i in range(n):
        if ck_val[i].get():
            result += f"{hobby[i]}"
    lbl_result.config(text=result)        

window = tk.Tk() # tk 클래스의 인스턴스 생성(window)
window.title("목록 버튼")
window.geometry("250x200")


hobby = ["독서", "운동", "게임", "등산"]
ck_val = [None, None, None, None]
ck_btn = [None] * 4
n = len(hobby)

for i in range(n):
    ck_val[i] = tk.BooleanVar() # 트루나 펄스를 저장함(체크 했을 때와 그렇지 않을 때)
    ck_val[i].set(False) # 기본적으로 체크가 되있게 함
    ck_btn[i] = tk.Checkbutton(text = hobby[i], font = ("System", 13), variable=ck_val[i])
    ck_btn[i].place(x = 100, y = 20 + (30 * i))    


#확인 버튼
tk.Button(window, text="확인", command=click).place(x = 110, y = 160 )



#결과 표시 레이블
lbl_result = tk.Label(window, text = "", font = ("System", 13))
lbl_result.place(x = 40, y = 200)
window.mainloop()