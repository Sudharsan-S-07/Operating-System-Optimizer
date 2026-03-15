import tkinter as tk
from tkinter import ttk

from cpu_panel import CPUPanel
from memory_panel import MemoryPanel
from process_panel import ProcessPanel
from disk_panel import DiskPanel
from battery_panel import BatteryPanel


class OSOptimizerApp:

    def __init__(self,root):

        root.title("Operating System Optimizer")
        root.geometry("900x600")

        notebook = ttk.Notebook(root)
        notebook.pack(fill="both",expand=True)

        notebook.add(CPUPanel(notebook),text="CPU")
        notebook.add(MemoryPanel(notebook),text="Memory")
        notebook.add(ProcessPanel(notebook),text="Processes")
        notebook.add(DiskPanel(notebook),text="Disk")
        notebook.add(BatteryPanel(notebook),text="Battery")


root=tk.Tk()

app=OSOptimizerApp(root)

root.mainloop()