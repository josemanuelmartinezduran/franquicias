import csv
import os, sys
import connection, utilities


''' 
Formato de format
field:
type: string,static,number,date,datetime
index: 
options:  Create/NoCreate or value for static
model: Related model name
compare: Field to compare

many2one
format_list.append(format.format("campo", "many2one", index, "NoCreate", "model", "campo"))
'''



class uploader():
    def upload(self, model, formatlist, start, end, filename, constraints=[]):
        conn_obj = connection.connection()
        c = conn_obj.getConnection()
        inicial = start
        final = end
        contador = 0    
        print("Sesion iniciada {}".format(c))
        origin_class = c.env[model]
        u=utilities.utilities()
        with open(os.path.join(sys.path[0], "datafiles/{}".format(filename))) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')    
            for row in csv_reader:
                contador += 1
                print("Row {}".format(contador))
                if(contador < inicial):
                    continue
                elif(contador >= final):
                    break
                data = {}
                for f  in formatlist:
                    if(f.type=="string"):
                        valor = row[f.index]
                        valor = u.cleanString(valor)
                        data[f.field] = valor
                    if(f.type=="substring"):
                        valor = row[f.index]
                        valor = valor[f.options:f.model]
                        data[f.field] = valor
                    elif(f.type=="number"):
                        valor = row[f.index]
                        valor = u.cleanNumber(valor)
                        data[f.field] = valor
                    elif(f.type=="numberdefault"):
                        valor = row[f.index]
                        valor = u.cleanNumber(valor)
                        if(valor > 0):
                            data[f.field] = valor
                        else:
                            data[f.field] = f.options
                    elif(f.type=="many2one"):
                        valor = row[f.index]
                        if(f.options=="Create"):
                            id = u.getIdCreate(valor, f.model, f.compare, c)
                        else:
                            id = u.getIdNoCreate(valor, f.model, f.compare, c)
                        data[f.field] = id
                    elif(f.type=="static"):
                        data[f.field] = f.options
                    elif(f.type=="many2onecompany"):
                        valor = row[f.index]
                        id = u.getIdNoCreateCompany(valor, f.model, f.compare, f.options, c)
                        data[f.field] = id
                    elif(f.type=="boolean"):
                        valor = row[f.index]
                        data[f.field] = u.strToBoolean(valor)
                    elif(f.type=="exclusiveboolean"):
                        valor = row[f.index]
                        data[f.field] = u.strToXBoolean(valor,f.model, f.options, f.compare)
                    elif(f.type=="selection"):
                        valor = row[f.index]
                        data[f.field] = u.selectionToString(valor, f.options, f.model)
                    elif(f.type in ["date","datetime"]):
                        valor = row[f.index]
                        data[f.field] = valor
                    elif(f.type=="many2many"):
                        data[f.field] = "[(6, 0, {})]".format(f.index)
                    elif(f.type=="many2many_selection"):
                        valor = row[f.index]
                        formated_dict = u.selectionToString(valor, f.options)
                        data[f.field] = [(6, 0, formated_dict)]
                    elif(f.type == "many2many_comas"):
                        valor = row[f.index]
                        formated_dict = u.csvToMany2many(valor, f.model, f.options, c)
                        data[f.field] = [(6, 0, formated_dict)]
                    elif(f.type=="options"):
                        valor = row[f.index]
                        opciones = f.options
                        for o in opciones:
                            if(valor == o['opcion']):
                                valor = o['valor']
                                break
                        data[f.field] = valor
                        
                try:
                    skip = False
                    for const in constraints:
                        if (const[0] == "unique"):
                            if(u.existsInModel(model, const[1], data[const[1]], c)):
                                print("El dato {} ya existe en la base".format(data[const[1]]))
                                u.writeError("Línea {} unque constraint: {}".format(contador, data[const[1]]))
                                skip = True
                        if (const[0] == "equal"):
                            if(u.checkNotEqual(const[1][1], data[const[1][0]])):
                                print("El dato {} no es igual a {}".format(data[const[1]], const[1]))
                                u.writeError("El dato {} no es igual a {}".format(data[const[1]], const[1]))
                                skip = True
                        if (const[0] == "not_equal"):
                            if(u.checkEqual(const[1][1], data[const[1][0]])):
                                print("El dato {} es igual a {}".format(data[const[1]], const[1]))
                                u.writeError("El dato {} es igual a {}".format(data[const[1]], const[1]))
                                skip = True
                        if (const[0] == "in"):
                            if(u.checkNotIn(const[1][1], data[const[1][0]])):
                                print("El dato {} no está en {}".format(data[const[1]], const[1]))
                                u.writeError("El dato {} no está en {}".format(data[const[1]], const[1]))
                                skip = True
                        if (const[0] == "not_in"):
                            if(u.checkIn(const[1][1], data[const[1][0]])):
                                print("El dato {} está en {}".format(data[const[1]], const[1]))
                                u.writeError("El dato {} está en {}".format(data[const[1]], const[1]))
                                skip = True
                        if (const[0] == "not_null"):
                            if(not data[const[1]] or data[const[1]]=="" or data[const[1]]==0):
                                print("El dato {} no puede estar vacío".format(data[const[1]]))
                                u.writeError("El dato {} no puede estar vacío".format(data[const[1]]))
                                skip = True
                    if not skip:
                        created = origin_class.create(data)
                        print("Created {}".format(created))
                except Exception as e:
                    u.writeError("Línea {} error: {}".format(contador, e))
                    print("Línea {} error: {}".format(contador, e))
                    
    def doubleupload(self, model, formatlist, model2, formatlist2, start, end, filename):
        conn_obj = connection.connection()
        c = conn_obj.getConnection()
        inicial = start
        final = end
        contador = 0    
        print("Sesion iniciada {}".format(c))
        origin_class = c.env[model]
        second_class = c.env[model2]
        u=utilities.utilities()
        with open(os.path.join(sys.path[0], "datafiles/{}".format(filename))) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')    
            for row in csv_reader:
                contador += 1
                print("Row {}".format(contador))
                if(contador < inicial):
                    continue
                elif(contador >= final):
                    break
                data = {}
                for f  in formatlist:
                    if(f.type=="string"):
                        valor = row[f.index]
                        valor = u.cleanString(valor)
                        data[f.field] = valor
                    elif(f.type=="number"):
                        valor = row[f.index]
                        valor = u.cleanNumber(valor)
                        data[f.field] = valor
                    elif(f.type=="many2one"):
                        valor = row[f.index]
                        if(f.options=="Create"):
                            id = u.getIdCreate(valor, f.model, f.compare, c)
                        else:
                            id = u.getIdNoCreate(valor, f.model, f.compare, c)
                        data[f.field] = id
                    elif(f.type=="many2onecompany"):
                        valor = row[f.index]
                        id = u.getIdNoCreateCompany(valor, f.model, f.compare, f.options, c)
                        data[f.field] = id
                    elif(f.type=="static"):
                        data[f.field] = f.options
                    elif(f.type in ["date","datetime"]):
                        valor = row[f.index]
                        data[f.field] = valor
                    elif(f.type=="many2many"):
                        data[f.field] = "[(4, {}, 0)]".format(f.index)
                    elif(f.type=="options"):
                        valor = row[f.index]
                        opciones = f.options
                        for o in opciones:
                            if(valor == o['opcion']):
                                valor = o['valor']
                                break
                        data[f.field] = valor
                        
                try:
                    created = origin_class.create(data)
                    print("Created {}".format(created))
                    data2 = {}
                    for f in formatlist2:
                        if(f.type=="string"):
                            valor = row[f.index]
                            valor = u.cleanString(valor)
                            data2[f.field] = valor
                        elif(f.type=="number"):
                            valor = row[f.index]
                            valor = u.cleanNumber(valor)
                            data2[f.field] = valor
                        elif(f.type=="result"):
                            valor = created
                            data2[f.field] = valor
                        elif(f.type=="many2one"):
                            valor = row[f.index]
                            if(f.options=="Create"):
                                id = u.getIdCreate(valor, f.model, f.compare, c)
                            else:
                                id = u.getIdNoCreate(valor, f.model, f.compare, c)
                            data2[f.field] = id
                        elif(f.type=="many2onecompany"):
                            valor = row[f.index]
                            id = u.getIdNoCreateCompany(valor, f.model, f.compare, f.options, c)
                            data2[f.field] = id
                        elif(f.type=="static"):
                            data2[f.field] = f.options
                        elif(f.type in ["date","datetime"]):
                            valor = row[f.index]
                            data2[f.field] = valor
                        elif(f.type=="many2many"):
                            data2[f.field] = "[(4, {}, 0)]".format(f.index)
                        elif(f.type=="options"):
                            valor = row[f.index]
                            opciones = f.options
                            for o in opciones:
                                if(valor == o['opcion']):
                                    valor = o['valor']
                                    break
                            data2[f.field] = valor
                    result2 = second_class.create(data2)
                    print("Created {}".format(result2))
                except Exception as e:
                    u.writeError("Línea {} error: {}".format(contador, e))
                    print("Línea {} error: {}".format(contador, e))


