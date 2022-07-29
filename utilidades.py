class utilidades():
    def limpia(self, texto):
        nuevoTexto = texto.strip()
        nuevoTexto= nuevoTexto.replace("-", "")
        nuevoTexto= nuevoTexto.replace(".", "")
        nuevoTexto= nuevoTexto.replace(".", "")
        nuevoTexto= nuevoTexto.replace(",", "")
        nuevoTexto= nuevoTexto.replace("/", "")
        nuevoTexto= nuevoTexto.replace("&", "")
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