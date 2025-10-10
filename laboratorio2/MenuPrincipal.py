#Kevin Linares, Isalleth Sanchez, Adrian Romero, Alex Hernández
from Contenedor import Contenedor, GestorContenedores
from Reporte import Reportes

class Menu:
    def __init__(self):
        self.gestor = GestorContenedores()
        self.reportes = Reportes(self.gestor)

    def mostrar_menu(self):
        while True:
            print("\n Contenedores Inteligentes ")
            print("1. Registrar contenedor")
            print("2. Actualizar contenedor")
            print("3. Consultar contenedor")
            print("4. Reporte general")
            print("5. Estadísticas de la ciudad")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")
            self.procesar_opcion(opcion)

    def procesar_opcion(self, opcion):
        try:
            if opcion == "1":
                self.opcion_registrar()
            elif opcion == "2":
                self.opcion_actualizar()
            elif opcion == "3":
                self.opcion_consultar()
            elif opcion == "4":
                print(self.reportes.reporte_general())
            elif opcion == "5":
                print(self.reportes.estadisticas_ciudad())
            elif opcion == "6":
                print("Saliendo del programa...")
                exit()
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyError as ke:
            print(f"Error: {ke}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def opcion_registrar(self):
        id_contenedor = input("ID del contenedor: ")
        llenado = float(input("Nivel de llenado (%): "))
        temperatura = float(input("Temperatura (°C): "))
        frecuencia = int(input("Frecuencia de uso (aperturas/día): "))
        cont = Contenedor(id_contenedor, llenado, temperatura, frecuencia)
        self.gestor.registrar_contenedor(cont)
        print("Contenedor registrado con éxito.")

    def opcion_actualizar(self):
        id_contenedor = input("ID del contenedor a actualizar: ")
        llenado = float(input("Nuevo nivel de llenado (%): "))
        temperatura = float(input("Nueva temperatura (°C): "))
        frecuencia = int(input("Nueva frecuencia de uso: "))
        self.gestor.actualizar_contenedor(id_contenedor, llenado, temperatura, frecuencia)
        print("Contenedor actualizado con éxito.")

    def opcion_consultar(self):
        id_contenedor = input("ID del contenedor a consultar: ")
        info = self.gestor.consultar_contenedor(id_contenedor)
        print(info)
