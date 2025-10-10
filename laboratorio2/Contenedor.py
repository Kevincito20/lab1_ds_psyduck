#Kevin Linares, Isalleth Sanchez, Adrian Romero, Alex Hernández
'''
Creamos 2 clases: Contenedor y GestorContenedores.
La clase Contenedor maneja los datos individuales de cada contenedor,
mientras que GestorContenedores maneja la colección de contenedores y
sus operaciones.
'''
class Contenedor:

    def __init__(self, id_contenedor, llenado=0, temperatura=25, frecuencia_uso=0):
        self.id = id_contenedor
        self.llenado = llenado
        self.temperatura = temperatura
        self.frecuencia_uso = frecuencia_uso

    def actualizar_datos(self, llenado=None, temperatura=None, frecuencia_uso=None):
        if llenado is not None:
            self.llenado = llenado
        if temperatura is not None:
            self.temperatura = temperatura
        if frecuencia_uso is not None:
            self.frecuencia_uso = frecuencia_uso

    def mostrar_info(self):
        return (f"ID: {self.id}\n"
                f"Llenado: {self.llenado}%\n"
                f"Temperatura: {self.temperatura}°C\n"
                f"Frecuencia de uso: {self.frecuencia_uso} aperturas/día")


class GestorContenedores:
    
    def __init__(self):
        self.contenedores = {}  

    def registrar_contenedor(self, contenedor):
        if contenedor.id in self.contenedores:
            raise ValueError(f"El contenedor {contenedor.id} ya existe.")
        self.contenedores[contenedor.id] = contenedor

    def actualizar_contenedor(self, id_contenedor, llenado=None, temperatura=None, frecuencia_uso=None):
        if id_contenedor not in self.contenedores:
            raise KeyError(f"El contenedor {id_contenedor} no existe.")
        self.contenedores[id_contenedor].actualizar_datos(llenado, temperatura, frecuencia_uso)

    def consultar_contenedor(self, id_contenedor):
        if id_contenedor not in self.contenedores:
            raise KeyError(f"El contenedor {id_contenedor} no existe.")
        return self.contenedores[id_contenedor].mostrar_info()
    

