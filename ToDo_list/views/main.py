import tkinter as tk
from ToDo_list.views.resources import BACKGROUND, ICON

ventana = tk.Tk()
ventana.configure(background=BACKGROUND)
ventana.state("zoomed")
ventana.iconbitmap(ICON)
ventana.title("Actividades")

