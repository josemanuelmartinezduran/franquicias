import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
format_list.append(format.format("field", "many2many", util.col2num("column"), ["IndexList"]), "", ""))

u = uploader.updater()
u.update("tipo_franquicia", format_list, 2, 10000, "productos_tipo_franquicia.csv", util.col2num("A"), "many2one", "name", [])
