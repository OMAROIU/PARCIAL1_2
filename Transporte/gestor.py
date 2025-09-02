# gestor.py
from usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, nombre):
        if nombre not in self.usuarios:
            self.usuarios[nombre] = Usuario(nombre)
        return self.usuarios[nombre]

    def listar_usuarios(self):
        if not self.usuarios:
            print("\n⚠ No hay usuarios registrados.")
            return
        print("\n--- Usuarios registrados ---")
        for i, nombre in enumerate(self.usuarios.keys(), start=1):
            print(f"{i}. {nombre}")
