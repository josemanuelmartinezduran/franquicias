import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []

format_list.append(format.format("tipo_sucursal", "many2one", util.col2num("A"), "NoCreate", "franquicia.tipo", "tipo_sucursal"))
format_list.append(format.format("concepto", "many2one", util.col2num("B"), "Create", "product.template", "name"))
format_list.append(format.format("tipo", "selection", util.col2num("C"), [("Fijo","Fijo"), ("%", "Porcentaje")],"", ""))
format_list.append(format.format("monto", "number", util.col2num("D"), "", "", ""))
format_list.append(format.format("porcentaje", "number", util.col2num("E"), "", "", ""))
format_list.append(format.format("iva", "exclusiveboolean", util.col2num("F"), True,"Con IVA", "IF"))
format_list.append(format.format("frecuencia", "selection", util.col2num("G"), [("Diario","Diario"), ("Semanal", "Semanal"), ("Mensual", "Mensual"), ("Bimetral", "Bimestral"), ("Trimestral", "Trimestral"), ("Semestral", "Semestral"), ("Anual", "Anual")],"", ""))
format_list.append(format.format("produce_bloqueo", "boolean", util.col2num("I"), "", "", ""))
format_list.append(format.format("dia_cobro", "string", util.col2num("H"), "", "", ""))
format_list.append(format.format("dias_bloqueo", "number", util.col2num("J"), "", "", ""))
format_list.append(format.format("desbloqueo_automatico", "number", util.col2num("K"), "", "", ""))

u = uploader.uploader()
u.upload("franquicia.regalia", format_list, 2, 10000, "regalias.csv")
