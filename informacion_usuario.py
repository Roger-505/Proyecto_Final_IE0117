class Usuario:
    def __init__(self):
        self.nombre = self.obtener_nombre()
        self.trabajo = self.obtener_trabajo()
        self.edad = self.obtener_edad()

    def obtener_nombre(self):
        while True:
            nombre = input("Por favor, ingresa tu nombre: ")
            if 4 <= len(nombre) <= 16 and nombre.isalpha():
                return nombre
            else:
                if not (4 <= len(nombre) <= 16):
                    print("El nombre debe tener entre 4 y 16 letras. Inténtalo de nuevo.")
                if not nombre.isalpha():
                    print("El nombre solo puede contener letras. Inténtalo de nuevo.")

    def obtener_trabajo(self):
        while True:
            trabajo = input("¿Cuál es tu trabajo? ")
            if trabajo.isalpha():
                return trabajo
            else:
                print("El trabajo solo puede contener letras. Inténtalo de nuevo.")

    def obtener_edad(self):
        while True:
            edad = input("¿Cuántos años tienes? ")
            if 1 <= len(edad) <= 2 and edad.isdigit():
                return edad
            else:
                if not (1 <= len(edad) <= 2):
                    print("La edad debe tener máximo 2 dígitos. Inténtalo de nuevo.")
                if not edad.isdigit():
                    print("La edad puede contener números. Inténtalo de nuevo.")
