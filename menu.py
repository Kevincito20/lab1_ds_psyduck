#Este modulo es para la gestion de la interfaz del menu interactivo
from contenedores import registrar_contenedor, actualizar_contenedor, consultar_contenedor
from reportes import reporte_general, estadisticas_generales

def mostrar_menu():
    contenedores = {}
    while True:
        print("\n1. Registrar contenedor")
        print("2. Actualizar contenedor")
        print("3. Consultar contenedor")
        print("4. Reporte general")
        print("5. Estadísticas generales")
        print("6. Salir")
        try:
            opcion = int(input("Seleccione opción: "))
            if opcion == 1:
                id = input("ID: ")
                llenado = int(input("Llenado (%): "))
                temperatura = float(input("Temperatura (°C): "))
                uso = int(input("Aperturas/día: "))
                print(registrar_contenedor(contenedores, id, llenado, temperatura, uso))
            elif opcion == 2:
                id = input("ID: ")
                llenado = int(input("Llenado (%): "))
                temperatura = float(input("Temperatura (°C): "))
                uso = int(input("Aperturas/día: "))
                print(actualizar_contenedor(contenedores, id, llenado, temperatura, uso))
            elif opcion == 3:
                id = input("ID: ")
                print(consultar_contenedor(contenedores, id))
            elif opcion == 4:
                print(reporte_general(contenedores))
            elif opcion == 5:
                print(estadisticas_generales(contenedores))
            elif opcion == 6:
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error de entrada:", e)


if __name__ == "__main__":
    mostrar_menu()
