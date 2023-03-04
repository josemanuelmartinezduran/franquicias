import uploader, format
id_warehouse = 1
id_ubicacion = 8
id_company = 1

format_list = []
#format_list.append(format.format("company_id", "static", id_company, 1, "", ""))
format_list.append(format.format("purchase_ok", "static", 1, 1, "", ""))
format_list.append(format.format("sale_ok", "static", 0, "", "", ""))
format_list.append(format.format("name", "string", 0, "", "", ""))
format_list.append(format.format("categ_id", "many2one", 1, "Create", "product.category", "name"))
format_list.append(format.format("default_code", "string", 2, "", "", ""))
format_list.append(format.format("standard_price", "number", 3, "", "", ""))
format_list.append(format.format("uom_id", "many2one", 4, "NoCreate", "uom.uom", "name"))
format_list.append(format.format("uom_po_id", "many2one", 4, "NoCreate", "uom.uom", "name"))
format_list.append(format.format("clave_sat", "string", 5, "","", ""))
format_list.append(format.format("barcode", "string", 6, "","", ""))
format_list.append(format.format("description_sale", "string", 7, "","", ""))
format_list.append(format.format("description_purchase", "string", 8, "","", ""))
format_list.append(format.format("weight", "number", 9, "","", ""))
format_list.append(format.format("volume", "number", 10, "","", ""))
format_list.append(format.format("can_be_expensed", "string", 11, "","", ""))
format_list.append(format.format("tracking", "selection", 12, [("Serie","serial"), ("Lote","lot"), ("Sin seguimiento","none")],"", ""))
format_list.append(format.format("type", "selection", 13, [("Servicio", "service"),("Almacenable", "product"),("Consumible", "consu")],"", ""))


format_list2 = []
format_list2.append(format.format("warehouse_id", "static", id_warehouse, 1, "", ""))
format_list2.append(format.format("location_id", "static", id_ubicacion, 1, "", ""))
format_list2.append(format.format("product_min_qty", "number", 14, "", "", ""))
format_list2.append(format.format("product_max_qty", "number", 15, "", "", ""))
format_list2.append(format.format("qty_multiple", "number", 16, "","", ""))
format_list2.append(format.format("product_id", "many2one", 2, "NoCreate", "product.product", "default_code"))


format_list3 = []
format_list3.append(format.format("company_id", "static", id_company, 1, 1, 1))
format_list3.append(format.format("location_in_id", "static", id_ubicacion, 1, 1, 1))
format_list3.append(format.format("location_out_id", "many2one", 18, "NoCreate", "stock.location", "name"))
format_list3.append(format.format("product_id", "many2one", 2, "NoCreate", "product.product", "default_code"))





u = uploader.uploader()
u.upload("product.template", format_list, 2, 3, "listainsum.csv")
#u.upload("stock.warehouse.orderpoint", format_list2, 2, 3, "listainsum.csv")
#u.upload("stock.putaway.rule", format_list3, 2, 3, "listainsum.csv")
