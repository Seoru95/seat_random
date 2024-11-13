import tkinter as tk
import random as rd    #tkinter, random 라이브러리 불러오기

screen = tk.Tk()
screen.title('자리 랜덤 배치 프로그램')   #기본 화면 설정
screen.geometry("1000x600")

board = tk.Label(screen, text = "칠판", font = ("Arial", 25), bg = "green", bd = 4, relief = "ridge")  #칠판 레이븧(방향때문에)
board.place(x = 425, y = 50, width = 150, height = 80)

blind = tk.Label(screen, text = "자리", font = ("Arial", 50), bg = "gray", bd = 2, relief = "raised")  #버튼 누르기 전에 자리 부분 가려둠(레이븧)
blind.place(x = 100, y = 200, width = 800, height = 220)

def ran_seat() :

    number = list(range(1, 25))   #자리 번호 리스트
    blind.destroy()     #blind 레이블 제거

    for i in range(24) :                   #자리 레이블 생성
        r = rd.choice(number)
        globals()["la_{}".format(i + 1)] = tk.Label(screen, text = r, font = ("Arial", 20), bg = "brown", bd = 2, relief = "groove")
        number.remove(r)

    #자리 레이블 위치
    la_1.place(x = 150, y = 200, width = 100, height = 40)
    la_2.place(x = 250, y = 200, width = 100, height = 40)
    la_3.place(x = 400, y = 200, width = 100, height = 40)
    la_4.place(x = 500, y = 200, width = 100, height = 40)                #첫째줄
    la_5.place(x = 650, y = 200, width = 100, height = 40)
    la_6.place(x = 750, y = 200, width = 100, height = 40)

    la_7.place(x = 150, y = 260, width = 100, height = 40)
    la_8.place(x = 250, y = 260, width = 100, height = 40)
    la_9.place(x = 400, y = 260, width = 100, height = 40)
    la_10.place(x = 500, y = 260, width = 100, height = 40)                #둘째줄
    la_11.place(x = 650, y = 260, width = 100, height = 40)
    la_12.place(x = 750, y = 260, width = 100, height = 40)

    la_13.place(x = 150, y = 320, width = 100, height = 40)
    la_14.place(x = 250, y = 320, width = 100, height = 40)
    la_15.place(x = 400, y = 320, width = 100, height = 40)
    la_16.place(x = 500, y = 320, width = 100, height = 40)                #셋째줄
    la_17.place(x = 650, y = 320, width = 100, height = 40)
    la_18.place(x = 750, y = 320, width = 100, height = 40)

    la_19.place(x = 150, y = 380, width = 100, height = 40)
    la_20.place(x = 250, y = 380, width = 100, height = 40)
    la_21.place(x = 400, y = 380, width = 100, height = 40)
    la_22.place(x = 500, y = 380, width = 100, height = 40)                #넷째줄
    la_23.place(x = 650, y = 380, width = 100, height = 40)
    la_24.place(x = 750, y = 380, width = 100, height = 40)

button = tk.Button(screen, text="자리 섞기", font = ("Arial", 25), bg = "white", command = ran_seat)     #버튼 생성
button.place(x = 425, y = 450, width = 150, height = 80)


screen.mainloop()

