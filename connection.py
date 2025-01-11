import odoorpc
class connection:
    def getConnection(self):
        servidor="208.113.166.49"
        puerto="7010"
        base_de_datos="saza"
        usuario="administrador@saza"
        password="Glircboq18"
        odoo = odoorpc.ODOO(servidor, port=puerto)
        #base de datos, usuario, contraseña
        odoo.login(base_de_datos, usuario, password)
        print("Sesion iniciada {}".format(odoo))
        return odoo