import odoorpc
import csv
import os, sys
import utilidades

#datos para cambiar
servidor="208.109.190.2"
puerto="7073"
base_de_datos="tiendasmediform"
usuario="noreply@"
password="noreply@"
objeto_a_crear="product.template"
#Cambiar
id_proveedor = 1

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
supplier_class = odoo.env["product.supplierinfo"]
u=utilidades.utilidades()

#Recorre todos los productos
for i in origin_class.search([]):
    supplier_class.create({
        "name": id_proveedor,
        "product_id": i,
        "min_qty": 1,
        #Cambiar
        "price": precio
    })