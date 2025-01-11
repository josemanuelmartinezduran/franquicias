import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
fila_inicial = 2
fila_final = 3
nombre_archivo = ".csv"
u = uploader.uploader()

format_list.append(format.format("name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("prject_ids", "many2many_search", util.col2num("B"), "name", "project.project"), "", "")

u.upload("project.task.type", format_list, fila_inicial, fila_final, nombre_archivo)