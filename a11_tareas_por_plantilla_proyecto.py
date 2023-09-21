import uploader
import format
import utilities
import connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()

# Modificar por consultor
nombre_archivo = "listas.csv"
fila_inicial = 2
fila_final = 20


format_list = []
# sin recurrencia
format_list.append(format.format(
    "name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("project_id", "many2one",
                   util.col2num("A"), "NoCreate", "project.project", "name"))
format_list.append(format.format(
    "description", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format(
    "planned_hours", "number", util.col2num("E"), "", "", ""))
format_list.append(format.format(
    "recurring_task", "boolean", util.col2num("F"), "", "", ""))
format_list.append(format.format("stage_id", "many2one",
                   util.col2num("C"), "Create", "project.task.type", "name"))


u = uploader.uploader()
u.upload("project.task", format_list, fila_inicial, fila_final, nombre_archivo,
         [("equal", ["recurring_task", False])])

format_list = []

# Recurrencia for ever
format_list.append(format.format(
    "name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("project_id", "many2one",
                   util.col2num("A"), "NoCreate", "project.project", "name"))
format_list.append(format.format(
    "description", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format(
    "planned_hours", "number", util.col2num("E"), "", "", ""))
format_list.append(format.format(
    "recurring_task", "boolean", util.col2num("F"), "", "", ""))
format_list.append(format.format("stage_id", "many2one",
                   util.col2num("C"), "Create", "project.task.type", "name"))
format_list.append(format.format("repeat_unit", "selection", util.col2num("G"), [(
    "Días", "day"), ("Semanas", "week"), ("Meses", "month"), ("Años", "year")], "", ""))
format_list.append(format.format("repeat_type", "static", 1, "forever", 1, 1))
format_list.append(format.format(
    "repeat_number", "number", util.col2num("H"), "", "", ""))
format_list.append(format.format(
    "mon", "boolean", util.col2num("I"), "", "", ""))
format_list.append(format.format(
    "tue", "boolean", util.col2num("J"), "", "", ""))
format_list.append(format.format(
    "wed", "boolean", util.col2num("K"), "", "", ""))
format_list.append(format.format(
    "thu", "boolean", util.col2num("L"), "", "", ""))
format_list.append(format.format(
    "fri", "boolean", util.col2num("M"), "", "", ""))
format_list.append(format.format(
    "sat", "boolean", util.col2num("N"), "", "", ""))
format_list.append(format.format(
    "sun", "boolean", util.col2num("O"), "", "", ""))

u.upload("project.task", format_list, fila_inicial, fila_final, nombre_archivo, [
         ("equal", ["recurring_task", True]), ("equal", ["repeat_number", 0])])


format_list.append(format.format(
    "name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("project_id", "many2one",
                   util.col2num("A"), "NoCreate", "project.project", "name"))
format_list.append(format.format(
    "description", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format(
    "planned_hours", "number", util.col2num("E"), "", "", ""))
format_list.append(format.format(
    "recurring_task", "boolean", util.col2num("F"), "", "", ""))
format_list.append(format.format("stage_id", "many2one",
                   util.col2num("C"), "Create", "project.task.type", "name"))
format_list.append(format.format("repeat_unit", "selection", util.col2num("G"), [(
    "Días", "day"), ("Semanas", "week"), ("Meses", "month"), ("Años", "year")], "", ""))
format_list.append(format.format("repeat_type", "static", 1, "after", 1, 1))
format_list.append(format.format(
    "repeat_number", "number", util.col2num("H"), "", "", ""))
format_list.append(format.format(
    "mon", "boolean", util.col2num("I"), "", "", ""))
format_list.append(format.format(
    "tue", "boolean", util.col2num("J"), "", "", ""))
format_list.append(format.format(
    "wed", "boolean", util.col2num("K"), "", "", ""))
format_list.append(format.format(
    "thu", "boolean", util.col2num("L"), "", "", ""))
format_list.append(format.format(
    "fri", "boolean", util.col2num("M"), "", "", ""))
format_list.append(format.format(
    "sat", "boolean", util.col2num("N"), "", "", ""))
format_list.append(format.format(
    "sun", "boolean", util.col2num("O"), "", "", ""))

u.upload("project.task", format_list, fila_inicial, fila_final, nombre_archivo, [
         ("equal", ["recurring_task", True]), ("not_equal", ["repeat_number", 0])])


format_list.append(format.format(
    "name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("project_id", "many2one",
                   util.col2num("A"), "NoCreate", "project.project", "name"))
format_list.append(format.format(
    "description", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format(
    "planned_hours", "number", util.col2num("E"), "", "", ""))
format_list.append(format.format(
    "recurring_task", "boolean", util.col2num("F"), "", "", ""))
format_list.append(format.format("stage_id", "many2one",
                   util.col2num("C"), "Create", "project.task.type", "name"))
format_list.append(format.format("repeat_unit", "selection", util.col2num("G"), [(
    "Días", "day"), ("Semanas", "week"), ("Meses", "month"), ("Años", "year")], "", ""))
format_list.append(format.format("repeat_type", "static", 1, "after", 1, 1))
format_list.append(format.format(
    "repeat_number", "number", util.col2num("H"), "", "", ""))
format_list.append(format.format(
    "mon", "boolean", util.col2num("I"), "", "", ""))
format_list.append(format.format(
    "tue", "boolean", util.col2num("J"), "", "", ""))
format_list.append(format.format(
    "wed", "boolean", util.col2num("K"), "", "", ""))
format_list.append(format.format(
    "thu", "boolean", util.col2num("L"), "", "", ""))
format_list.append(format.format(
    "fri", "boolean", util.col2num("M"), "", "", ""))
format_list.append(format.format(
    "sat", "boolean", util.col2num("N"), "", "", ""))
format_list.append(format.format(
    "sun", "boolean", util.col2num("O"), "", "", ""))

u.upload("project.task", format_list, fila_inicial, fila_final, nombre_archivo, [
         ("equal", ["recurring_task", True]), ("not_equal", ["repeat_number", 0])])