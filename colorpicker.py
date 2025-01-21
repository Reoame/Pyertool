import tkinter as tk
from tkinter import colorchooser, messagebox


class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("颜色选择器")
        self.root.geometry("500x200")

        # 用于存储当前选择的颜色值
        self.hex_color = ""

        # 用于显示颜色值的标签
        self.color_value_label = tk.Label(self.root, text="色值: ")
        self.color_value_label.pack(pady=10)

        # 选择颜色按钮
        self.button = tk.Button(self.root, text="选择颜色", command=self.update_color_label)
        self.button.pack(pady=10)

        # 复制颜色值按钮
        self.button1 = tk.Button(self.root, text="复制hex色值", command=self.copy_color)
        self.button1.pack(pady=10)

    def update_color_label(self):
        """更新颜色值显示标签的内容"""
        color_result = colorchooser.askcolor()
        if color_result:
            self.hex_color = color_result[1]  # 获取十六进制颜色值
            self.color_value_label.config(text=f"色值: {self.hex_color}")

    def copy_color(self):
        """将当前颜色值复制到剪贴板"""
        if self.hex_color:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.hex_color)
            messagebox.showinfo("复制颜色", "颜色值已复制到剪贴板")
        else:
            messagebox.showwarning("复制颜色", "请先选择一个颜色")
