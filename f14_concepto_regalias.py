import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
u = uploader.uploader()
fila_inicial = 2
fila_final = 20
nombre_acrchivo = "regalias.csv"
format_list = []

format_list = []
format_list.append(format.format("name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("default_code", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("available_in_pos", "static", 1, False, 1, 1))
format_list.append(format.format("clave_sat", "string", util.col2num("D"), "","", ""))
format_list.append(format.format("unidad_sat", "string", util.col2num("E"), "","", ""))
format_list.append(format.format("type", "static", 1, "service", 1, 1))
format_list.append(format.format("sale_ok", "static", 1, "", "", ""))


u.upload("product.template", format_list, fila_inicial, fila_final, nombre_acrchivo, [("unique", "default_code")])

format_list = []

format_list.append(format.format("tipo_sucursal", "many2one", util.col2num("A"), "NoCreate", "franquicia.tipo", "tipo_sucursal"))
format_list.append(format.format("concepto", "many2one", util.col2num("B"), "Create", "product.template", "name"))
format_list.append(format.format("tipo", "selection", util.col2num("F"), [("Fijo","Fijo"), ("%", "Porcentaje"), ("default", "Fijo")],"", ""))
format_list.append(format.format("monto", "number", util.col2num("G"), "", "", ""))
format_list.append(format.format("porcentaje", "number", util.col2num("H"), "", "", ""))
format_list.append(format.format("iva", "exclusiveboolean", util.col2num("I"), True,"Con IVA", "IF"))
format_list.append(format.format("frecuencia", "selection", util.col2num("J"), [("Diario","Diario"), ("Semanal", "Semanal"), ("Quincenal", "quincenal"), ("Mensual", "Mensual"), ("Bimsetral", "Bimestral"), ("Trimestral", "Trimestral"), ("Semestral", "Semestral"),("Semestral", "Semestral"), ("Anual", "Anual"), ("default", "Anual")],"", ""))
format_list.append(format.format("produce_bloqueo", "boolean", util.col2num("L"), "", "", ""))
format_list.append(format.format("dia_cobro", "string", util.col2num("K"), "", "", ""))
format_list.append(format.format("dias_bloqueo", "number", util.col2num("M"), "", "", ""))
format_list.append(format.format("desbloqueo_automatico", "number", util.col2num("N"), "", "", ""))

u = uploader.uploader()
u.upload("franquicia.regalia", format_list, fila_inicial, fila_final, nombre_acrchivo, [])