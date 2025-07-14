from tkinter import messagebox as mb, Tk, Label, Button
from ToDo_list.views.resources import BACKGROUND, PRIMARY, SECONDARY, TITLES, TEXT, LOGO
from PIL import Image, ImageTk
from ToDo_list.db.operations import obtener_actividades, eliminar_actividad, actualizar_actividad
from ToDo_list.views.activity.crear_actividad import mostrar_crear_actividades
from ToDo_list.views.components.table import show_table


def mostrar_home_actividades(w:Tk):
    def delete_activities(activity_id):
        res = mb.askyesno("¿Seguro de eliminar la actividad?")
        if res:
            eliminar_actividad(activity_id)
            activities = obtener_actividades()
            table_activities(activities)
    def update_client(client_id, client):
        #Funcion para mostrar cliente y actualizar
        pass
    def table_activities(actividades):
        table= show_table(w, 1,3, columnspan=2, padx=10, pady=10 )

        columns=["Titulo", "Descripcion", "Fecha de registro"]
        for i, column in enumerate (columns):
            table.columnconfigure(i, weight=1)
            Label(table, text=column, font= TEXT, bg=PRIMARY, fg=SECONDARY, relief="solid" ).grid(column=i, row=0,sticky="news")
        
        for i, cliente in enumerate(actividades,1):
            Label(table,text=cliente[1],font= TEXT, bg=PRIMARY, fg=SECONDARY, relief="solid" ).grid(column=0, row=i, sticky="news")
            Label(table,text=cliente[2],font= TEXT, bg=PRIMARY, fg=SECONDARY, relief="solid" ).grid(column=1, row=i, sticky="news")
            Label(table,text=cliente[3].strftime("%d-%m-%Y"),font= TEXT, bg=PRIMARY, fg=SECONDARY, relief="solid" ).grid(column=2, row=i, sticky="news")

 
    for widget in w.winfo_children():
        widget.destroy()
    
    #Configurar filas y columnas
    for i in range(6):
        w.rowconfigure(i, weight=1)
        w.columnconfigure(i, weight=1)
    #Logo
    image_pil = Image.open(LOGO)
    resized_image = image_pil.resize((200,200))
    photo = ImageTk.PhotoImage(resized_image)
    w.photo = photo
    Label(w, image=photo, bg=BACKGROUND).grid(column=0, row=0, columnspan=6, sticky="news")
    #Navbar
    #TODO navbar estara en la fila 1
    #Titulo y boton
    Label(w, text="ACTIVIDADES", font=TITLES, bg=BACKGROUND).grid(column=0, row=2, columnspan=6, sticky="n")
    Button(w, text="Crear actividad", font=TEXT, bg=PRIMARY, fg=SECONDARY, relief="groove", command=lambda:mostrar_crear_actividades(w)).grid(column=4, sticky="n", row=2, padx=10)
    #Tabla    
    actividades= obtener_actividades()
    table_activities(actividades)
   
    w.mainloop()