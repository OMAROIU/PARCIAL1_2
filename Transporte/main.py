# main.py
from gestor import GestorUsuarios

def menu():
    print("\n" + "="*40)
    print("--SISTEMA DE REGISTRO DE VIAJES--")
    print("="*40)
    print("1. Registrar un nuevo usuario")
    print("2. Registrar un viaje")
    print("3. Mostrar viajes de un usuario")
    print("4. Mostrar resumen de un usuario")
    print("5. Listar usuarios")
    print("6. Salir")
    print("="*40)

def validar_numero(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

def main():
    gestor = GestorUsuarios()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            gestor.agregar_usuario(nombre)
            print(f"Usuario '{nombre}' registrado.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = gestor.agregar_usuario(nombre)
            ruta = input("Ingrese la ruta del viaje: ")
            dia = input("Ingrese el día del viaje: ")
            costo = validar_numero("Ingrese el costo del viaje ($): ", float)
            tiempo = validar_numero("Ingrese el tiempo del viaje (min): ", int)
            usuario.agregar_viaje(ruta, costo, tiempo, dia)
            print("Viaje registrado con éxito.")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            if nombre in gestor.usuarios:
                criterio = input("Ordenar por (costo/tiempo): ").lower()
                gestor.usuarios[nombre].mostrar_viajes(criterio)
            else:
                print(" Usuario no encontrado.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del usuario: ")
            if nombre in gestor.usuarios:
                gestor.usuarios[nombre].resumen()
            else:
                print("Usuario no encontrado.")

        elif opcion == "5":
            gestor.listar_usuarios()

        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()

