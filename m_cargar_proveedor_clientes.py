import uploader, format, utilities, connection
company_id = 1
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
id_mx = util.getIdNoCreate("México", "res.country", "name", c)
format_list = []
format_list.append(format.format("customer", "boolean", util.col2num("A"), "options", "model", "compare"))
format_list.append(format.format("supplier", "boolean", util.col2num("B"), "options", "model", "compare"))
format_list.append(format.format("company_type", "selection", util.col2num("C"), [("Individual", "person"),("Compañia", "company")], "model", "compare"))
format_list.append(format.format("name", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format("property_product_pricelist", "many2one", util.col2num("G"), "NoCreate", "product.pricelist", "name"))
format_list.append(format.format("property_supplier_payment_term_id", "many2one", util.col2num("G"), "NoCreate", "account.payment.term", "name"))
format_list.append(format.format("property_payment_term_id", "many2one", util.col2num("G"), "NoCreate", "account.payment.term", "name"))
format_list.append(format.format("phone", "string", util.col2num("H"), "", "", ""))
format_list.append(format.format("email", "string", util.col2num("I"), "", "", ""))
format_list.append(format.format("street", "string", util.col2num("J"), "", "", ""))
format_list.append(format.format("street2", "string", util.col2num("K"), "", "", ""))
format_list.append(format.format("zip", "string", util.col2num("L"), "", "", ""))
format_list.append(format.format("city", "string", util.col2num("M"), "", "", ""))
format_list.append(format.format("state_id", "many2one", util.col2num("N"), "NoCreate", "res.country.state", "name"))
format_list.append(format.format("country_id", "many2one", util.col2num("O"), "NoCreate", "res.country", "name"))
format_list.append(format.format("rfc", "string", util.col2num("P"), "", "", ""))
#format_list.append(format.format("company_id", "selection", util.col2num("AA"), [("Si", ""), ("No", company_id)], "model", "compare"))



format_list2 = []
format_list2.append(format.format("name", "string", 4, "options", "model", "compare"))
format_list2.append(format.format("parent_id", "many2one", 3, "NoCreate", "res.partner", "name"))
format_list.append(format.format("company_type", "static", "person", "person", "model", "compare"))

format_list3 = []
format_list3.append(format.format("name", "string", util.col2num("Q"), "", "", ""))
format_list3.append(format.format("email", "string", util.col2num("R"), "", "", ""))
format_list3.append(format.format("parent_id", "many2one", 3, "NoCreate", "res.partner", "name"))
format_list3.append(format.format("company_type", "static", "person", "person", "model", "compare"))

format_list4 = []
format_list4.append(format.format("name", "string", util.col2num("S"), "", "", ""))
format_list4.append(format.format("email", "string", util.col2num("T"), "", "", ""))
format_list4.append(format.format("parent_id", "many2one", 3, "NoCreate", "res.partner", "name"))
format_list4.append(format.format("company_type", "static", "person", "person", "model", "compare"))

format_list5 = []
format_list5.append(format.format("name", "string", util.col2num("U"), "", "", ""))
format_list5.append(format.format("email", "string", util.col2num("V"), "", "", ""))
format_list5.append(format.format("parent_id", "many2one", 3, "NoCreate", "res.partner", "name"))
format_list5.append(format.format("company_type", "static", "person", "person", "model", "compare"))

format_list6 = []
format_list6.append(format.format("name", "string", util.col2num("W"), "", "", ""))
format_list6.append(format.format("email", "string", util.col2num("X"), "", "", ""))
format_list6.append(format.format("parent_id", "many2one", 3, "NoCreate", "res.partner", "name"))
format_list6.append(format.format("company_type", "static", "person", "person", "model", "compare"))

format_list7 = []
format_list7.append(format.format("name", "string", util.col2num("Y"), "", "", ""))
format_list7.append(format.format("email", "string", util.col2num("Z"), "", "", ""))
format_list7.append(format.format("parent_id", "many2one", 3, "NoCreate", "res.partner", "name"))
format_list7.append(format.format("company_type", "static", "person", "person", "model", "compare"))


#Agregar contactos

u = uploader.uploader()
u.upload("res.partner",format_list,2,3,"prov.csv")
#u.upload("res.partner",format_list2,2,1000,"proveedoresclientes.csv", [("not_null", "name")])
#
#u.upload("res.partner",format_list3,2,1000,"proveedoresclientes.csv", [("not_null", "name")])
#u.upload("res.partner",format_list4,2,1000,"proveedoresclientes.csv", [("not_null", "name")])
#u.upload("res.partner",format_list5,2,1000,"proveedoresclientes.csv", [("not_null", "name")])
#u.upload("res.partner",format_list6,2,1000,"proveedoresclientes.csv", [("not_null", "name")])
#u.upload("res.partner",format_list7,2,1000,"proveedoresclientes.csv", [("not_null", "name")])


