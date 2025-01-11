import tkinter as tk
from tkinter import scrolledtext
import markdown
import html2text
import tkinter.messagebox as messagebox
from tkinter.font import Font
from tkinter.filedialog import asksaveasfilename
import webbrowser
from tkinter import scrolledtext
import os
def markdown_html():
    markdownwindow = tk.Toplevel()
    markdownwindow.title("MDEDIT")
    # 设置窗口大小
    markdownwindow.geometry("800x600")

    # 创建一个 Frame 用于放置输入和输出组件
    frame = tk.Frame(markdownwindow)
    frame.pack(padx=20, pady=20)

    # Markdown 输入区域
    tk.Label(frame, text='Markdown code').grid(row=0, column=0, sticky='w', padx=10, pady=10)
    text_area = scrolledtext.ScrolledText(frame, width=60, height=15)
    text_area.grid(row=1, column=0, padx=10, pady=10)

    # HTML 输出区域
    tk.Label(frame, text='HTML code').grid(row=2, column=0, sticky='w', padx=10, pady=10)
    text_area1 = scrolledtext.ScrolledText(frame, width=60, height=15)
    text_area1.grid(row=3, column=0, padx=10, pady=10)

    def convert_markdown():
        markdown_text = text_area.get("1.0", "end-1c")
        try:
            html_text = markdown.markdown(markdown_text)
            text_area1.delete("1.0", "end")
            text_area1.insert("1.0", html_text)
        except Exception as e:
            messagebox.showerror("错误", f"转换为 HTML 时出现错误：{e}")

    def convert_back():
        html_text = text_area1.get("1.0", "end-1c")
        try:
            h = html2text.HTML2Text()
            markdown_text = h.handle(html_text)
            text_area.delete("1.0", "end")
            text_area.insert("1.0", markdown_text)
        except Exception as e:
            messagebox.showerror("错误", f"转换为 Markdown 时出现错误：{e}")

    def save():
        markdown_content = text_area.get("1.0", "end-1c").strip()
        html_content = text_area1.get("1.0", "end-1c").strip()
        if not markdown_content and not html_content:
            messagebox.showwarning("警告", "没有内容可保存。")
            return
        elif markdown_content and not html_content:
            filename = asksaveasfilename(defaultextension=".md", filetypes=[("Markdown 文件", "*.md")])
            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
        elif not markdown_content and html_content:
            filename = asksaveasfilename(defaultextension=".html", filetypes=[("HTML 文件", "*.html")])
            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html_content)
        else:
            save_window = tk.Toplevel(markdownwindow)
            save_window.title('Save')
            tk.Label(save_window, text='保存为').pack()
            selected_option = tk.StringVar()
            radio_button1 = tk.Radiobutton(save_window, text="HTML", variable=selected_option, value="HTML")
            radio_button1.pack()
            radio_button2 = tk.Radiobutton(save_window, text="MARKDOWN", variable=selected_option, value="MARKDOWN")
            radio_button2.pack()
            result_label = tk.Label(save_window, text="")
            result_label.pack()
            save_window.geometry('800x600')

            def save_selected():
                if selected_option.get() == "HTML":
                    filename = asksaveasfilename(defaultextension=".html", filetypes=[("HTML 文件", "*.html")])
                    if filename:
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(html_content)
                else:
                    filename = asksaveasfilename(defaultextension=".md", filetypes=[("Markdown 文件", "*.md")])
                    if filename:
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(markdown_content)
                save_window.destroy()

            tk.Button(save_window, text="确定保存", command=save_selected).pack()

    def preview():
        html_content = text_area1.get("1.0", "end-1c")
        if not html_content:
            markdown_text = text_area.get("1.0", "end-1c")
            try:
                html_content = markdown.markdown(markdown_text)
            except Exception as e:
                messagebox.showerror("错误", f"转换为 HTML 时出现错误：{e}")
                return
        temp_file = "temp.html"
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        webbrowser.open(temp_file)

    # 转换按钮
    custom_font = Font(family="Helvetica", size=12)
    convert_to_html_button = tk.Button(frame, text="转换为 HTML", command=convert_markdown, bg='lightblue')
    convert_to_html_button.grid(row=4, column=0, padx=10, pady=10)
    convert_back_button = tk.Button(frame, text="转换为 Markdown", command=convert_back, bg='lightgreen')
    convert_back_button.grid(row=4, column=1, padx=10, pady=10)
    convert_save_button = tk.Button(frame, text="保存", command=save, bg='lightpink', font=custom_font)
    convert_save_button.grid(row=4, column=2, padx=10, pady=10)
    preview = tk.Button(frame, text="预览", command=preview, bg='lightyellow')
    preview.grid(row=4, column=3, padx=10, pady=10)

    markdownwindow.mainloop()

   



