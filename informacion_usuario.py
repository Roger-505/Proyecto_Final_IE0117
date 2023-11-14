def usuario():

    while True:
        nombre = input("Por favor, ingresa tu nombre: ")
        if 4 <= len(nombre) <= 16 and nombre.isalpha():
            break
        else:
            if not (4 <= len(nombre) <= 16):
                print("El nombre debe tener entre 4 y 16 letras. Inténtalo de nuevo.")
            if not nombre.isalpha():
                print("El nombre solo puede contener letras. Inténtalo de nuevo.")

    while True:
        trabajo = input("¿Cuál es tu trabajo? ")
        if trabajo.isalpha():
            break
        else:
            print("El trabajo solo puede contener letras. Inténtalo de nuevo.")

    while True:
        edad = input("¿Cuántos años tienes? ")
        if 1 <= len(edad) <= 2 and edad.isdigit():
            break
        else:

            if not (1 <= len(edad) <= 2):
                print("La edad debe tener máximo 2 dígitos. Inténtalo de nuevo.")
            if not edad.isdigit():
                print("La edad puede contener números. Inténtalo de nuevo.")

    return nombre, trabajo, edad


def main():
    nombre, trabajo, edad = usuario()
    print("Nombre:", nombre)
    print("Trabajo:", trabajo)
    print("Edad:", edad)


main()
