def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")
 
    return consumo_kwh * factor_emision
 
 
def obtener_metricas_consumo(registros: list[dict]) -> dict:
    total_emisiones = 0
    consumo_por_planta = {}

    for registro in registros:
        try:
            emisiones = calcular_emisiones_carbono(registro["consumo_kwh"])
        except ValueError:
            continue  # registro con consumo negativo: se ignora

        total_emisiones += emisiones

        planta = registro["planta"]
        if planta in consumo_por_planta:
            consumo_por_planta[planta] += registro["consumo_kwh"]
        else:
            consumo_por_planta[planta] = registro["consumo_kwh"]

    desglose = []
    planta_mayor_consumo = None
    consumo_maximo = -1

    for planta, consumo in consumo_por_planta.items():
        desglose.append({
            "planta": planta,
            "consumo_kwh": consumo,
            "emisiones": round(calcular_emisiones_carbono(consumo), 2),
        })

        if consumo > consumo_maximo:
            consumo_maximo = consumo
            planta_mayor_consumo = planta

    return {
        "total_emisiones": round(total_emisiones, 2),
        "planta_mayor_consumo": planta_mayor_consumo,
        "desglose": desglose,
    }