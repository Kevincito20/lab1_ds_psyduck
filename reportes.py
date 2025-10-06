def reporte_general(contenedores):
    resultado = []
    for id, datos in contenedores.items():
        resultado.append(f"ID: {id}, Llenado: {datos['llenado']}%, Temp: {datos['temperatura']}°C, Uso: {datos['uso']} aperturas/día")
    return "\n".join(resultado) if resultado else "No hay contenedores registrados."

def estadisticas_generales(contenedores):
    if not contenedores:
        return "No hay contenedores registrados."
    max_llenado = max(contenedores.items(), key=lambda x: x[1]['llenado'])
    max_uso = max(contenedores.items(), key=lambda x: x[1]['uso'])
    promedio_llenado = sum(datos['llenado'] for datos in contenedores.values()) / len(contenedores)
    return (
        f"Contenedor más lleno: {max_llenado[0]} ({max_llenado[1]['llenado']}%)\n"
        f"Contenedor con mayor uso: {max_uso[0]} ({max_uso[1]['uso']} aperturas/día)\n"
        f"Promedio de llenado: {promedio_llenado:.2f}%"
    )
