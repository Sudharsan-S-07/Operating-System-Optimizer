import tkinter as tk
from tkinter import ttk
import psutil

class BatteryPanel(ttk.Frame):

    def __init__(self,parent):

        super().__init__(parent)

        self.label=tk.Label(self,text="Battery Status",font=("Arial",18))
        self.label.pack(pady=20)

        self.battery=tk.Label(self,font=("Arial",28))
        self.battery.pack()

        self.update_battery()

    def update_battery(self):

        battery=psutil.sensors_battery()

        if battery:

            self.battery.config(text=f"{battery.percent}%")

        else:

            self.battery.config(text="No Battery")

        self.after(3000,self.update_battery)