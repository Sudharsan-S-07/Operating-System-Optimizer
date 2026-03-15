import tkinter as tk
from tkinter import ttk
import psutil

class MemoryPanel(ttk.Frame):

    def __init__(self,parent):

        super().__init__(parent)

        self.label=tk.Label(self,text="Memory Usage",font=("Arial",18))
        self.label.pack(pady=20)

        self.mem=tk.Label(self,font=("Arial",28))
        self.mem.pack()

        self.update_memory()

    def update_memory(self):

        memory=psutil.virtual_memory()

        self.mem.config(text=f"{memory.percent}%")

        self.after(1000,self.update_memory)
        