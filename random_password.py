import tkinter as tk
import random
import string


def create_password_generator():
    """
    创建一个随机密码生成器的图形界面应用并启动它。

    返回主窗口对象，外部可通过该对象进行相关操作（比如设置窗口属性等）。
    """
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
    return root


class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("随机密码生成器")
        self.master.geometry("300x200")
        self.init_ui()

    def init_ui(self):
        # 密码长度标签
        length_label = tk.Label(self.master, text="请输入密码长度：")
        length_label.pack(padx=10, pady=5)

        # 密码长度输入框
        self.length_edit = tk.Entry(self.master, width=10)
        self.length_edit.pack(padx=10, pady=5)

        # 生成密码按钮
        generate_button = tk.Button(self.master, text="生成密码", command=self.generate_and_display_password)
        generate_button.pack(padx=10, pady=5)

        # 显示生成密码的标签
        self.password_label = tk.Label(self.master, text="生成的密码将显示在此处")
        self.password_label.pack(padx=10, pady=5)

    def generate_and_display_password(self):
        try:
            length = int(self.length_edit.get())
            if length <= 0:
                raise ValueError("密码长度必须大于0")
            password = generate_password(length)
            self.password_label.config(text=f"生成的密码：{password}")
        except ValueError as e:
            self.password_label.config(text=f"输入有误：{str(e)}")


def generate_password(length):
    """
    按照给定长度生成一个随机密码。

    参数:
    length: 密码的长度，为整数类型。

    返回值:
    password: 生成的随机密码字符串。
    """
    # 定义所有可能用于密码的字符
    characters = string.ascii_letters + string.digits + string.punctuation

    # 生成指定长度的随机密码
    password = ''.join(random.choice(characters) for i in range(length))

    return password
