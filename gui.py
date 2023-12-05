import tkinter as tk
from tkinter import messagebox
from informacion_usuario import Usuario
from logica_preguntas import Juego_preguntas, center
import time 

class Millionario:
    def __init__(self, root):
        self.root = root
        self.root.title("¿Quién quiere ser millonario?")
        self.root.geometry("400x300")
        center(self.root)
        self.menu()

    def menu(self):
        label = tk.Label(self.root, text="Bienvenido a \n ¿Quién Quiere ser Millionario?", font=("Arial", 18))
        label.pack(pady=20)
        
        botón_iniciar= tk.Button(self.root, text="Iniciar Partida", command=self.iniciar_cuestionario)
        botón_iniciar.pack()
        botón_iniciar= tk.Button(self.root, text="Ingresar información del usuario", command=self.obtener_info_usuario)
        botón_iniciar.pack()

    def obtener_info_usuario(self):
        # crear ventana para ingresar info de usuario
        ventana_usuario = tk.Toplevel(self.root)
        ventana_usuario.geometry("400x300")
        center(ventana_usuario)
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


        botón_ingresar = tk.Button(ventana_usuario, text="Ingresar", command=lambda: self.desplegar_info_usuario(ventana_usuario, info_nombre.get(), info_trabajo.get(), info_edad.get()))
        botón_ingresar.pack()

        usuario = Usuario(info_nombre.get(), info_trabajo.get(), info_edad.get())

        return usuario

    def desplegar_info_usuario(self, ventana, nombre, trabajo, edad):
        usuario = Usuario(nombre, trabajo, edad)
        ventana_usuario = tk.Toplevel(self.root)

        # crear ventana para desplegar info de usuario
        ventana_usuario.geometry("400x200")
        ventana_usuario.title("Información del Usuario")
        center(ventana_usuario)
        datos = [usuario.nombre, usuario.trabajo, usuario.edad]

        etiqueta = tk.Label(ventana_usuario)
        lista = tk.Listbox(ventana_usuario, width = 70)
  
        for dato in datos:
            lista.insert(tk.END, dato)
        lista.pack()
        
        aceptar = tk.Button(ventana_usuario, text="Ok", command=ventana_usuario.destroy)
        aceptar.pack()

        ventana.destroy()

    def iniciar_cuestionario(self):
        
        archivos_preguntas = ["Nivel_1.txt", "Nivel_2.txt", "Nivel_3.txt",
                              "Nivel_4.txt", "Nivel_5.txt", "Nivel_6.txt", "Nivel_7.txt"]
        juego= Juego_preguntas(archivos_preguntas, self.root)
        juego.jugar()


def main():
    root = tk.Tk()
    app = Millionario(root)
    root.mainloop()

if __name__ == "__main__":
    main()