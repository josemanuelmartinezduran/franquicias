import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
u = uploader.uploader()
fila_inicial = 2
fila_final = 10
nombre_acrchivo = "tipo.csv"
format_list = []

format_list.append(format.format("tipo_sucursal", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("zona", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("tamano", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("es_fabrica", "boolean", util.col2num("D"), "", "", ""))



u = uploader.uploader()
u.upload("franquicia.tipo", format_list, fila_inicial, fila_final, nombre_acrchivo, [('unique', 'tipo_sucursal')])