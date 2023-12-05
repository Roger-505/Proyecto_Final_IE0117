import tkinter as tk
from tkinter import messagebox
from informacion_usuario import Usuario
from logica_preguntas import Juego_preguntas

class Millionario:
    def __init__(self, root):
        self.root = root
        self.root.title("¿Quién Quiere Ser Millonario?")
        self.root.geometry("400x300")

        self.menu()

    def menu(self):
        label = tk.Label(self.root, text="Bienvenido al juego", font=("Arial", 18))
        label.pack(pady=20)

        botón_iniciar= tk.Button(self.root, text="Iniciar Partida", command=self.iniciar_juego)
        botón_iniciar.pack()

    def iniciar_juego(self):
        usuario = self.obtener_info_usuario()
        if usuario:
            self.root.destroy()  # Cerrar la ventana actual del menú principal
            self.iniciar_cuestionario(usuario)

    def obtener_info_usuario(self):
        # crear ventana para ingresar info de usuario
        ventana_usuario = tk.Toplevel(self.root)
        ventana_usuario.geometry("400x300")
        ventana_usuario.title("Información del Usuario")

        etiqueta = tk.Label(ventana_usuario, text="Nombre:")
        etiqueta.pack()
        info_nombre = tk.Entry(ventana_usuario)
        info_nombre.pack()

        info_trabajo = tk.Label(ventana_usuario, text="Trabajo:")
        info_trabajo.pack()
        info_trabajo = tk.Entry(ventana_usuario)
        info_trabajo.pack()

        info_edad = tk.Label(ventana_usuario, text="Edad:")
        info_edad.pack()
        info_edad = tk.Entry(ventana_usuario)
        info_edad.pack()

        botón_ingresar = tk.Button(ventana_usuario, text="Ingresar", command=lambda: self.desplegar_info_usuario(
            ventana_usuario, info_nombre.get(), info_trabajo.get(), info_edad.get()))
        botón_ingresar.pack()

        usuario = Usuario(info_nombre.get(), info_trabajo.get(), info_edad.get())

        return usuario

    def desplegar_info_usuario(self, ventana, nombre, trabajo, edad):
        usuario = Usuario(nombre, trabajo, edad)
        ventana_usuario = tk.Toplevel(self.root)

        # crear ventana para desplegar info de usuario
        ventana_usuario.geometry("400x300")
        ventana_usuario.title("Información del Usuario")
        datos = [usuario.nombre, usuario.trabajo, usuario.edad]

        etiqueta = tk.Label(ventana_usuario)
        lista = tk.Listbox(ventana_usuario, width = 70)
  
        for dato in datos:
            lista.insert(tk.END, dato)
        lista.pack()
        
        aceptar = tk.Button(ventana_usuario, text="Ok", command=ventana_usuario.destroy)
        aceptar.pack()

    def iniciar_cuestionario(self, user):
        # Iniciar el juego con la información del usuario
        # Por ejemplo:
        archivos_preguntas = ["Nivel_1.txt", "Nivel_2.txt", "Nivel_3.txt",
                              "Nivel_4.txt", "Nivel_5.txt", "Nivel_6.txt", "Nivel_7.txt"]
        print("HOLA")
        juego= Juego_preguntas(archivos_preguntas)
        # Llamar a la función para comenzar a mostrar las preguntas
        juego.jugar()


def main():
    root = tk.Tk()
    app = Millionario(root)
    root.mainloop()

if __name__ == "__main__":
    main()