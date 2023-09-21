import odoorpc
import csv
import os, sys
import utilidades

#datos para cambiar
servidor="127.0.0.1"
puerto="7072"
base_de_datos="franquicias"
usuario="admin"
password="admin"
objeto_a_crear="stock.inventory"

#Donde inicia a cargar datos (filas del archivo de excel)
inicial = 1
#Donde termina de cargar datos
final = 1000
contador = 0
#Ruta del servidor y puerto
odoo = odoorpc.ODOO(servidor, port=puerto)
#base de datos, usuario, contraseña
odoo.login(base_de_datos, usuario, password)
print("Sesion iniciada {}".format(odoo))
#A donde voy a subir mis datos
origin_class = odoo.env[objeto_a_crear]
linea_class = odoo.env["stock.inventory.line"]
u=utilidades.utilidades()
inventory_id = origin_class.create(
        {
            'name': "Inventario base",
            'location_ids': [8],
            "state": "confirm"
        }
    )
#Nombre del archivo csv
with open(os.path.join(sys.path[0], "existencias.csv")) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        priducto_id = u.damelid_nocrear("Caja de almacenaje", "product.product", odoo)
        if(priducto_id == ""):
            continue
        linea = linea_class.create({
            'inventory_id': inventory_id,
            'product_id': priducto_id,
            "product_qty": 3,
            "location_id": 8
        })
        print("linea creada ok {}".format(linea))
