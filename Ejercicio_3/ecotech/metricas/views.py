from django.shortcuts import render
from .funcs import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1200.0},
        {"planta": "Planta Sur", "consumo_kwh": 800.5},
        {"planta": "Planta Norte", "consumo_kwh": 450.0},
        {"planta": "Planta Este", "consumo_kwh": 1500.0},
        {"planta": "Planta Sur", "consumo_kwh": 300.0},
    ]
 
    metricas = obtener_metricas_consumo(registros)
 
    contexto = {
        "titulo": "Panel de Sustentabilidad - EcoTech Solutions",
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "consumo_mayor_kwh": metricas["consumo_mayor_kwh"],
        "consumo_por_planta": metricas["consumo_por_planta"],
    }
 
    return render(request, "sustentabilidad/panel.html", contexto)
