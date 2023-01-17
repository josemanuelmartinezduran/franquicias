import uploader, format, connection, utilities
id_warehouse = 1
id_ubicacion = 8
id_company = 1
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
id_fabricar = util.getIdNoCreate("Fabricar", "stock.location.route", "name", c)
id_comprar = util.getIdNoCreate("Comprar", "stock.location.route", "name", c)

format_list = []
format_list.append(format.format("name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("default_code", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("categ_id", "many2one", util.col2num("D"), "Create", "product.category", "name"))
format_list.append(format.format("list_price", "number", util.col2num("E"), "", "", ""))
format_list.append(format.format("uom_id", "many2one", util.col2num("F"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one", util.col2num("F"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("available_in_pos", "boolean", util.col2num("G"), "options", "model", "compare"))
format_list.append(format.format("clave_sat", "string", util.col2num("H"), "","", ""))
format_list.append(format.format("barcode", "string", util.col2num("I"), "","", ""))
format_list.append(format.format("description_sale", "string", util.col2num("J"), "","", ""))
format_list.append(format.format("weight", "number", util.col2num("K"), "","", ""))
format_list.append(format.format("volume", "number", util.col2num("L"), "","", ""))
format_list.append(format.format("sale_delay", "number", util.col2num("M"), "options", "model", "compare"))
format_list.append(format.format("route_ids", "many2many_selection", util.col2num("N"), [("Lo fabricamos", [id_fabricar]), ("Lo compramos", [id_comprar]), ("Ambos", [id_fabricar, id_comprar])], "model", "compare"))
format_list.append(format.format("standard_price", "number", util.col2num("O"), "", "", ""))
format_list.append(format.format("tracking", "selection", util.col2num("Q"), [("Serie","serial"), ("Lote","lot"), ("Sin seguimiento","none")],"", ""))
format_list.append(format.format("use_expiration_date", "boolean", util.col2num("R"), "options", "model", "compare"))
format_list.append(format.format("expiration_time", "number", util.col2num("S"), "options", "model", "compare"))  
format_list.append(format.format("use_time", "number", util.col2num("T"), "options", "model", "compare"))
format_list.append(format.format("removal_time", "number", util.col2num("U"), "options", "model", "compare"))
format_list.append(format.format("type", "selection", util.col2num("V"), [("Servicio", "service"),("Almacenable", "product"),("Consumible", "consu")],"", ""))
format_list.append(format.format("garantia", "number", util.col2num("Z"), "options", "model", "compare"))
format_list.append(format.format("comision", "number", util.col2num("AA"), "options", "model", "compare"))
format_list.append(format.format("comision_especial", "number", util.col2num("AB"), "options", "model", "compare"))
#format_list.append(format.format("company_id", "static", id_company, 1, "", ""))
format_list.append(format.format("sale_ok", "static", 1, "", "", ""))
format_list.append(format.format("can_be_expensed", "static", 0, "","", ""))



format_list2 = []
format_list2.append(format.format("warehouse_id", "static", id_warehouse, 1, "", ""))
format_list2.append(format.format("location_id", "static", id_ubicacion, 1, "", ""))
format_list2.append(format.format("product_min_qty", "number", util.col2num("X"), "", "", ""))
format_list2.append(format.format("product_max_qty", "number", util.col2num("W"), "", "", ""))
format_list2.append(format.format("qty_multiple", "number", util.col2num("Y"), "","", ""))
format_list2.append(format.format("product_id", "many2one", util.col2num("B"), "NoCreate", "product.product", "name"))


format_list3 = []
#format_list3.append(format.format("company_id", "static", id_company, id_company, 1, 1))
format_list3.append(format.format("location_in_id", "static", id_ubicacion, id_ubicacion, 1, 1))
format_list3.append(format.format("location_out_id", "many2one", util.col2num("P"), "NoCreate", "stock.location", "name"))
format_list3.append(format.format("product_id", "many2one", util.col2num("B"), "NoCreate", "product.product", "default_code"))





u = uploader.uploader()
u.upload("product.template", format_list, 2, 1000, "insumos_produccion.csv", [("unique", "default_code")])
u.upload("stock.warehouse.orderpoint", format_list2, 2, 1000, "insumos_produccion.csv")
u.upload("stock.putaway.rule", format_list3, 2, 1000, "insumos_produccion.csv") 
