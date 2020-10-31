# 계산기 프로그램
from tkinter import *

# ----------------------------------------------
# 계산 기능 구현을 위한 함수부 
# ----------------------------------------------

## 숫자 및 연산자 입력  
def input_value(v):
    display.insert(0,v)


## 계산 수행
def calculate():
    value = Entry.get(display)
    if value != '':
        result = eval(value)
        clear_entry()
        display.insert(0, result)

### Enter키 발생 시 calculate() 호출
def calculate_enter(event):
    calculate()


## clear 기능 
def clear_entry():
    display.delete(0,'end')


# ----------------------------------------------
# 계산기 UI 구현
# ----------------------------------------------

## 프로그램 창 
window = Tk()
window.title("My Calculator - 15615013 김준혁")


## 입력 및 출력부
display = Entry(window, width=55, bg="yellow", justify='right')
display.grid(row=0, column=0, columnspan=5)


## 계산기 버튼부
btn_width = 10
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

### 숫자 버튼 추가
Button(window, text=num_list[0], width=btn_width, command=lambda:input_value(num_list[0])).grid(row=4, column=0)
Button(window, text=num_list[1], width=btn_width, command=lambda:input_value(num_list[1])).grid(row=3, column=0)
Button(window, text=num_list[2], width=btn_width, command=lambda:input_value(num_list[2])).grid(row=3, column=1)
Button(window, text=num_list[3], width=btn_width, command=lambda:input_value(num_list[3])).grid(row=3, column=2)
Button(window, text=num_list[4], width=btn_width, command=lambda:input_value(num_list[4])).grid(row=2, column=0)
Button(window, text=num_list[5], width=btn_width, command=lambda:input_value(num_list[5])).grid(row=2, column=1)
Button(window, text=num_list[6], width=btn_width, command=lambda:input_value(num_list[6])).grid(row=2, column=2)
Button(window, text=num_list[7], width=btn_width, command=lambda:input_value(num_list[7])).grid(row=1, column=0)
Button(window, text=num_list[8], width=btn_width, command=lambda:input_value(num_list[8])).grid(row=1, column=1)
Button(window, text=num_list[9], width=btn_width, command=lambda:input_value(num_list[9])).grid(row=1, column=2)

### 연산자 버튼 추가
op_list = ['+', '-', '*', '/']
Button(window, text=op_list[0], width=btn_width, command=lambda:input_value(op_list[0])).grid(row=4, column=3)
Button(window, text=op_list[1], width=btn_width, command=lambda:input_value(op_list[1])).grid(row=3, column=3)
Button(window, text=op_list[2], width=btn_width, command=lambda:input_value(op_list[2])).grid(row=2, column=3)
Button(window, text=op_list[3], width=btn_width, command=lambda:input_value(op_list[3])).grid(row=1, column=3)

### 기타 버튼(초기화, 소수점, 계산요청) 추가
Button(window, text='C', width=btn_width, command=clear_entry).grid(row=1, column=4)
Button(window, text='.', width=btn_width, command=lambda:input_value('.')).grid(row=4, column=1)
Button(window, text='=', width=btn_width, command=calculate).grid(row=4, column=2)

### Enter키 누르면 계산 수행
window.bind('<Return>', calculate_enter)


# 이벤트 메시지 루프로서 키보드/마우스 같은 다양한 이벤트로부터 오는 메시지를 받고 전달하는 역할 수행.
window.mainloop()