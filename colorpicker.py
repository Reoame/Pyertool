import tkinter as tk
from tkinter import colorchooser


def get_color():
    color = colorchooser.askcolor()
    return color


def get_color1():
    root3 = tk.Toplevel()
    root3.geometry("500x200")

    # 用于显示颜色值的标签，初始文本先设为空
    color_value_label = tk.Label(root3, text="")
    color_value_label.pack(pady=10)

    def update_color_label():
        """
        这个内部函数用于更新颜色值显示标签的内容，
        每次点击按钮选择颜色后会调用它来更新界面显示。
        """
        color_result = get_color()
        if color_result:
            hex_color = color_result[1]  # 获取十六进制颜色值
            color_value_label.config(text=f"色值: {hex_color}")

    button = tk.Button(root3, text="Choose Color", command=update_color_label)
    button.pack(pady=10)


