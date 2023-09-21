import uploader, format, utilities, connection
con = connection.connection()
c = con.getConnection()
util = utilities.utilities()
format_list = []
product_object = c.env["product.template"]
for i in  product_object.search([]):
    res = product_object.write([i], {'purchase_ok': True})
    print(res)
