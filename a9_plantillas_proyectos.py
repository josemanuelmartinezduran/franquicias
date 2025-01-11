import uploader
import format
import utilities
import connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
u = uploader.uploader()

# Modificar por consultor Plantillas de proyecto
nombre_archivo = "plantillas.csv"
fila_inicial = 21
fila_final = 3

#Modificar por consultor datos de las etapas
nombre_archivo_etapas = "etapas_proyecto.csv"
fila_inicial_etapas = 2
fila_final_etapas = 3


format_list = []
""" format_list.append(format.format(
    "name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("allow_timesheets",
                   "boolean", util.col2num("B"), "", "", ""))
format_list.append(format.format(
    "allow_billable", "boolean", util.col2num("C"), "", "", ""))
format_list.append(format.format(
    "rating_active", "exclusiveboolean", util.col2num("E"), True, "No", "IFNOT"))
format_list.append(format.format("rating_status", "selection", util.col2num("E"), [
                   ("A cada cambio de estado", "stage"), ("Periódicamente", "periodic")], "stage", ""))
format_list.append(format.format("rating_status_period", "selection", util.col2num("F"), [("Diario", "daily"), ("Semanal", "weekly"), (
    "Dos veces al mes", "bimonthly"), ("Mensual", "monthly"), ("Trimestral", "quarterly"), ("Anual", "yearly")], "daily", ""))
format_list.append(format.format("allow_recurring_tasks",
                   "boolean", util.col2num("D"), "", "", ""))
format_list.append(format.format("label_tasks", "static", 1, "Tareas", 1, 1))
format_list.append(format.format("bill_type", "selection", util.col2num("G"), [("1 plantilla por cliente", "customer_project"), (
    "1 plantilla y varios clientes adentro", "customer_task"), ("default", "customer_task")], "", ""))


u.upload("project.project", format_list,
         fila_inicial, fila_final, nombre_archivo) """


format_list = []
format_list.append(format.format("name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("project_ids", "many2many_search", util.col2num("A"), "name", "project.project", ""))

u.upload("project.task.type", format_list, fila_inicial_etapas, fila_final_etapas, nombre_archivo_etapas)