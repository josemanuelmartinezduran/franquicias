import odoorpc
class connection:
    def getConnection(self):
        servidor="metrology.opentechmx.com"
        puerto="7073"
        base_de_datos="llave_en_mano"
        usuario="noreply@"
        password="admin"
        odoo = odoorpc.ODOO(servidor, port=puerto)
        #base de datos, usuario, contraseña
        odoo.login(base_de_datos, usuario, password)
        print("Sesion iniciada {}".format(odoo))
        return odoo
