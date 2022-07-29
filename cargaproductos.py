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
u=utilidades.utilidades()
#Nombre del archivo csv
with open(os.path.join(sys.path[0], "mediformtodas.csv")) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    u.borraTodoCuidado("product.template",odoo)
    for row in csv_reader:
        print("Leyendo el csv fila {}".format(contador))
        if contador < inicial:
            contador += 1
            continue
        elif contador > final:
            break
        #PONER TODOS LOS MANY TO ONE
        cat_id=u.damelid(row[3],"product.category",odoo)
        #unidmed=u.damelid(row[3],"uom.uom",odoo)

        contador += 1
        #LIMPIAR DATOS
        precio=u.limpia(row[4])
        seguimiento=u.reemplazaDatos(row[14],["Sin Seguimiento","Lote","Serie"],["none","lot","serial"])
        resultado=-1
        try:
            resultado = origin_class.create({
        
            #Aqui poner tu codigo
            "name": row[0],
            "default_code": row[1],
            'list_price': precio,
            'barcode': row[7],
            'description_sale': row[8],
            'sale_ok': True,
            'purchase_ok': True,
            'type':"product",
            'invoice_policy': "delivery",
            'available_in_pos': True,
            'categ_id': cat_id,
            })
            print("Producto creado id {}".format(resultado))
        except Exception as e:
            u.escribeErrores(contador)
            print(e)
        if(resultado==-1):
            continue
        listas_class = odoo.env['product.pricelist.item']
        listas_class.create({   
            "applied_on":"1_product",
            "product_tmpl_id":resultado,
            "compute_price":"fixed",
            "fixed_price":row[23],
            "pricelist_id":2
            })
        print(resultado)
        listas_class.create({   
            "applied_on":"1_product",
            "product_tmpl_id":resultado,
            "compute_price":"fixed",
            "fixed_price":row[24],
            "pricelist_id":3
            })