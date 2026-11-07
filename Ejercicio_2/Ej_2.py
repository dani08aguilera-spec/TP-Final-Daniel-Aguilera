import json
from pathlib import Path
 
# Punto A: Dominio del catálogo y reglas de inventario

class StockInvalidoError(Exception):
    """Se lanza cuando el stock asignado es negativo, nulo o no numérico."""
    pass
 
 
class DispositivoEcológico:
    codigo: str
    nombre: str
    __stock: int
 
    def __init__(self, codigo: str, nombre: str, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock
 
    @property
    def stock(self):
        return self.__stock
 
    @stock.setter
    def stock(self, valor):
        try:
            if int(valor) < 0:
                raise StockInvalidoError("El valor a asignar en stock debe ser mayor o igual a 0")
            self.__stock = int(valor)
        except ValueError:
            raise StockInvalidoError("El tipo de dato a asignar en stock debe ser numérico")
        except TypeError:
            raise StockInvalidoError("El valor a asignar en stock no puede ser nulo")
 
    def ficha_tecnica(self, imprimir: bool = False) -> str:
        ficha = f"codigo: {self.codigo} | nombre: {self.nombre} | stock: {self.stock}"
 
        if imprimir:
            print(ficha)
        return ficha
 
    def to_dict(self):
        return {
            "tipo": type(self).__name__,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "stock": self.stock,
        }
 
 
class PanelSolar(DispositivoEcológico):
    potencia_watts: float
    eficiencia: float
 
    def __init__(self, codigo: str, nombre: str, stock: int, potencia_watts: float, eficiencia: float):
        super().__init__(codigo, nombre, stock)
        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia
 
    def ficha_tecnica(self, imprimir: bool = False) -> str:
        ficha = super().ficha_tecnica(imprimir=False)
        ficha += f" | potencia: {self.potencia_watts} W | eficiencia: {self.eficiencia}%"
 
        if imprimir:
            print(ficha)
        return ficha
 
    def to_dict(self):
        dict = super().to_dict()
        dict["potencia_watts"] = self.potencia_watts
        dict["eficiencia"] = self.eficiencia
 
        return dict



# Punto B: Persistencia y gestión del catálogo

class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos: list[DispositivoEcológico | PanelSolar], ruta_archivo: str) -> bool:
        """
        lista_dispositivos: lista de instancias ya creadas y válidas.
        ruta_archivo: ruta del archivo de salida, por ejemplo "catalogo_ecotech.json".
        """
        Path(ruta_archivo).parent.mkdir(parents=True, exist_ok=True)
 
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            lista_serializada = []
            for elemento in lista_dispositivos:
                lista_serializada.append(elemento.to_dict())
 
            json.dump(lista_serializada, archivo, indent=4, ensure_ascii=False)
 
        return True


try:
    dispositivo_erroneo = DispositivoEcológico("ECO-999", "Dispositivo inválido", -5)
except StockInvalidoError as e:
    print(f"Excepción capturada al instanciar un dispositivo con stock negativo: {e}")
 
# Dispositivos válidos
dispositivo_1 = DispositivoEcológico("ECO-001", "Controlador de Carga", 25)
panel_1 = PanelSolar("PS-001", "Panel Monocristalino 450W", 40, 450, 21.5)
panel_2 = PanelSolar("PS-002", "Panel Policristalino 330W", 15, 330, 17.8)
 
try:
    dispositivo_1.stock = -10
except StockInvalidoError as e:
    print(f"Excepción capturada al modificar el stock con un valor negativo: {e}")
print(f"El stock de {dispositivo_1.codigo} no cambió: {dispositivo_1.stock}")
 
lista_dispositivos = [dispositivo_1, panel_1, panel_2]
 
for dispositivo in lista_dispositivos:
    dispositivo.ficha_tecnica(imprimir=True)
 
if GestorInventario.guardar_catalogo_json(lista_dispositivos, "catalogo_ecotech.json"):
    print("Catálogo exportado correctamente a catalogo_ecotech.json")
