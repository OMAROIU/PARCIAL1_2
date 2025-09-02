# usuario.py
from viaje import Viaje

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.viajes = []

    def agregar_viaje(self, ruta, costo, tiempo, dia):
        self.viajes.append(Viaje(ruta, costo, tiempo, dia))

    def mostrar_viajes(self, criterio="costo"):
        if not self.viajes:
            print(f"\n⚠ {self.nombre} no tiene viajes registrados.")
            return

        if criterio == "costo":
            viajes_ordenados = sorted(self.viajes, key=lambda x: x.costo, reverse=True)
            print(f"\n--- Viajes de {self.nombre} (ordenados por costo) ---")
        else:
            viajes_ordenados = sorted(self.viajes, key=lambda x: x.tiempo, reverse=True)
            print(f"\n--- Viajes de {self.nombre} (ordenados por tiempo) ---")

        for i, v in enumerate(viajes_ordenados, start=1):
            print(f"{i}. {v}")

    def resumen(self):
        if not self.viajes:
            print(f"\n⚠ No hay datos de viajes para {self.nombre}.")
            return

        total_costo = sum(v.costo for v in self.viajes)
        total_tiempo = sum(v.tiempo for v in self.viajes)
        promedio_costo = total_costo / len(self.viajes)
        promedio_tiempo = total_tiempo / len(self.viajes)

        viaje_caro = max(self.viajes, key=lambda x: x.costo)
        viaje_barato = min(self.viajes, key=lambda x: x.costo)

        print(f"\n===== RESUMEN DE {self.nombre.upper()} =====")
        print(f"Total de viajes: {len(self.viajes)}")
        print(f"Gasto total: ${total_costo:.2f}")
        print(f"Tiempo total: {total_tiempo} minutos")
        print(f"Promedio gasto por viaje: ${promedio_costo:.2f}")
        print(f"Promedio tiempo por viaje: {promedio_tiempo:.2f} min")
        print(f"➡ Viaje más caro: {viaje_caro}")
        print(f"➡ Viaje más barato: {viaje_barato}")
        print("=================================")
