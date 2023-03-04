import odoorpc
class connection:
    def getConnection(self):
        servidor="68.178.202.135"
        puerto="7073"
        base_de_datos="iluminamos"
        usuario="noreply@"
        password="1%CF5g0f@v"
        odoo = odoorpc.ODOO(servidor, port=puerto)
        #base de datos, usuario, contraseña
        odoo.login(base_de_datos, usuario, password)
        print("Sesion iniciada {}".format(odoo))
        return odoo
