# contenedores.py

def registrar_contenedor(contenedores, identificador, llenado, temperatura, frecuencia):
    if identificador in contenedores:
        return False, "Error: El contenedor ya existe."
    contenedores[identificador] = {
        "llenado": llenado,
        "temperatura": temperatura,
        "frecuencia": frecuencia
    }
    return True, "Contenedor registrado exitosamente."

def actualizar_contenedor(contenedores, identificador, llenado, temperatura, frecuencia):
    if identificador not in contenedores:
        return False, "Error: El contenedor no existe."
    contenedores[identificador]["llenado"] = llenado
    contenedores[identificador]["temperatura"] = temperatura
    contenedores[identificador]["frecuencia"] = frecuencia
    return True, "Datos actualizados exitosamente."

def consultar_contenedor(contenedores, identificador):
    if identificador not in contenedores:
        return False, "Error: El contenedor no existe."
    datos = contenedores[identificador]
    return True, f"ID: {identificador}\nLlenado: {datos['llenado']}%\nTemperatura: {datos['temperatura']}°C\nFrecuencia: {datos['frecuencia']} aperturas/día"
