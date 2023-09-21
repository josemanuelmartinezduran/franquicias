import uploader
import format
import connection
import utilities
id_warehouse = 1
id_ubicacion = 8
id_company = 1

con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
u = uploader.uploader() 

# Modificar por consultor
nombre_archivo = "listainsum.csv"
fila_inicial = 2
fila_final = 3
cargar_seguimiento = True

format_list = []
format_list.append(format.format("purchase_ok", "static", 1, 1, "", ""))
format_list.append(format.format("sale_ok", "static", 0, "", "", ""))
format_list.append(format.format(
    "name", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("categ_id", "many2one",
                   util.col2num("C"), "Create", "product.category", "name"))
format_list.append(format.format(
    "default_code", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format(
    "standard_price", "number", util.col2num("E"), "", "", ""))
format_list.append(format.format("uom_id", "many2one",
                   util.col2num("F"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one",
                   util.col2num("F"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format(
    "clave_sat", "string", util.col2num("G"), "", "", ""))
format_list.append(format.format(
    "barcode", "string", util.col2num("H"), "", "", ""))
format_list.append(format.format("description_sale",
                   "string", util.col2num("I"), "", "", ""))
format_list.append(format.format("description_purchase",
                   "string", util.col2num("J"), "", "", ""))
format_list.append(format.format(
    "weight", "number", util.col2num("K"), "", "", ""))
format_list.append(format.format("volume", "number",
                   util.col2num("L"), 0.0, "", ""))
format_list.append(format.format("can_be_expensed", "static", 1, False, 1, 1))
format_list.append(format.format("type", "selection", util.col2num("M"), [(
    "Servicio", "service"), ("Almacenable", "product"), ("Consumible", "consu"), ("default", "product")], "", ""))

if (cargar_seguimiento):
    format_list.append(format.format("tracking", "selection", util.col2num("N"), [(
        "Serie", "serial"), ("Lote", "lot"), ("Sin seguimiento", "none"), ("default", "none")], "", ""))




u.upload("product.template", format_list,
         fila_inicial, fila_final, nombre_archivo, [("unique", "default_code")])

format_list = []
format_list.append(format.format("cargador_id", "many2one", util.col2num("A"), "NoCreate", "franquicia.tipo", "tipo_sucursal"))
format_list.append(format.format("name", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format("costo", "number", util.col2num("E"), 0, "", ""))
format_list.append(format.format("minimo", "number", util.col2num("Q"), 1, "", ""))
format_list.append(format.format("maximo", "number", util.col2num("P"), 1, "", ""))
format_list.append(format.format("multiplo", "number", util.col2num("R"), 1, "", ""))

u.upload("franquicia.cargador.producto", format_list,
         fila_inicial, fila_final, nombre_archivo)