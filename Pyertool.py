import tkinter as tk
import webbrowser
from tkinter import scrolledtext
import requests
import script
import calculator
import functions
from random_password import create_password_generator
print("Pyertool 0.1")
print("Please don‘t close this window")
print("\033[32mStarted successfully\033[0m")

roota = tk.Tk()
roota.geometry("800x600")
roota.title("Pyertool")

from tkinter import scrolledtext, filedialog, messagebox, simpledialog
def function():
    functions.markdown_html()

def code():
    root = tk.Toplevel()

    root.title("网页源码获取器")
    # 创建输入框用于输入网址
    url_label = tk.Label(root, text="输入网址:")
    url_label.pack(padx=10, pady=5)
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(padx=10, pady=5)

    def get_page_source():
        url = url_entry.get()
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
            page_source = response.text
            # 显示网页源码
            code_text.delete('1.0', tk.END)
            code_text.insert('1.0', page_source)
        except requests.RequestException as e:
            # 显示错误信息
            code_text.delete('1.0', tk.END)
            code_text.insert('1.0', f"Error: {e}")
    # 创建按钮用于获取网页源码
    fetch_button = tk.Button(root, text="获取源码", command=get_page_source)
    fetch_button.pack(padx=10, pady=5)



    # 创建文本框用于显示网页源码
    code_text = scrolledtext.ScrolledText(root, width=80, height=20)
    code_text.pack(padx=10, pady=10)

    # 运行主循环
class TextEditor:
    def __init__(self, new_window):
        self.new_window = new_window
        self.new_window.title("文本编辑器")

        # 创建一个滚动文本框
        self.text_area = scrolledtext.ScrolledText(self.new_window, wrap='word')
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)

        # 创建菜单栏
        self.menu_bar = tk.Menu(self.new_window)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="新建", command=self.new_file)
        self.file_menu.add_command(label="打开", command=self.open_file)
        self.file_menu.add_command(label="保存", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", command=self.quit_editor)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="查找", command=self.find_text)
        self.edit_menu.add_command(label="替换", command=self.replace_text)
        self.menu_bar.add_cascade(label="编辑", menu=self.edit_menu)

        self.new_window.config(menu=self.menu_bar)

    def new_file(self):
        # 新建文件
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        # 打开文件
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                              filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        # 保存文件
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

    def quit_editor(self):
        # 退出编辑器
        if messagebox.askokcancel("退出", "确定要退出吗？"):
            self.new_window.destroy()

    def find_text(self):
        # 查找文本
        find_text = simpledialog.askstring("查找", "输入要查找的文本：")
        if find_text:
            self.text_area.tag_remove('found', '1.0', tk.END)
            start_index = self.text_area.search(find_text, '1.0', nocase=True, stopindex=tk.END)
            while start_index:
                end_index = f"{start_index}+{len(find_text)}c"
                self.text_area.tag_add('found', start_index, end_index)
                start_index = self.text_area.search(find_text, end_index, nocase=True, stopindex=tk.END)
            self.text_area.tag_config('found', background='yellow')

    def replace_text(self):
        # 替换文本
        find_text = simpledialog.askstring("替换", "输入要查找的文本：")
        if find_text:
            replace_text = simpledialog.askstring("替换", "输入替换后的文本：")
            if replace_text:
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert('1.0', self.text_area.get('1.0', tk.END).replace(find_text, replace_text))
def open_github():
    webbrowser.open("https://github.com/Reoame/My_invention")
def function1():
    calculator.calculator()
def function2():
    password = functions.Random_password()

def fun2():
    rabdom_password = create_password_generator()
def f2():
    script.convert_to_exe_gui()

def color():
    import colorpicker
    colorpicker.get_color1()
tk.Label(roota,text='代码工具').place(x=0,y=0)
tk.Button(roota,text="Markdown工具",command=function,bg='lightblue').place(x=0,y=20)
tk.Button(roota,text="获取网页源码",bg='lightblue',command=code).place(x=120,y=20)
tk.Button(roota, text="文本编辑器",bg='lightblue', command=lambda: TextEditor(tk.Toplevel())).place(x=240,y=20)
tk.Button(roota, text="python代码转exe",bg='lightblue', command=f2).place(x=240,y=20)
tk.Button(roota, text="github",bg='lightblue', command=open_github).place(x=360,y=20)
tk.Label(roota,text='计算工具').place(x=0,y=100)
tk.Button(roota,text='计算器',command=function1,bg='lightgreen').place(x=0,y=160)
tk.Button(roota,text='随机密码',command=fun2,bg='lightgreen').place(x=100,y=160)
tk.Label(roota,text='其他工具').place(x=0,y=200)
tk.Button(roota,text='取色器',command=color,bg='lightyellow').place(x=0,y=260)

roota.mainloop()