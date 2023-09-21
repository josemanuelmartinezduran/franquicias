import uploader, format, connection, utilities
id_warehouse = 1
id_ubicacion = 8
id_company = 1

con = connection.connection()
c = con.getConnection()
util = utilities.utilities()

#Modificar por consultor
nombre_archivo = "listainsum.csv"
fila_inicial = 2
fila_final = 3
cargar_minimos = True
cargar_almacen_inicial = True
cargar_seguimiento = True

format_list = []
format_list.append(format.format("purchase_ok", "static", 1, 1, "", ""))
format_list.append(format.format("sale_ok", "static", 0, "", "", ""))
format_list.append(format.format("name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("categ_id", "many2one", util.col2num("B"), "Create", "product.category", "name"))
format_list.append(format.format("default_code", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("standard_price", "number", util.col2num("D"), "", "", ""))
format_list.append(format.format("uom_id", "many2one", util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one", util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("barcode", "string", util.col2num("G"), "","", ""))
format_list.append(format.format("description_sale", "string", util.col2num("H"), "","", ""))
format_list.append(format.format("description_purchase", "string", util.col2num("I"), "","", ""))
format_list.append(format.format("weight", "number", util.col2num("J"), "","", ""))
format_list.append(format.format("volume", "number", util.col2num("K"), "","", ""))
format_list.append(format.format("can_be_expensed", "string", util.col2num("L"), "","", ""))
if(cargar_seguimiento):
    format_list.append(format.format("tracking", "selection", util.col2num("M"), [("Serie","serial"), ("Lote","lot"), ("Sin seguimiento","none"), ("default","none")],"", ""))
format_list.append(format.format("type", "selection", util.col2num("N"), [("Servicio", "service"),("Almacenable", "product"),("Consumible", "consu")],"", ""))


format_list2 = []
format_list2.append(format.format("warehouse_id", "static", id_warehouse, 1, "", ""))
format_list2.append(format.format("location_id", "static", id_ubicacion, 1, "", ""))
format_list2.append(format.format("product_min_qty", "number", util.col2num("O"), "", "", ""))
format_list2.append(format.format("product_max_qty", "number", util.col2num("P"), "", "", ""))
format_list2.append(format.format("qty_multiple", "numberdefault", util.col2num("Q"), 1,"", ""))
format_list2.append(format.format("product_id", "many2one", util.col2num("C"), "NoCreate", "product.product", "default_code"))


format_list3 = []
format_list3.append(format.format("company_id", "static", id_company, 1, 1, 1))
format_list3.append(format.format("location_in_id", "static", id_ubicacion, 1, 1, 1))
format_list3.append(format.format("location_out_id", "many2one", util.col2num("R"), "NoCreate", "stock.location", "name"))
format_list3.append(format.format("product_id", "many2one", 2, "NoCreate", "product.product", "default_code"))


""" Regla de recepcion en dos pasos columna R-> Almacen final S -> se debe revisar
    format_list4 = []
format_list5 = []
if(carga_rutas):
    format_list4.append(format.format("name", "string", util.col2num("C"), "", "", ""))
    format_list4.append(format.format("product_selectable", "static", 1, True, 1, 1))
    format_list5
 """



u = uploader.uploader()
u.upload("product.template", format_list, fila_inicial, fila_final, nombre_archivo)
if(cargar_minimos):
    u.upload("stock.warehouse.orderpoint", format_list2, fila_inicial, fila_final, nombre_archivo)
if(cargar_almacen_inicial):
    u.upload("stock.putaway.rule", format_list3, fila_inicial, fila_final, nombre_archivo)