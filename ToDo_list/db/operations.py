from ToDo_list.db.db import conn

cur = conn.cursor()

def crear_actividad(data):
    if not data["title"]:
        return (False, "Es necesario enviar un titulo")
    try:
     cur.execute("INSERT INTO activities (titulo, descripcion) VALUES (%s, %s)",(data["title"], data["description"]))
     conn.commit()
     return (True, "Actividad guardado con exito")
    except Exception as e:
        print(e)
        return False

def actualizar_actividad(actividad_id, data):
    if not actividad_id:
        return (False, "Es necesario enviar el ID de la actividad")
    
    if not data["title"] or not data["description"]:
        return (False, "Es necesario enviar todos los parametros para actualizar la actividad")

    cur.execute("SELECT * FROM activities WHERE id = %s", (actividad_id))
    actividad = cur.fetchone()
    if not actividad[1]:
        return (False, "El ID de la actividad no esta reagistrado en la DB")
    
    cur.execute("UPDATE activities SET titulo=%s, descripcion=%s, WHERE id = %s,"(data["title"], data["description"], actividad_id))
    conn.commit()
    return (True, "Actividad acualizada con exito")

def eliminar_actividad(actividad_id):
    cur.execute("DELETE FROM activities WHERE id=%s",(str(actividad_id)))
    conn.commit()
    return(True, "Actividad eliminanda con exito")

def obtener_actividad(actividad_id):
    cur.execute("SELECT * FROM activities WHERE id = %s", (actividad_id))
    actividad = cur.fetchone()
    return actividad

def obtener_actividades():
    cur.execute("SELECT * FROM activities ORDER BY id")
    actividades = cur.fetchall()
    return actividades


