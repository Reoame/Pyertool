import tkinter as tk


def pyeditor():
    print("Python Editor started...")
    pyeditor_window = tk.Toplevel()
    pyeditor_window.title("Python Editor")
    pyeditor_window.geometry("800x600")
    pyeditor_window.resizable(0, 0)
    
    pyeditor_window.mainloop()