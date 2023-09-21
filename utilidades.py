class utilidades():
    def limpia(self, texto):
        nuevoTexto = texto.strip()
        nuevoTexto= nuevoTexto.replace("-", "")
        nuevoTexto= nuevoTexto.replace(".", "")
        nuevoTexto= nuevoTexto.replace(".", "")
        nuevoTexto= nuevoTexto.replace(",", "")
        nuevoTexto= nuevoTexto.replace("/", "")
        nuevoTexto= nuevoTexto.replace("&", "")
        nuevoTexto= nuevoTexto.replace("%", "")
        nuevoTexto= nuevoTexto.replace("'", "")
        nuevoTexto= nuevoTexto.replace("\"", "")
        nuevoTexto= nuevoTexto.replace("  ", "")
        nuevoTexto= nuevoTexto.replace("  ", "")
        nuevoTexto= nuevoTexto.replace("  ", "")
        nuevoTexto= nuevoTexto.replace("  ", "")
        nuevoTexto= nuevoTexto.replace("$", "")
        nuevoTexto= nuevoTexto.replace("N/A", "")
        nuevoTexto = nuevoTexto.strip()
        return nuevoTexto

    def damelid(self,nombre,model,odoo):
        category_class = odoo.env[model]
        model_id = ""
        for cat in category_class.search([('name','like',nombre)]):
            model_id = cat
        if(model_id==""):    
             model_id = category_class.create({
            'name': nombre,
        })
        return model_id
    
    def dameelid_nocrear(self,nombre,model,odoo):
        category_class = odoo.env[model]
        model_id = ""
        for cat in category_class.search([('name','like',nombre)]):
            model_id = cat
        return model_id
    
    def dameelid_nocrear(self,nombre,model,campo,odoo):
        category_class = odoo.env[model]
        model_id = ""
        for cat in category_class.search([(campo,'like',nombre)]):
            model_id = cat
        return model_id
    
    def get_object(self, field, needle, model, odoo):
        category_class = odoo.env[model]
        object = None
        for cat in category_class.search([(field,'like', needle)]):
            object = category_class.browse(cat)
        return object


    def borraTodoCuidado(self, model, odoo):
        delete_class = odoo.env[model]
        for i in  delete_class.search([]):
            delete_class.unlink( [i])


    def reemplazaDatos(self, texto, encuentra, reemplaza):
        contador = 0
        for i in encuentra:
            if texto == i:
                return reemplaza[contador]
            contador += 1


    def escribeErrores(self, error):
        with open('errores.txt', 'w') as f:
            f.write("{} \n".format(error))