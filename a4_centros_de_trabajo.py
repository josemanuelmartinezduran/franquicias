import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
fila_inicial = 2
fila_final = 6
nombre_archivo = "centros.csv"
u = uploader.uploader()

format_list.append(format.format("name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("time_efficiency", "number", util.col2num("B"), 100, "", ""))
format_list.append(format.format("capacity", "number", util.col2num("C"), 1, "", ""))
format_list.append(format.format("oee_target", "number", util.col2num("D"), 90, "", ""))
format_list.append(format.format("costs_hour", "number", util.col2num("E"), 0, "", ""))
format_list.append(format.format("time_start", "number", util.col2num("F"), 0, "", ""))
format_list.append(format.format("time_stop", "number", util.col2num("G"), 0, "", ""))

    
u.upload("mrp.workcenter", format_list, fila_inicial, fila_final, nombre_archivo)