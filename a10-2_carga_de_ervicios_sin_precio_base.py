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
id_fabricar = util.getIdNoCreate("Fabricar", "stock.location.route", "name", c)
id_comprar = util.getIdNoCreate("Comprar", "stock.location.route", "name", c)
id_listas_precios = []

# Modificar por consultor
nombre_archivo = "servcon.csv"
fila_inicial = 2
fila_final = 10
es_franquicia = True
listas_precios = ["Precio 1", "2", "3", "4"]
columnas_listas_precios = ["Q", "R", "S", "T"]

format_list = []
format_list.append(format.format(
    "name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format(
    "default_code", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("categ_id", "many2one",
                   util.col2num("C"), "Create", "product.category", "name"))
format_list.append(format.format(
    "list_price", "number", util.col2num("D"), "", "", ""))
format_list.append(format.format("uom_id", "many2one",
                   util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one",
                   util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("available_in_pos", "boolean",
                   util.col2num("F"), "options", "model", "compare"))
format_list.append(format.format(
    "barcode", "string", util.col2num("G"), "", "", ""))
format_list.append(format.format("sale_delay", "number",
                   util.col2num("H"), "options", "model", "compare"))
format_list.append(format.format("description_sale",
                   "string", util.col2num("I"), "", "", ""))
format_list.append(format.format(
    "standard_price", "number", util.col2num("J"), "", "", ""))
format_list.append(format.format("type", "static", 1, "service", 1, 1))
format_list.append(format.format("service_policy", "selection", util.col2num("K"), [("Por entrega", "delivered_manual"), (
    "Por horas trabajadas", "delivered_timesheet"), ("Por Proyecto", "ordered_timesheet"), ("default", "delivered_manual")], "", ""))
format_list.append(format.format("sale_ok", "static", 1, 1, "", ""))
format_list.append(format.format("can_be_expensed", "static", 0, "", "", ""))
format_list.append(format.format("service_tracking", "selection", util.col2num("L"), [("Se crea un proyecto en base a una plantilla", "project_only"), (
    "Se crea un nuevo proyecto", "project_only"), ("Se agrega una tarea", "task_global_project"), ("default", "no")], "", ""))
format_list.append(format.format("project_id", "many2one", util.col2num("N"), "NoCreate", "project.project", "name"))
format_list.append(format.format("clave_sat", "string", util.col2num("O"), "", "", ""))
format_list.append(format.format("unidad_sat", "string", util.col2num("P"), "", "", ""))

if (es_franquicia):
    format_list.append(format.format("garantia", "number",
                       util.col2num("U"), "options", "model", "compare"))
    format_list.append(format.format("comision", "number",
                       util.col2num("V"), "options", "model", "compare"))
    format_list.append(format.format("comision_especial", "number",
                       util.col2num("W"), "options", "model", "compare"))






u = uploader.uploader()
u.upload("product.template", format_list, fila_inicial, fila_final,
         nombre_archivo, [("unique", "default_code"), ("equal", ["service_tracking", "task_global_project"])])


format_list = []
format_list.append(format.format(
    "name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format(
    "default_code", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("categ_id", "many2one",
                   util.col2num("C"), "Create", "product.category", "name"))
format_list.append(format.format(
    "list_price", "number", util.col2num("D"), "", "", ""))
format_list.append(format.format("uom_id", "many2one",
                   util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one",
                   util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("available_in_pos", "boolean",
                   util.col2num("F"), "options", "model", "compare"))
format_list.append(format.format(
    "barcode", "string", util.col2num("G"), "", "", ""))
format_list.append(format.format("sale_delay", "number",
                   util.col2num("H"), "options", "model", "compare"))
format_list.append(format.format("description_sale",
                   "string", util.col2num("I"), "", "", ""))
format_list.append(format.format(
    "standard_price", "number", util.col2num("J"), "", "", ""))
format_list.append(format.format("type", "static", 1, "service", 1, 1))
format_list.append(format.format("service_policy", "selection", util.col2num("K"), [("Por entrega", "delivered_manual"), (
    "Por horas trabajadas", "delivered_timesheet"), ("Por Proyecto", "ordered_timesheet"), ("default", "delivered_manual")], "", ""))
format_list.append(format.format("sale_ok", "static", 1, 1, "", ""))
format_list.append(format.format("can_be_expensed", "static", 0, "", "", ""))
format_list.append(format.format("service_tracking", "selection", util.col2num("L"), [("Se crea un proyecto en base a una plantilla", "project_only"), (
    "Se crea un nuevo proyecto", "project_only"), ("Se agrega una tarea", "task_global_project"), ("default", "no")], "", ""))
format_list.append(format.format("project_template_id", "many2one",
                   util.col2num("M"), "NoCreate", "project.project", "name"))
format_list.append(format.format("clave_sat", "string", util.col2num("O"), "", "", ""))
format_list.append(format.format("unidad_sat", "string", util.col2num("P"), "", "", ""))

if (es_franquicia):
    format_list.append(format.format("garantia", "number",
                       util.col2num("U"), "options", "model", "compare"))
    format_list.append(format.format("comision", "number",
                       util.col2num("V"), "options", "model", "compare"))
    format_list.append(format.format("comision_especial", "number",
                       util.col2num("W"), "options", "model", "compare"))


u.upload("product.template", format_list, fila_inicial, fila_final,
         nombre_archivo, [("unique", "default_code"), ("not_equal", ["service_tracking", "task_global_project"])])

# Creando la lista
# Modificar por cada lista
format_list = []
for i, n in enumerate(listas_precios):
    id_lista = c.env["product.pricelist"].create({"name": n})
    id_listas_precios.append(id_lista)
    print("Lista creada {}".format(id_lista))
    format_list.append(format.format(
        "applied_on", "static", 1, "1_product", 1, 1))
    format_list.append(format.format("min_quantity", "static", 1, 0, 1, 1))
    format_list.append(format.format(
        "compute_price", "static", 1, "fixed", 1, 1))
    format_list.append(format.format("product_tmpl_id", "many2one", util.col2num(
        "B"), "NoCreate", "product.template", "default_code"))
    format_list.append(format.format("fixed_price", "number",
                       util.col2num(columnas_listas_precios[i]), "", "", ""))
    format_list.append(format.format(
        "pricelist_id", "static", 1, id_lista, 1, 1))
    u.upload("product.pricelist.item", format_list,
         fila_inicial, fila_final, nombre_archivo)