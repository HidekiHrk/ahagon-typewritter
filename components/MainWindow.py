import tkinter as tk
from typing import Tuple


class MainWindow(tk.Tk):
    def __init__(self, title: str, sizes: Tuple[int, int], icon: str = None):
        super().__init__()
        self.title(title)
        self.geometry("{}x{}".format(*sizes[:2]))
        self.resizable(width=False, height=False)
        if icon:
            self.iconphoto(True, tk.PhotoImage(file=icon))

    def close(self):
        self.destroy()

    def show(self):
        self.mainloop()
