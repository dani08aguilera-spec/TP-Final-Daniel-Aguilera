def limpiar_registro_sensor(registro_raw: dict[str, str]):

    sensor_id = registro_raw["sensor_id"].strip()

    temperatura = float(registro_raw["temperatura"]
                        .replace("°C", "")
                        .replace("C", "")
                        .strip()
                        )

    ubicacion = registro_raw.get("ubicacion", "").strip()

    if ubicacion == "":
        ubicacion = "Ubicación desconocida"

    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

    return registro_limpio

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):

    lista_sensores_alerta = []
    suma_temperaturas = 0

    for sensor in lista_sensores_limpios:

        temperatura = sensor["temperatura"]
        sensor_id = sensor["sensor_id"]

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor_id)

        suma_temperaturas += temperatura

    if len(lista_sensores_limpios) > 0:
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    else:
        promedio_temperatura = 0

    return lista_sensores_alerta, promedio_temperatura

sensores_raw = [
    {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C",
        "ubicacion": "Planta Norte"
    },
    {
        "sensor_id": " SENSOR-002",
        "temperatura": "32.5C",
        "ubicacion": "Depósito"
    },
    {
        "sensor_id": "SENSOR-003 ",
        "temperatura": "25.3 °C",
        "ubicacion": "Laboratorio"
    },
    {
        "sensor_id": " SENSOR-004 ",
        "temperatura": "35.8C"
    }
]

sensores_limpios = []

for registro in sensores_raw:
    registro_limpio = limpiar_registro_sensor(registro)
    sensores_limpios.append(registro_limpio)

umbral = 30.0

sensores_alerta, promedio_global = generar_resumen_sensores(sensores_limpios, umbral)

# reporte final
for sensor in sensores_limpios:
    print(f"sensor: {sensor['sensor_id']} - temperatura: {sensor['temperatura']} - ubicación: {sensor['ubicacion']}")

print(f"Umbral establecido: {umbral}")
print(f"Promedio global: {promedio_global:.2f} °C")
print(f"Dispositivos en alerta (superan el umbral): {sensores_alerta}")