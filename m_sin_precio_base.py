import uploader, format, utilities, connection
format_list = []
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()

###################################
lista_uno = "Precio amigable"
lista_dos = "Mayoreo"
lista_tres = "XXXX"
lista_cuatro = "YYYYY"
columna_uno = "AC"
columna_dos = "AD"
columna_tres = "AE"
columna_cuatro = "AF"
###################################

#Creando la lista
#Modificar por cada lista
id_lista = c.env["product.pricelist"].create({"name": lista_uno})
print("Lista creada {}".format(id_lista))

#Cargando los productos
format_list.append(format.format("applied_on", "static", 1, "1_product", 1, 1))
format_list.append(format.format("min_quantity", "static", 1, 0, 1, 1))
format_list.append(format.format("compute_price", "static", 1, "fixed", 1, 1))
format_list.append(format.format("product_tmpl_id", "many2one", util.col2num("C"), "NoCreate", "product.template", "default_code"))
#Modificar por cada lista
format_list.append(format.format("fixed_price", "number", util.col2num(columna_uno), "", "", ""))
format_list.append(format.format("pricelist_id", "static", 1, id_lista, 1, 1))

u = uploader.uploader()
u.upload("product.pricelist.item", format_list, 2, 10000, "productos_servicios_sin_precio_base.csv")