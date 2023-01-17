
import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []

format_list.append(format.format("name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("allow_timesheets", "boolean", util.col2num("B"), "", "", ""))
format_list.append(format.format("allow_billable", "boolean", util.col2num("C"), "", "", ""))
format_list.append(format.format("rating_active", "exclusiveboolean", util.col2num("E"), True, "No", "IFNOT"))
format_list.append(format.format("rating_status", "selection", util.col2num("E"), [("A cada cambio de estado","stage"), ("Periódicamente", "periodic")],"stage", ""))
format_list.append(format.format("rating_status_period", "selection", util.col2num("F"), [("Diario","daily"), ("Semanal", "weekly"), ("Dos veces al mes", "bimonthly"), ("Mensual", "monthly"), ("Trimestral", "quarterly"), ("Anual", "yearly")],"daily", ""))
format_list.append(format.format("allow_recurring_tasks", "boolean", util.col2num("D"), "", "", ""))
format_list.append(format.format("label_tasks", "static", 1, "Tareas", 1, 1))

u = uploader.uploader()
u.upload("project.project", format_list, 2, 10000, "plantillas_proyectos.csv")
