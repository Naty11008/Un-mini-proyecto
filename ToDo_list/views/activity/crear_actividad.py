import tkinter as tk
from ToDo_list.db.operations import crear_actividad
from tkinter import messagebox as mb  
from ToDo_list.views.resources import BACKGROUND, SECONDARY, TEXT, TITLES, PRIMARY 

def mostrar_crear_actividades(w:tk.Tk):
    from ToDo_list.views.activity.home import mostrar_home_actividades
    for widget in w.winfo_children():
        widget.destroy()
    w.columnconfigure(0, weight=1)
    w.columnconfigure(1)
    w.columnconfigure(2, weight=1)

    for i in range(7):
        w.rowconfigure(i, pad=20)


    tk.Label(w, text="Formulario para dar de alta actividades", fg=PRIMARY, font=TITLES, bg=BACKGROUND).grid(
    column=0, row=0, columnspan=3, sticky="n")

    tk.Label(w, text="Titulo:", fg=SECONDARY, bg=BACKGROUND, font=TEXT).grid(column=0, row=1, sticky="e")
    tk.Label(w, text="Descripcion:", fg=SECONDARY, bg=BACKGROUND, font=TEXT).grid(column=0, row=2, sticky="e")

    entry_title = tk.Entry(w, font=TEXT, relief="flat")
    entry_description = tk.Entry(w, font=TEXT, relief="flat")

    entry_title.grid(column=1, row=1, padx=20)
    entry_description.grid(column=1, row=2, padx=20)

    def enviar():
        data={}
        data["title"]= entry_title.get()
        data["description"]= entry_description.get()
        status, msg = crear_actividad(data)
        if not status:
            mb.showerror("Ocurrio un error", msg)
            return
        mb.showinfo("Exito!", "Actividad almacenada con exito")
        
    tk.Button(w, command=enviar, text="Guardar", relief="flat", font=TEXT).grid(column=0, row=4, columnspan=3, sticky="n")
    tk.Button(w, command=lambda: mostrar_home_actividades(w), text="Regresar al inicio", relief="flat", font=TEXT).grid(column=0, row=5, columnspan=3, sticky="n", pady=20)

    w.mainloop()
    
