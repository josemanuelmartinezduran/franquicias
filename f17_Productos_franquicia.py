import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
u = uploader.uploader()
# Modificar por consultor
nombre_archivo = "productos_venta.csv"
fila_inicial = 2
fila_final = 100
cargar_seguimiento = True
cargar_fechas_caducidad = True
es_franquicia = True



id_fabricar = util.getIdNoCreate("Fabricar", "stock.location.route", "name", c)
id_comprar = util.getIdNoCreate("Comprar", "stock.location.route", "name", c)

format_list = []
format_list.append(format.format("name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("default_code", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("categ_id", "many2one", util.col2num("D"), "Create", "product.category", "name"))
format_list.append(format.format("uom_id", "many2one", util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one", util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("available_in_pos", "boolean", util.col2num("F"), "options", "model", "compare"))
format_list.append(format.format("barcode", "string", util.col2num("G"), "","", ""))
format_list.append(format.format("description_sale", "string", util.col2num("H"), "","", ""))
format_list.append(format.format("weight", "number", util.col2num("I"), "","", ""))
format_list.append(format.format("volume", "number", util.col2num("J"), "","", ""))
format_list.append(format.format("sale_delay", "number", util.col2num("K"), "options", "model", "compare"))
format_list.append(format.format("route_ids", "many2many_selection", util.col2num("L"), [("lo fabricamos", [id_fabricar]), ("lo compramos", [id_comprar]), ("ambos", [id_fabricar, id_comprar])], "model", "compare"))
format_list.append(format.format("sale_ok", "static", 1, 1, "", ""))
format_list.append(format.format("can_be_expensed", "static", 0, "","", ""))
if(cargar_seguimiento):
    format_list.append(format.format("tracking", "selection", util.col2num("M"), [("Serie","serial"), ("Lote","lot"), ("Sin seguimiento","none"), ("default", "none")],"", ""))
if(cargar_fechas_caducidad):
    format_list.append(format.format("use_expiration_date", "boolean", util.col2num("N"), "options", "model", "compare"))
    format_list.append(format.format("expiration_time", "number", util.col2num("O"), "options", "model", "compare"))  
    format_list.append(format.format("use_time", "number", util.col2num("P"), "options", "model", "compare"))
    format_list.append(format.format("removal_time", "number", util.col2num("Q"), "options", "model", "compare"))
format_list.append(format.format("type", "selection", util.col2num("R"), [("Servicio", "service"),("Almacenable", "product"),("Consumible", "consu"),("default", "product")],"", ""))
format_list.append(format.format("clave_sat", "string", util.col2num("S"), "", "", ""))
format_list.append(format.format("unidad_sat", "string", util.col2num("T"), "", "", ""))
format_list.append(format.format("active", "static", 1, False, 1, 1))
format_list.append(format.format("para_franquicia", "static", 1, True, 1, 1))

if(es_franquicia):
    format_list.append(format.format("garantia", "number", util.col2num("U"), "options", "model", "compare"))
    format_list.append(format.format("comision", "number", util.col2num("V"), "options", "model", "compare"))
    format_list.append(format.format("comision_especial", "number", util.col2num("W"), "options", "model", "compare"))
    
u.upload("product.template", format_list, fila_inicial, fila_final, nombre_archivo, [("unique", "default_code")])


format_list = []
format_list.append(format.format("cargador_id", "many2one", util.col2num("A"), "NoCreate", "franquicia.tipo", "tipo_sucursal"))
format_list.append(format.format("name", "string", util.col2num("C"), "", "", ""))
format_list.append(format.format("precio", "number", util.col2num("AA"), 0, "", ""))
format_list.append(format.format("minimo", "number", util.col2num("Y"), 1, "", ""))
format_list.append(format.format("maximo", "number", util.col2num("X"), 1, "", ""))
format_list.append(format.format("multiplo", "number", util.col2num("Z"), 1, "", ""))

u.upload("franquicia.cargador.producto", format_list,
         fila_inicial, fila_final, nombre_archivo)