import uploader, format, connection, utilities
id_warehouse = 1
id_ubicacion = 8
id_company = 1
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()

#Modificar por consultor
nombre_archivo = "agosto_saza.csv"
fila_inicial = 3
fila_final = 3000
cargar_seguimiento = True
cargar_fechas_caducidad = True
cargar_lotes = False
es_franquicia = True
es_multisucursal = False
cargar_minimos = False
cargar_almacen_inicial = False
carga_rutas = False


id_fabricar = util.getIdNoCreate("Fabricar", "stock.location.route", "name", c)
id_comprar = util.getIdNoCreate("Comprar", "stock.location.route", "name", c)

format_list = []
format_list.append(format.format("name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("default_code", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("categ_id", "many2one", util.col2num("D"), "Create", "product.category", "name"))
format_list.append(format.format("list_price", "number", util.col2num("AA"), "", "", ""))
format_list.append(format.format("uom_id", "many2one", util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one", util.col2num("AB"), "NoCreate", "uom.uom", "name"))
#format_list.append(format.format("uom_id", "static", 1, "1", 1, 1))
#format_list.append(format.format("uom_po_id", "static", 1, "1", 1, 1))
format_list.append(format.format("available_in_pos", "boolean", util.col2num("F"), "options", "model", "compare"))
format_list.append(format.format("barcode", "string", util.col2num("G"), "","", ""))
format_list.append(format.format("description_sale", "string", util.col2num("H"), "","", ""))
format_list.append(format.format("weight", "number", util.col2num("I"), "","", ""))
format_list.append(format.format("volume", "number", util.col2num("J"), "","", ""))
format_list.append(format.format("sale_delay", "number", util.col2num("K"), "options", "model", "compare"))
format_list.append(format.format("route_ids", "many2many_selection", util.col2num("L"), [("lo fabricamos", [id_fabricar]), ("lo compramos", [id_comprar]), ("ambos", [id_fabricar, id_comprar])], "model", "compare"))
format_list.append(format.format("sale_ok", "static", 1, 1, "", ""))
format_list.append(format.format("can_be_expensed", "static", 0, "","", ""))
format_list.append(format.format("standard_price", "number", util.col2num("AC"), "", "", ""))
if(cargar_seguimiento):
    format_list.append(format.format("tracking", "selection", util.col2num("M"), [("Sí","serial"), ("Lote","lot"), ("Sin seguimiento","none"), ("default", "none")],"", ""))
if(cargar_fechas_caducidad):
    format_list.append(format.format("use_expiration_date", "boolean", util.col2num("N"), "options", "model", "compare"))
    format_list.append(format.format("expiration_time", "number", util.col2num("O"), "options", "model", "compare"))  
    format_list.append(format.format("use_time", "number", util.col2num("P"), "options", "model", "compare"))
    format_list.append(format.format("removal_time", "number", util.col2num("Q"), "options", "model", "compare"))
format_list.append(format.format("type", "selection", util.col2num("R"), [("Servicio", "service"),("Almacenable", "product"),("Consumible", "consu"),("default", "product")],"", ""))
format_list.append(format.format("clave_sat", "string", util.col2num("S"), "", "", ""))
format_list.append(format.format("unidad_sat", "string", util.col2num("T"), "", "", ""))

if(es_franquicia):
    format_list.append(format.format("garantia", "number", util.col2num("U"), "options", "model", "compare"))
    format_list.append(format.format("comision", "number", util.col2num("V"), "options", "model", "compare"))
    format_list.append(format.format("comision_especial", "number", util.col2num("W"), "options", "model", "compare"))

#if(es_multisucursal):
#    format_list.append(format.format("company_us", "many2many_comas", util.col2num("AE"), "name", "res.company", ""))

format_list2 = []
format_list2.append(format.format("warehouse_id", "static", id_warehouse, 1, "", ""))
format_list2.append(format.format("location_id", "static", id_ubicacion, 1, "", ""))
format_list2.append(format.format("product_min_qty", "number", util.col2num("Y"), "", "", ""))
format_list2.append(format.format("product_max_qty", "number", util.col2num("X"), "", "", ""))
format_list2.append(format.format("qty_multiple", "number", util.col2num("Z"), 1,"", ""))
format_list2.append(format.format("product_id", "many2one", util.col2num("B"), "NoCreate", "product.product", "name"))

format_list3 = []
if(es_multisucursal):
    format_list3.append(format.format("company_id", "static", id_company, id_company, 1, 1))
format_list3.append(format.format("location_in_id", "static", id_ubicacion, id_ubicacion, 1, 1))
format_list3.append(format.format("location_out_id", "many2one", util.col2num("AH"), "NoCreate", "stock.location", "name"))
format_list3.append(format.format("product_id", "many2one", util.col2num("B"), "NoCreate", "product.product", "default_code"))

################Tarjeta de lealtad#####################
format_list.append(format.format("puntos_compra", "string", util.col2num("AD"), 0, "", ""))
format_list.append(format.format("costo_puntos", "number", util.col2num("AE"), 0, "", ""))


############Campos Especificos SAZA#####################
format_list.append(format.format("grupo_med", "selection", util.col2num("AM"), [("GRUPO 1","Uno"), ("GRUPO 2","Dos"), ("GRUPO 3","Tres"), ("SIN CONTROL",""), ("default", "")],"", ""))
format_list.append(format.format("nombre_laboratorio", "string", util.col2num("AI"), "", "", ""))
format_list.append(format.format("sustancia_activa", "string", util.col2num("AJ"), "", "", ""))
format_list.append(format.format("tasa_iva", "number", util.col2num("AF"), 16, "", ""))
format_list.append(format.format("tasa_ieps", "number", util.col2num("AG"), 0, "", ""))
format_list.append(format.format("registro_senasica", "string", util.col2num("AK"), "", "", ""))
format_list.append(format.format("departamento", "string", util.col2num("AL"), "", "", ""))



u = uploader.uploader()
u.upload("product.template", format_list, fila_inicial, fila_final, nombre_archivo, [("unique", "default_code")])
if(cargar_minimos):
    u.upload("stock.warehouse.orderpoint", format_list2, fila_inicial, fila_final, nombre_archivo)
if(cargar_seguimiento):
    u.upload("stock.putaway.rule", format_list3, fila_inicial, fila_final, nombre_archivo)