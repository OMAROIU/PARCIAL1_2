# viaje.py
class Viaje:
    def __init__(self, ruta, costo, tiempo, dia):
        self.ruta = ruta
        self.costo = costo
        self.tiempo = tiempo
        self.dia = dia

    def __str__(self):
        return (f"Ruta: {self.ruta} | Día: {self.dia} | "
                f"Costo: ${self.costo:.2f} | Tiempo: {self.tiempo} min")
