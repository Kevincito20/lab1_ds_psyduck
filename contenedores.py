def registrar_contenedor(contenedores, id, llenado, temperatura, uso):
    if id in contenedores:
        return "Error: el contenedor ya existe."
    contenedores[id] = {
        "llenado": llenado,
        "temperatura": temperatura,
        "uso": uso
    }
    return "Contenedor registrado."

def actualizar_contenedor(contenedores, id, llenado=None, temperatura=None, uso=None):
    if id not in contenedores:
        return "Error: el contenedor no existe."
    if llenado is not None:
        contenedores[id]["llenado"] = llenado
    if temperatura is not None:
        contenedores[id]["temperatura"] = temperatura
    if uso is not None:
        contenedores[id]["uso"] = uso
    return "Contenedor actualizado."

def consultar_contenedor(contenedores, id):
    if id not in contenedores:
        return "Error: el contenedor no existe."
    datos = contenedores[id]
    return f"ID: {id}, Llenado: {datos['llenado']}%, Temp: {datos['temperatura']}°C, Uso: {datos['uso']} aperturas/día"
