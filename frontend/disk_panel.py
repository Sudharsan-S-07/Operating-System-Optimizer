import tkinter as tk
from tkinter import ttk
import psutil

class DiskPanel(ttk.Frame):

    def __init__(self,parent):

        super().__init__(parent)

        self.label=tk.Label(self,text="Disk Usage",font=("Arial",18))
        self.label.pack(pady=20)

        self.disk=tk.Label(self,font=("Arial",28))
        self.disk.pack()

        self.update_disk()

    def update_disk(self):

        usage=psutil.disk_usage("/")

        self.disk.config(text=f"{usage.percent}% used")

        self.after(2000,self.update_disk)