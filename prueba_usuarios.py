from usuario import Usuario


def main():
    while True:
        print("\nWelcome to the User Management System")
        print("1. Registro")
        print("2. Inicio de sesión")
        print("3. Cambio de contraseña")
        print("4. Darse de baja")
        print("5. Ingresar dinero")
        print("6. Retirar dinero")
        print("7. Salir")
        choice = input("Opción: ")

        if choice == '1':
            dni = input("Introduce DNI/NIE: ")
            nombre = input("Introduce nombre: ")
            apellidos = input("Introduce apellidos: ")
            contrasena = input("Introduce contraseña: ")
            if dni_nie_correcto(dni):
                usuario = Usuario(dni, nombre, apellidos, contrasena)
                usuario.guardar_en_bd()
            else:
                print("Introduzca un DNI/NIE válido")

        elif choice == '2':
            dni = input("Introduce dni: ")
            contrasena = input("Introduce contraseña: ")
            if Usuario.login(dni, contrasena):
                dni_usuario, dinero_usuario = Usuario.login(dni, contrasena)
                print(f"¡Bienvenido de nuevo!")
            else:
                print("DNI o contraseña incorrectos")

        # Inicio sesion previo
        elif choice == '3':
            cont_actual = input("Introduce contraseña actual: ")
            if Usuario.login(dni_usuario, cont_actual):
                nueva_cont = input("Introduce nueva contraseña: ")
                Usuario.cambiar_contrasena(dni_usuario, nueva_cont)
            else:
                print("Contraseña incorrecta")

        # Inicio sesion previo
        elif choice == '4':
            contrasena = input("Introduce contraseña: ")
            if Usuario.login(dni_usuario, contrasena):
                Usuario.eliminar_usuario(dni_usuario)
            else:
                print("Contraseña incorrecta")

        # Inicio sesion previo
        elif choice == '5':
            try:
                ingreso = int(input("Cantidad a ingresar (euros): "))
            except ValueError:
                print("Ingrese una cantidad válida (sin decimales).")
            else:
                dinero_usuario += ingreso
                Usuario.actualizar_dinero(dni_usuario, dinero_usuario)

        # Inicio sesion previo
        elif choice == '6':
            try:
                retirada = int(input("Cantidad a retirar (euros): "))
            except ValueError:
                print("Ingrese una cantidad válida (sin decimales).")
            else:
                if dinero_usuario >= retirada:
                    dinero_usuario -= retirada
                    Usuario.actualizar_dinero(dni_usuario, dinero_usuario)
                else:
                    print("No dispone de tanto dinero para retirar.")
                    print(f"Capital actual: {dinero_usuario} euros.")

        elif choice == '7':
            print("Saliendo...")
            break

        else:
            print("Opción no válida")


import re
def dni_nie_correcto(dni):
    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
              'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    dni_valido = re.search('^\d{8}[A-Z]$', dni)
    nie_valido = re.search('^[X-Z]\d{7}[A-Z]$', dni)
    if dni_valido:
        valido = dni_valido
        sin_letra = valido[0][:-1]
        resto = int(sin_letra) % 23
        if (sin_letra + letras[resto]) == valido[0]:
            print('true')
            return True
        else:
            print('false')
            return False
    elif nie_valido:
        valido = nie_valido
        sin_letra = valido[0][0:-1]
        resto = int(sin_letra[1:]) % 23
        if (sin_letra + letras[resto]) == valido[0]:
            print('true')
            return True
        else:
            print('false')
            return False
    else:
        return False


main()