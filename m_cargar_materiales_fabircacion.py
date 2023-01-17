import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
format_list.append(format.format("purchase_ok", "boolean", util.col2num("L"), "", "", ""))
format_list.append(format.format("sale_ok", "boolean", util.col2num("M"), "", "", ""))
format_list.append(format.format("name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("categ_id", "many2one", util.col2num("C"), "Create", "product.category", "name"))
format_list.append(format.format("default_code", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("uom_id", "many2one", util.col2num("J"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one", util.col2num("J"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("clave_sat", "string", util.col2num("D"), "","", ""))
format_list.append(format.format("barcode", "string", util.col2num("E"), "","", ""))
format_list.append(format.format("weight", "number", util.col2num("F"), "","", ""))
format_list.append(format.format("volume", "number", util.col2num("G"), "","", ""))
format_list.append(format.format("can_be_expensed", "static", 0, 0,"", ""))
format_list.append(format.format("tracking", "selection", util.col2num("H"), [("Serie","serial"), ("Lote","lot"), ("Sin seguimiento","none")],"", ""))
format_list.append(format.format("type", "static", 1, "product", 1, 1))
u = uploader.uploader()
#u.upload("product.template", format_list, 2, 10000, "materiales_fabricación.csv", [("not_null", "name")])

#Creando la lista de materiales
format_list = []
format_list.append(format.format("product_tmpl_id", "many2one", util.col2num("B"), "NoCreate", "product.template", "default_code"))
format_list.append(format.format("code", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("product_qty", "number", util.col2num("I"), "", "", ""))
format_list.append(format.format("product_uom_id", "many2one", util.col2num("J"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("type", "static", 1, "normal", 1, 1))
#u.upload("mrp.bom", format_list, 2, 10000, "materiales_fabricación.csv", [("not_null", "product_tmpl_id")])

#Creando las lineas
format_list = []
format_list.append(format.format("bom_id", "many2one", util.col2num("B"), "NoCreate", "mrp.bom", "code"))
format_list.append(format.format("product_id", "many2one", util.col2num("N"), "NoCreate", "product.product", "default_code"))
format_list.append(format.format("product_qty", "number", util.col2num("O"), "", "", ""))
format_list.append(format.format("product_uom_id", "many2one", util.col2num("P"), "NoCreate", "uom.uom", "name"))
u.upload("mrp.bom.line", format_list, 2, 10000, "materiales_fabricación.csv")