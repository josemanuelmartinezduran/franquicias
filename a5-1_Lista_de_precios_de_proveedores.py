import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
u = uploader.uploader()
fila_inicial = 2
fila_final = 7
nombre_archivo = "precios_prov.csv"

format_list.append(format.format("product_tmpl_id", "many2one", util.col2num("A"), "NoCreate", "product.template", "default_code"))
format_list.append(format.format("name", "many2one", util.col2num("B"), "NoCreate", "res.partner", "name"))
format_list.append(format.format("price", "number", util.col2num("C"), 1, "", ""))
format_list.append(format.format("currency_id", "many2one", util.col2num("D"), "NoCreate", "res.currency", "name"))
format_list.append(format.format("min_qty", "static", 1, 1, 1, 1))
format_list.append(format.format("delay", "static", 1, 1, 1, 1))


u.upload("product.supplierinfo", format_list, fila_inicial, fila_final, nombre_archivo, [("not_null", "name")])

format_list = []
format_list.append(format.format("product_tmpl_id", "many2one", util.col2num("A"), "NoCreate", "product.template", "default_code"))
format_list.append(format.format("name", "many2one", util.col2num("E"), "NoCreate", "res.partner", "name"))
format_list.append(format.format("price", "number", util.col2num("F"), 1, "", ""))
format_list.append(format.format("currency_id", "many2one", util.col2num("G"), "NoCreate", "res.currency", "name"))
format_list.append(format.format("min_qty", "static", 1, 1, 1, 1))
format_list.append(format.format("delay", "static", 1, 1, 1, 1))


u.upload("product.supplierinfo", format_list, fila_inicial, fila_final, nombre_archivo, [("not_null", "name")])

format_list = []
format_list.append(format.format("product_tmpl_id", "many2one", util.col2num("A"), "NoCreate", "product.template", "default_code"))
format_list.append(format.format("name", "many2one", util.col2num("H"), "NoCreate", "res.partner", "name"))
format_list.append(format.format("price", "number", util.col2num("I"), 1, "", ""))
format_list.append(format.format("currency_id", "many2one", util.col2num("J"), "NoCreate", "res.currency", "name"))
format_list.append(format.format("min_qty", "static", 1, 1, 1, 1))
format_list.append(format.format("delay", "static", 1, 1, 1, 1))


u.upload("product.supplierinfo", format_list, fila_inicial, fila_final, nombre_archivo, [("not_null", "name")])


format_list = []
format_list.append(format.format("product_tmpl_id", "many2one", util.col2num("A"), "NoCreate", "product.template", "default_code"))
format_list.append(format.format("name", "many2one", util.col2num("K"), "NoCreate", "res.partner", "name"))
format_list.append(format.format("price", "number", util.col2num("L"), 1, "", ""))
format_list.append(format.format("currency_id", "many2one", util.col2num("M"), "NoCreate", "res.currency", "name"))
format_list.append(format.format("min_qty", "static", 1, 1, 1, 1))
format_list.append(format.format("delay", "static", 1, 1, 1, 1))


u.upload("product.supplierinfo", format_list, fila_inicial, fila_final, nombre_archivo, [("not_null", "name")])