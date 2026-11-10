def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")
 
    return consumo_kwh * factor_emision
 
 
def obtener_metricas_consumo(registros):

    total_emisiones = 0
    consumo_por_planta = {}
 
    for registro in registros:
        planta = registro["planta"]
        consumo = registro["consumo_kwh"]
 
        total_emisiones += calcular_emisiones_carbono(consumo)
 
        if planta in consumo_por_planta:
            consumo_por_planta[planta] += consumo
        else:
            consumo_por_planta[planta] = consumo
 
    if len(consumo_por_planta) > 0:
        planta_mayor_consumo = max(consumo_por_planta, key=consumo_por_planta.get)
        consumo_mayor_kwh = consumo_por_planta[planta_mayor_consumo]
    else:
        planta_mayor_consumo = None
        consumo_mayor_kwh = 0
 
    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "consumo_mayor_kwh": consumo_mayor_kwh,
        "consumo_por_planta": consumo_por_planta,
    }