class updater():
    def update(self, model, formatlist, start, end, filename, id_column, id_type, compare, constraints=[]):
        conn_obj = connection.connection()
        c = conn_obj.getConnection()
        inicial = start
        final = end
        contador = 0    
        print("Sesion iniciada {}".format(c))
        origin_class = c.env[model]
        u=utilities.utilities()
        with open(os.path.join(sys.path[0], "datafiles/{}".format(filename))) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')    
            for row in csv_reader:
                contador += 1
                print("Row {}".format(contador))
                if(contador < inicial):
                    continue
                elif(contador >= final):
                    break
                id = ""
                if(id_type == "string"):
                    id = row[id_column]
                if(id_type == "many2one"):
                    id = u.getIdNoCreate(row[id_column], model, compare, c)
                if(id==""):
                    print("El dato {} no fue encontrado en el modelo de referencia".format(row[id_column]))
                    u.writeError("El dato {} no fue encontrado en el modelo de referencia".format(row[id_column]))
                data = {}
                for f  in formatlist:
                    if(f.type=="string"):
                        valor = row[f.index]
                        valor = u.cleanString(valor)
                        data[f.field] = valor
                    elif(f.type=="number"):
                        valor = row[f.index]
                        valor = u.cleanNumber(valor)
                        data[f.field] = valor
                    elif(f.type=="many2one"):
                        valor = row[f.index]
                        if(f.options=="Create"):
                            id = u.getIdCreate(valor, f.model, f.compare, c)
                        else:
                            id = u.getIdNoCreate(valor, f.model, f.compare, c)
                        data[f.field] = id
                    elif(f.type=="static"):
                        data[f.field] = f.options
                    elif(f.type=="many2onecompany"):
                        valor = row[f.index]
                        id = u.getIdNoCreateCompany(valor, f.model, f.compare, f.options, c)
                        data[f.field] = id
                    elif(f.type=="boolean"):
                        valor = row[f.index]
                        data[f.field] = u.strToBoolean(valor)
                    elif(f.type=="exclusiveboolean"):
                        valor = row[f.index]
                        data[f.field] = u.strToXBoolean(valor,f.model, f.options, f.compare)
                    elif(f.type=="selection"):
                        valor = row[f.index]
                        data[f.field] = u.selectionToString(valor, f.options, f.model)
                    elif(f.type in ["date","datetime"]):
                        valor = row[f.index]
                        data[f.field] = valor
                    elif(f.type=="many2many"):
                        valor = row[f.index]
                        data[f.field] = "[(4, {}, 0)]".format(valor)
                    elif(f.type=="many2many_search"):
                        valor = row[f.index]
                        field_id = u.getIdNoCreate(valor, f.model, f.compare, c)
                        data[f.field] = "[(4, {}, 0)]".format(field_id)
                    elif(f.type=="many2many_selection"):
                        valor = row[f.index]
                        formated_dict = u.selectionToString(valor, f.options)
                        data[f.field] = [(6, 0, formated_dict)]
                    elif(f.type == "many2many_comas"):
                        valor = row[f.index]
                        formated_dict = u.csvToMany2many(valor, f.model, f.options, c)
                        data[f.field] = [(6, 0, formated_dict)]
                    elif(f.type=="options"):
                        valor = row[f.index]
                        opciones = f.options
                        for o in opciones:
                            if(valor == o['opcion']):
                                valor = o['valor']
                                break
                        data[f.field] = valor   
                try:
                    skip = False
                    for const in constraints:
                        if (const[0] == "unique"):
                            if(u.existsInModel(model, const[1], data[const[1]], c)):
                                print("El dato {} ya existe en la base".format(data[const[1]]))
                                u.writeError("Línea {} unque constraint: {}".format(contador, data[const[1]]))
                                skip = True
                        if (const[0] == "equal"):
                            if(u.checkNotEqual(const[1][1], data[const[1][0]])):
                                print("El dato {} no es igual a {}".format(data[const[1]], const[1]))
                                u.writeError("El dato {} no es igual a {}".format(data[const[1]], const[1]))
                                skip = True
                        if (const[0] == "not_equal"):
                            if(u.checkEqual(const[1][1], data[const[1][0]])):
                                print("El dato {} es igual a {}".format(data[const[1]], const[1]))
                                u.writeError("El dato {} es igual a {}".format(data[const[1]], const[1]))
                                skip = True
                        if (const[0] == "in"):
                            if(u.checkNotIn(const[1][1], data[const[1][0]])):
                                print("El dato {} no está en {}".format(data[const[1]], const[1]))
                                u.writeError("El dato {} no está en {}".format(data[const[1]], const[1]))
                                skip = True
                        if (const[0] == "not_in"):
                            if(u.checkIn(const[1][1], data[const[1][0]])):
                                print("El dato {} está en {}".format(data[const[1]], const[1]))
                                u.writeError("El dato {} está en {}".format(data[const[1]], const[1]))
                                skip = True
                        if (const[0] == "not_null"):
                            if(not data[const[1]] or data[const[1]]=="" or data[const[1]]==0):
                                print("El dato {} no puede estar vacío".format(data[const[1]]))
                                u.writeError("El dato {} no puede estar vacío".format(data[const[1]]))
                                skip = True
                    if not skip:
                        print(type(data))
                        updated = origin_class.write([id], data)
                        print("Updated {}".format(updated))
                except Exception as e:
                    u.writeError("Línea {} error: {}".format(contador, e))
                    print("Línea {} error: {}".format(contador, e))