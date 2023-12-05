import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__(self, nombre, trabajo, edad):
        self.nombre = self.obtener_nombre(nombre)
        self.trabajo = self.obtener_trabajo(trabajo)
        self.edad = self.obtener_edad(edad)

    def obtener_nombre(self, nombre):
        while True:
            if 4 <= len(nombre) <= 16 and  nombre.isalpha():
                return nombre
            else:
                if not (4 <= len(nombre) <= 16):
                    return "El nombre debe tener entre 4 y 16 letras. Inténtalo de nuevo."
                if not nombre.isalpha():
                    return "El nombre solo puede contener letras. Inténtalo de nuevo."

    def obtener_trabajo(self, trabajo):
        while True:
            if trabajo.isalpha():
                return trabajo
            else:
                return "El trabajo solo puede contener letras. Inténtalo de nuevo."

    def obtener_edad(self, edad):
        while True:
            if 1 <= len(edad) <= 2 and edad.isdigit():
                return edad
            else:
                if not (1 <= len(edad) <= 2):
                    return "La edad debe tener máximo 2 dígitos. Inténtalo de nuevo."
                if not edad.isdigit():
                    return "La edad puede contener números. Inténtalo de nuevo."

def main():
    usuario_objeto = Usuario()
    
    print("Nombre:", usuario_objeto.nombre)
    print("Trabajo:", usuario_objeto.trabajo)
    print("Edad:", usuario_objeto.edad)

if __name__ == "__main__":
    main()