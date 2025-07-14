from ToDo_list.db.db_init import iniciar_db
from ToDo_list.views.main import ventana
from ToDo_list.views.activity.home import mostrar_home_actividades
#Iniciamos la DB
iniciar_db()
#Ejecutamos las ventanas 
mostrar_home_actividades(ventana)
