import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def convert_to_exe_gui():
    def convert_to_exe():
        input_source = input_type.get()
        package_scope = package_option.get()  # 获取打包范围选项
        if input_source == "file":
            python_file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
            if not python_file_path:
                return
            file_name_without_extension = os.path.splitext(os.path.basename(python_file_path))[0]
            try:
                if package_scope == "single":  # 仅打包单个文件
                    command = f"pyinstaller -F {python_file_path}"
                    subprocess.run(command, shell=True, check=True)
                    if zip_option.get():
                        zip_file_name = f"{file_name_without_extension}.zip"
                        zip_command = f"zip -r {zip_file_name} dist"
                        subprocess.run(zip_command, shell=True, check=True)
                        messagebox.showinfo("Success", f"{file_name_without_extension}.exe 文件生成成功，可在 dist 目录下找到，并且已压缩为 {zip_file_name}。")
                    else:
                        messagebox.showinfo("Success", f"{file_name_without_extension}.exe 文件生成成功，可在 dist 目录下找到。")
                elif package_scope == "project":  # 打包整个项目
                    project_dir = os.path.dirname(python_file_path)
                    command = f"pyinstaller {python_file_path}"  # 不使用 -F 参数，保留项目结构相关文件
                    subprocess.run(command, shell=True, check=True)
                    if zip_option.get():
                        zip_file_name = f"{file_name_without_extension}_project.zip"
                        zip_command = f"zip -r {zip_file_name} {project_dir}"
                        subprocess.run(zip_command, shell=True, check=True)
                        messagebox.showinfo("Success", f"项目打包成功，生成的文件已压缩为 {zip_file_name}，包含整个项目相关文件。")
                    else:
                        messagebox.showinfo("Success", f"项目打包成功，包含整个项目相关文件，可查看生成的相关文件。")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"转换过程出现错误：{e}")
        elif input_type == "text":
            python_code = code_text.get("1.0", tk.END)
            if not python_code.strip():
                messagebox.showerror("Error", "请输入有效的Python代码内容")
                return
            # 创建临时文件保存输入的代码
            temp_file_path = "Python_app.py"
            with open(temp_file_path, "w", encoding="utf-8") as f:
                f.write(python_code)
            try:
                if package_scope == "single":  # 仅打包单个临时文件
                    command = f"pyinstaller -F {temp_file_path}"
                    subprocess.run(command, shell=True, check=True)
                    os.remove(temp_file_path)
                    if zip_option.get():
                        zip_file_name = "temp_app.zip"
                        zip_command = f"zip -r {zip_file_name} dist"
                        subprocess.run(zip_command, shell=True, check=True)
                        messagebox.showinfo("Success", "输入的代码转换生成.exe文件成功，可在 dist 目录下找到，并且已压缩为 {zip_file_name}。")
                    else:
                        messagebox.showinfo("Success", "输入的代码转换生成.exe文件成功，可在 dist 目录下找到。")
                elif package_scope == "project":  # 模拟打包整个项目（以临时文件所在目录为例）
                    project_dir = os.path.dirname(temp_file_path)
                    command = f"pyinstaller {temp_file_path}"  # 不使用 -F 参数，保留项目结构相关文件
                    subprocess.run(command, shell=True, check=True)
                    os.remove(temp_file_path)
                    if zip_option.get():
                        zip_file_name = "temp_project.zip"
                        zip_command = f"zip -r {zip_file_name} {project_dir}"
                        subprocess.run(zip_command, shell=True, check=True)
                        messagebox.showinfo("Success", "模拟项目打包成功，生成的文件已压缩为 {zip_file_name}，包含整个项目相关文件。")
                    else:
                        messagebox.showinfo("Success", "模拟项目打包成功，包含整个项目相关文件，可查看生成的相关文件。")
            except subprocess.CalledProcessError as e:
                os.remove(temp_file_path)
                messagebox.showerror("Error", f"转换过程出现错误：{e}")

    root1 = tk.Toplevel()
    root1.title("Python to EXE Converter")
    root1.geometry("400x400")
    # 用于选择输入来源（文件或者文本输入）的变量
    input_type = tk.StringVar(value="file")
    # 新增：用于选择打包范围的变量（单个文件或整个项目）
    package_option = tk.StringVar(value="single")
    # 用于选择是否压缩的变量
    zip_option = tk.BooleanVar(value=False)

    # 单选按钮，用于选择是通过文件还是文本输入代码
    file_radio = tk.Radiobutton(root1, text="选择已有Python文件", variable=input_type, value="file")
    file_radio.pack()
    text_radio = tk.Radiobutton(root1, text="手动输入Python代码", variable=input_type, value="text")
    text_radio.pack()

    # 新增：单选按钮，用于选择打包范围（单个文件或整个项目）
    single_radio = tk.Radiobutton(root1, text="仅打包单个文件", variable=package_option, value="single")
    single_radio.pack()
    project_radio = tk.Radiobutton(root1, text="打包整个项目", variable=package_option, value="project")
    project_radio.pack()

    # 文本框，用于输入Python代码（初始隐藏，当选择手动输入时显示）
    code_text = tk.Text(root1, height=10, width=40)
    code_text.pack_forget()

    # 根据选择显示或隐藏文本框的函数
    def show_hide_text_box():
        if input_type.get() == "text":
            code_text.pack()
        else:
            code_text.pack_forget()

    text_radio.config(command=show_hide_text_box)
    file_radio.config(command=show_hide_text_box)

    convert_button = tk.Button(root1, text="转换为EXE", command=convert_to_exe)
    convert_button.pack(pady=20)

    root1.mainloop()


if __name__ == "__main__":
    convert_to_exe_gui()