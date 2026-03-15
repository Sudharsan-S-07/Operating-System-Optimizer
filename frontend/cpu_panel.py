import tkinter as tk
from tkinter import ttk
import psutil

class CPUPanel(ttk.Frame):

    def __init__(self,parent):

        super().__init__(parent)

        self.label=tk.Label(self,text="CPU Usage",font=("Arial",18))
        self.label.pack(pady=20)

        self.usage=tk.Label(self,font=("Arial",30))
        self.usage.pack()

        self.update_cpu()

    def update_cpu(self):

        cpu=psutil.cpu_percent()

        self.usage.config(text=f"{cpu}%")

        self.after(1000,self.update_cpu)