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
        "sensor_id": " SENSOR ",
        "temperatura": "35.8C"
    }
]

sensores_limpios = []

for registro in sensores_raw:
    registro_limpio = limpiar_registro_sensor(registro)
    sensores_limpios.append(registro_limpio)
