from django.shortcuts import render
from django.http import HttpRequest
from .funcs import obtener_metricas_consumo


def vista_panel_sustentabilidad(request: HttpRequest):
    registros_consumo = [
        {"planta": "Planta Norte", "consumo_kwh": 1200.0},
        {"planta": "Planta Sur", "consumo_kwh": 800.5},
        {"planta": "Planta Norte", "consumo_kwh": 450.0},
        {"planta": "Planta Este", "consumo_kwh": 1500.0},
        {"planta": "Planta Sur", "consumo_kwh": 300.0},
    ]

    metricas = obtener_metricas_consumo(registros_consumo)

    contexto = {"titulo": "Panel de Sustentabilidad", "metricas": metricas}
    return render(request, "sustentabilidad/panel.html", contexto)