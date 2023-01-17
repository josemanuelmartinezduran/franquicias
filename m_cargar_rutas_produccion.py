import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []

############################
company_id = 1
############################

format_list.append(format.format("bom_id", "many2one", util.col2num("B"), "NoCreate", "mrp.bom", "code"))
format_list.append(format.format("name", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format("sequence", "number", util.col2num("C"), "", "", ""))
format_list.append(format.format("workcenter_id", "many2one", util.col2num("E"), "NoCreate", "mrp.workcenter", "name"))
format_list.append(format.format("time_cycle_manual", "number", util.col2num("F"), "", "", ""))

u = uploader.uploader()
u.upload("mrp.routing.workcenter", format_list, 2, 10000, "operaciones_fabricacion.csv")