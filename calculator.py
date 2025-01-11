import tkinter as tk
import math
def calculator():
    calculatorwindow = tk.Toplevel()
    calculatorwindow.title("计算器")
    calculatorwindow.geometry("400x400")

    frame = tk.Frame(calculatorwindow)
    frame.pack(padx=20, pady=20)

    input_value = tk.StringVar()
    output_value = tk.StringVar()

    # 创建输入框
    input_value.set('')
    tk.Entry(frame, textvariable=input_value, width=20).grid(row=0, columnspan=4, padx=10, pady=10)

    # 创建输出框
    output_value.set('')
    tk.Label(frame, textvariable=output_value, width=20).grid(row=5, columnspan=4, padx=10, pady=10)

    # 按钮列表
    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '+'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '*','C', '(', ')']
    
    ]

    # 创建按钮
    for row_index, row in enumerate(buttons):
        for col_index, button_text in enumerate(row):
            if button_text == '=':
                command = lambda: output_value.set('The resultis:'+str(eval(input_value.get())))
            elif button_text == 'C':
                command1 = lambda: input_value.set('')
                command2 = lambda: output_value.set('')
            else:
                command = lambda x=button_text: input_value.set(input_value.get() + x)
            
            tk.Button(frame, text=button_text, command=command).grid(row=row_index + 1, column=col_index, padx=10, pady=10)

    calculatorwindow.mainloop()

