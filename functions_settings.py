import tkinter as tk
import os
import shutil
import time
import tkinter as tk
from tkinter import ttk

def update_log():
    update = tk.Toplevel()
    update.title("Update Log")
    update.geometry("400x400")
    update.resizable(False, False)
    Label = tk.Label(update, text="更新日志")
    Label.pack()
    Label2 = tk.Label(update, text="版本号：V1.0.1")
    Label2.pack()
    Label3 = tk.Label(update, text="更新内容：\n1. 优化功能：\n2. 修复BUG：")
    Label3.pack()
    update.mainloop()


def clear_cache():
    def clear():
        # 获取缓存目录，这里以系统临时目录为例
        cache_dir = os.path.join(os.getenv('TEMP'))
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(cache_dir):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        deleted_size = 0
        for dirpath, dirnames, filenames in os.walk(cache_dir):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    os.remove(fp)
                    deleted_size += os.path.getsize(fp)
                    progress['value'] = int((deleted_size / total_size) * 100)
                    clear1.update_idletasks()
                except Exception as e:
                    print(f"Error deleting {fp}: {e}")
            for d in dirnames:
                dp = os.path.join(dirpath, d)
                try:
                    shutil.rmtree(dp)
                    deleted_size += sum(os.path.getsize(os.path.join(dirpath, f)) for f in os.listdir(dp))
                    progress['value'] = int((deleted_size / total_size) * 100)
                    clear1.update_idletasks()
                except Exception as e:
                    print(f"Error deleting {dp}: {e}")
        progress['value'] = 100
        status_label.config(text="缓存清理完成")

    clear1 = tk.Toplevel()
    clear1.title("缓存清理工具")
    # 创建进度条
    progress = ttk.Progressbar(clear1, orient=tk.HORIZONTAL, length=300, mode='determinate')
    progress.pack(pady=20)
    # 创建开始按钮
    start_button = tk.Button(clear1, text="开始清理", command=clear)
    start_button.pack(pady=20)
    # 创建状态标签
    status_label = tk.Label(clear1, text="")
    status_label.pack(pady=20)
    clear1.mainloop()