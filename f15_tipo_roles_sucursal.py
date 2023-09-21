import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
format_list.append(format.format("productos_disponibles", "many2many_search", util.col2num("C"), "", "product.template", "default_code"))

u = uploader.updater()
u.update("franquicia.tipo", format_list, 2, 5, "spa_productos.csv", util.col2num("A"), "many2one", "tipo_sucursal", [])
