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
format_list.append(format.format("name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("default_code", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("categ_id", "many2one", util.col2num("C"), "Create", "product.category", "name"))
format_list.append(format.format("list_price", "number", util.col2num("D"), "", "", ""))
format_list.append(format.format("uom_id", "many2one", util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one", util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("available_in_pos", "boolean", util.col2num("F"), "options", "model", "compare"))
format_list.append(format.format("clave_sat", "string", util.col2num("G"), "","", ""))
format_list.append(format.format("barcode", "string", util.col2num("H"), "","", ""))
format_list.append(format.format("description_sale", "string", util.col2num("J"), "","", ""))
format_list.append(format.format("sale_delay", "number", util.col2num("I"), "options", "model", "compare"))
format_list.append(format.format("standard_price", "number", util.col2num("K"), "", "", ""))
format_list.append(format.format("type", "static", 1, "service", 1, 1))
format_list.append(format.format("garantia", "number", util.col2num("L"), "options", "model", "compare"))
format_list.append(format.format("comision", "number", util.col2num("M"), "options", "model", "compare"))
format_list.append(format.format("comision_especial", "number", util.col2num("N"), "options", "model", "compare"))
format_list.append(format.format("service_policy", "selection", util.col2num("O"), [("Por entrega","delivered_manual"), ("Por horas trabajadas", "delivered_timesheet"), ("Por Proyecto Prepagado", "ordered_timesheet")],"", ""))
format_list.append(format.format("sale_ok", "static", 1, "", "", ""))
format_list.append(format.format("can_be_expensed", "static", 0, "","", ""))
format_list.append(format.format("service_tracking", "selection", util.col2num("P"), [("Se crea un proyecto en base a una plantilla","project_only"), ("Se crea un nuevo proyecto", "project_only"), ("Se agrega una tarea","task_global_project")],"", ""))
format_list.append(format.format("project_template_id", "many2one", util.col2num("Q"), "NoCreate", "project.project", "name"))




u = uploader.uploader()
u.upload("product.template", format_list, 2, 1000, "servicios_proyecto.csv", [("unique", "default_code"), ("not_equal", ["service_policy", "task_global_project"])])


format_list = []
format_list.append(format.format("name", "string", util.col2num("A"), "", "", ""))
format_list.append(format.format("default_code", "string", util.col2num("B"), "", "", ""))
format_list.append(format.format("categ_id", "many2one", util.col2num("C"), "Create", "product.category", "name"))
format_list.append(format.format("list_price", "number", util.col2num("D"), "", "", ""))
format_list.append(format.format("uom_id", "many2one", util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one", util.col2num("E"), "NoCreate", "uom.uom", "name"))
format_list.append(format.format("available_in_pos", "boolean", util.col2num("F"), "options", "model", "compare"))
format_list.append(format.format("clave_sat", "string", util.col2num("G"), "","", ""))
format_list.append(format.format("barcode", "string", util.col2num("H"), "","", ""))
format_list.append(format.format("description_sale", "string", util.col2num("J"), "","", ""))
format_list.append(format.format("sale_delay", "number", util.col2num("I"), "options", "model", "compare"))
format_list.append(format.format("standard_price", "number", util.col2num("K"), "", "", ""))
format_list.append(format.format("type", "static", 1, "service", 1, 1))
format_list.append(format.format("garantia", "number", util.col2num("L"), "options", "model", "compare"))
format_list.append(format.format("comision", "number", util.col2num("M"), "options", "model", "compare"))
format_list.append(format.format("comision_especial", "number", util.col2num("N"), "options", "model", "compare"))
format_list.append(format.format("service_policy", "selection", util.col2num("O"), [("Por entrega","delivered_manual"), ("Por horas trabajadas", "delivered_timesheet"), ("Por Proyecto Prepagado", "ordered_timesheet")],"", ""))
format_list.append(format.format("sale_ok", "static", 1, "", "", ""))
format_list.append(format.format("can_be_expensed", "static", 0, "","", ""))
format_list.append(format.format("service_tracking", "selection", util.col2num("P"), [("Se crea un proyecto en base a una plantilla","project_only"), ("Se crea un nuevo proyecto", "project_only"), ("Se agrega una tarea","task_global_project")],"", ""))
format_list.append(format.format("project_id", "many2one", util.col2num("R"), "NoCreate", "project.project", "name"))

u.upload("product.template", format_list, 2, 1000, "servicios_proyecto.csv", [("unique", "default_code"), ("equal", ["service_policy", "task_global_project"])])