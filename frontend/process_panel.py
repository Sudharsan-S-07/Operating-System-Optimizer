import tkinter as tk
from tkinter import ttk
import psutil

class ProcessPanel(ttk.Frame):

    def __init__(self,parent):

        super().__init__(parent)

        self.tree=ttk.Treeview(self)

        self.tree["columns"]=("PID","CPU")

        self.tree.heading("#0",text="Process")
        self.tree.heading("PID",text="PID")
        self.tree.heading("CPU",text="CPU")

        self.tree.pack(fill="both",expand=True)

        self.refresh()

    def refresh(self):

        for i in self.tree.get_children():
            self.tree.delete(i)

        for p in psutil.process_iter():

            try:

                self.tree.insert("",tk.END,text=p.name(),
                                 values=(p.pid,p.cpu_percent()))

            except:
                pass

        self.after(3000,self.refresh)