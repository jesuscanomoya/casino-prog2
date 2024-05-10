from usuario import Usuario


def main():
    while True:
        print("\nWelcome to the User Management System")
        print("1. Registro")
        print("2. Inicio de sesión")
        print("3. Cambio de contraseña")
        print("4. Darse de baja")
        print("5. Salir")
        choice = input("Opción: ")

        if choice == '1':
            dni = input("Introduce dni: ")
            nombre = input("Introduce nombre: ")
            apellidos = input("Introduce apellidos: ")
            contrasena = input("Introduce contraseña: ")
            usuario = Usuario(dni, nombre, apellidos, contrasena)
            usuario.guardar_en_bd()
        elif choice == '2':
            dni = input("Introduce dni: ")
            contrasena = input("Introduce contraseña: ")
            if Usuario.login(dni, contrasena):
                print("Inicio de sesión realizado")
            else:
                print("DNI o contraseña incorrectos")
        elif choice == '3':
            dni = input("Introduce dni: ")
            cont_actual = input("Introduce contraseña actual: ")
            if Usuario.login(dni, cont_actual):
                nueva_cont = input("Introduce nueva contraseña: ")
                Usuario.cambiar_contrasena(dni, nueva_cont)
            else:
                print("DNI o contraseña incorrectos")
        elif choice == '4':
            dni = input("Introduce dni: ")
            contrasena = input("Introduce contraseña: ")
            if Usuario.login(dni, contrasena):
                Usuario.eliminar_usuario(dni)
            else:
                print("DNI o contraseña incorrectos")
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")


main()
