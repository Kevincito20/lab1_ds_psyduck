class Reportes:

    def __init__(self, gestor):
        self.gestor = gestor

    def reporte_general(self):
        if not self.gestor.contenedores:
            return "No hay contenedores registrados."
        reporte = ""
        for contenedor in self.gestor.contenedores.values():
            reporte += contenedor.mostrar_info() + "\n" + "-"*30 + "\n" #se muestra la informacion de cada contenedor y se separa con una linea con 30 guiones
        return reporte

    def estadisticas_ciudad(self):
        if not self.gestor.contenedores:
            return "No hay contenedores registrados."

        contenedores = list(self.gestor.contenedores.values())
        # FUNCIONES LAMBDA PARA CALCULAR ESTADISTICAS DE LLENADO Y USO
        mas_lleno = max(contenedores, key=lambda c: c.llenado) 
        mas_usado = max(contenedores, key=lambda c: c.frecuencia_uso)
        suma = 0
        for c in contenedores:
            suma += c.llenado

        promedio_llenado = suma / len(contenedores) 

        return (f"Contenedor más lleno: {mas_lleno.id} ({mas_lleno.llenado}%)\n"
                f"Contenedor con mayor uso: {mas_usado.id} ({mas_usado.frecuencia_uso} aperturas/día)\n"
                f"Promedio de llenado de la ciudad: {promedio_llenado:.2f}%")
