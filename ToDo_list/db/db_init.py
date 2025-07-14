from ToDo_list.db.db import conn

sql_schema = """
CREATE TABLE IF NOT EXISTS 
activities(
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(100) NOT NULL,
  descripcion VARCHAR(100) NOT NULL,
  fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def iniciar_db():
    try:
        cur = conn.cursor()
        cur.execute(sql_schema)
        conn.commit()
        print("SQL Schema Ejecutado con exito")
    except Exception as e:
        print("Ocurrio un error al ejecutar el script")
        print(e)            

iniciar_db()
