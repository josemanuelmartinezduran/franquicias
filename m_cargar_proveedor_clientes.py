import uploader, format, utilities, connection
company_id = 1
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
id_mx = util.getIdNoCreate("México", "res.country", "name", c)
format_list = []
format_list.append(format.format("customer", "boolean", 0, "options", "model", "compare"))
format_list.append(format.format("supplier", "boolean", 1, "options", "model", "compare"))
format_list.append(format.format("company_type", "selection", 2, [("Individual", "person"),("Compañia", "company")], "model", "compare"))
format_list.append(format.format("name", "string", 3, "", "", ""))
format_list.append(format.format("property_product_pricelist", "many2one", 5, "NoCreate", "product.pricelist", "name"))
format_list.append(format.format("property_supplier_payment_term_id", "many2one", 6, "NoCreate", "account.payment.term", "name"))
format_list.append(format.format("property_payment_term_id", "many2one", 7, "NoCreate", "account.payment.term", "name"))
format_list.append(format.format("phone", "string", 8, "", "", ""))
format_list.append(format.format("email", "string", 9, "", "", ""))
format_list.append(format.format("street", "string", 10, "", "", ""))
format_list.append(format.format("street2", "string", 11, "", "", ""))
format_list.append(format.format("zip", "string", 12, "", "", ""))
format_list.append(format.format("city", "string", 13, "", "", ""))
format_list.append(format.format("state_id", "many2one", 14, "NoCreate", "res.country.state", "name"))
format_list.append(format.format("country_id", "many2one", 15, "NoCreate", "res.country", "name"))
format_list.append(format.format("rfc", "string", 16, "", "", ""))
format_list.append(format.format("company_id", "selection", 17, [("Si", ""), ("No", company_id)], "model", "compare"))



format_list2 = []
format_list2.append(format.format("name", "string", 4, "options", "model", "compare"))
format_list2.append(format.format("parent_id", "many2one", 3, "NoCreate", "res.partner", "name"))
format_list.append(format.format("company_type", "static", "person", "person", "model", "compare"))



#Agregar contactos

u = uploader.uploader()
u.upload("res.partner",format_list,2,1000,"proveedoresclientes.csv")
u.upload("res.partner",format_list2,2,1000,"proveedoresclientes.csv")