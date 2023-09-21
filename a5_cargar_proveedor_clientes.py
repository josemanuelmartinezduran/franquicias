import uploader
import format
import utilities
import connection
company_id = 1
format_list = []
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
id_mx = util.getIdNoCreate("México", "res.country", "name", c)
nombre_archivo = "clientes.csv"
es_franquicia = True
fina_inicial = 2
fila_final= 4
format_list = []
format_list.append(format.format("customer", "boolean",
                   util.col2num("A"), "options", "model", "compare"))
format_list.append(format.format("supplier", "boolean",
                   util.col2num("B"), "options", "model", "compare"))
format_list.append(format.format("company_type", "selection", util.col2num(
    "C"), [("Individual", "person"), ("Compañia", "company")], "model", "compare"))
format_list.append(format.format(
    "name", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format("property_product_pricelist", "many2one",
                   util.col2num("G"), "NoCreate", "product.pricelist", "name"))
format_list.append(format.format("property_supplier_payment_term_id",
                   "many2one", util.col2num("G"), "NoCreate", "account.payment.term", "name"))
format_list.append(format.format("property_payment_term_id", "many2one",
                   util.col2num("G"), "NoCreate", "account.payment.term", "name"))
format_list.append(format.format(
    "phone", "string", util.col2num("H"), "", "", ""))
format_list.append(format.format(
    "email", "string", util.col2num("I"), "", "", ""))
format_list.append(format.format(
    "street", "string", util.col2num("J"), "", "", ""))
format_list.append(format.format(
    "street2", "string", util.col2num("K"), "", "", ""))
format_list.append(format.format(
    "zip", "string", util.col2num("L"), "", "", ""))
format_list.append(format.format(
    "city", "string", util.col2num("M"), "", "", ""))
format_list.append(format.format("state_id", "many2one", util.col2num(
    "N"), "NoCreate", "res.country.state", "name"))
format_list.append(format.format("country_id", "many2one",
                   util.col2num("O"), "NoCreate", "res.country", "name"))
format_list.append(format.format(
    "rfc", "string", util.col2num("AG"), "", "", ""))
format_list.append(format.format("razon", "string",
                   util.col2num("AB"), "", "", ""))
format_list.append(format.format(
    "regimen", "substring", util.col2num("AC"), 0, 3, ""))
format_list.append(format.format(
    "uso", "substring", util.col2num("AD"), 0, 3, ""))
format_list.append(format.format("domicilio", "string",
                   util.col2num("AE"), "", "", ""))
format_list.append(format.format(
    "cp", "string", util.col2num("AF"), "", "", ""))
if (es_franquicia):
    format_list.append(format.format("company_id", "selection", util.col2num(
        "AI"), [("Si", ""), ("No", company_id)], "model", "compare"))
# Subimos a todos los clientes
u = uploader.uploader()
u.upload("res.partner", format_list, fina_inicial, fila_final, nombre_archivo)

format_list.append(format.format("customer", "boolean",
                   util.col2num("A"), "options", "model", "compare"))
format_list.append(format.format("supplier", "boolean",
                   util.col2num("B"), "options", "model", "compare"))
format_list.append(format.format("company_type", "selection", util.col2num(
    "C"), [("Individual", "person"), ("Compañia", "company")], "model", "compare"))
format_list.append(format.format(
    "name", "string", util.col2num("D"), "", "", ""))
format_list.append(format.format("property_product_pricelist", "many2one",
                   util.col2num("G"), "NoCreate", "product.pricelist", "name"))
format_list.append(format.format("property_supplier_payment_term_id",
                   "many2one", util.col2num("G"), "NoCreate", "account.payment.term", "name"))
format_list.append(format.format("property_payment_term_id", "many2one",
                   util.col2num("G"), "NoCreate", "account.payment.term", "name"))
format_list.append(format.format(
    "phone", "string", util.col2num("H"), "", "", ""))
format_list.append(format.format(
    "email", "string", util.col2num("I"), "", "", ""))
format_list.append(format.format(
    "street", "string", util.col2num("J"), "", "", ""))
format_list.append(format.format(
    "street2", "string", util.col2num("K"), "", "", ""))
format_list.append(format.format(
    "zip", "string", util.col2num("L"), "", "", ""))
format_list.append(format.format(
    "city", "string", util.col2num("M"), "", "", ""))
format_list.append(format.format("state_id", "many2one", util.col2num(
    "N"), "NoCreate", "res.country.state", "name"))
format_list.append(format.format("country_id", "many2one",
                   util.col2num("O"), "NoCreate", "res.country", "name"))
format_list.append(format.format(
    "rfc", "string", util.col2num("AG"), "", "", ""))
format_list.append(format.format("razon", "string",
                   util.col2num("AB"), "", "", ""))
format_list.append(format.format(
    "regimen", "substring", util.col2num("AC"), 0, 3, ""))
format_list.append(format.format(
    "uso", "substring", util.col2num("AD"), 0, 3, ""))
format_list.append(format.format("domicilio", "string",
                   util.col2num("AE"), "", "", ""))
format_list.append(format.format(
    "cp", "string", util.col2num("AF"), "", "", ""))
if (es_franquicia):
    format_list.append(format.format("company_id", "selection", util.col2num(
        "AI"), [("Si", ""), ("No", company_id)], "model", "compare"))
# Subimos a todos los clientes que no tienen contacto principal
u = uploader.uploader()
u.upload("res.partner", format_list, fina_inicial,
         fila_final, nombre_archivo, [("unique", "name")])


format_list2 = []
format_list2.append(format.format(
    "name", "string", 4, "options", "model", "compare"))
format_list2.append(format.format("parent_id", "many2one",
                    3, "NoCreate", "res.partner", "name"))
format_list.append(format.format("company_type", "static",
                   "person", "person", "model", "compare"))
u.upload("res.partner", format_list2, fina_inicial,
         fila_final, nombre_archivo, [("not_null", "name")])

format_list3 = []
format_list3.append(format.format(
    "name", "string", util.col2num("Q"), "", "", ""))
format_list3.append(format.format(
    "email", "string", util.col2num("R"), "", "", ""))
format_list3.append(format.format("parent_id", "many2one",
                    3, "NoCreate", "res.partner", "name"))
format_list3.append(format.format("company_type", "static",
                    "person", "person", "model", "compare"))
u.upload("res.partner", format_list3, fina_inicial,
         fila_final, nombre_archivo, [("not_null", "name")])

format_list4 = []
format_list4.append(format.format(
    "name", "string", util.col2num("S"), "", "", ""))
format_list4.append(format.format(
    "email", "string", util.col2num("T"), "", "", ""))
format_list4.append(format.format("parent_id", "many2one",
                    3, "NoCreate", "res.partner", "name"))
format_list4.append(format.format("company_type", "static",
                    "person", "person", "model", "compare"))
u.upload("res.partner", format_list4, fina_inicial,
         fila_final, nombre_archivo, [("not_null", "name")])

format_list5 = []
format_list5.append(format.format(
    "name", "string", util.col2num("U"), "", "", ""))
format_list5.append(format.format(
    "email", "string", util.col2num("V"), "", "", ""))
format_list5.append(format.format("parent_id", "many2one",
                    3, "NoCreate", "res.partner", "name"))
format_list5.append(format.format("company_type", "static",
                    "person", "person", "model", "compare"))
u.upload("res.partner", format_list5, fina_inicial,
         fila_final, nombre_archivo, [("not_null", "name")])

format_list6 = []
format_list6.append(format.format(
    "name", "string", util.col2num("W"), "", "", ""))
format_list6.append(format.format(
    "email", "string", util.col2num("X"), "", "", ""))
format_list6.append(format.format("parent_id", "many2one",
                    3, "NoCreate", "res.partner", "name"))
format_list6.append(format.format("company_type", "static",
                    "person", "person", "model", "compare"))
u.upload("res.partner", format_list6, fina_inicial,
         fila_final, nombre_archivo, [("not_null", "name")])

format_list7 = []
format_list7.append(format.format(
    "name", "string", util.col2num("Y"), "", "", ""))
format_list7.append(format.format(
    "email", "string", util.col2num("Z"), "", "", ""))
format_list7.append(format.format("parent_id", "many2one",
                    3, "NoCreate", "res.partner", "name"))
format_list7.append(format.format("company_type", "static",
                    "person", "person", "model", "compare"))
u.upload("res.partner", format_list7, fina_inicial,
         fila_final, nombre_archivo, [("not_null", "name")])