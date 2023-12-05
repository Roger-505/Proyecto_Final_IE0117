import random
import time
import threading
import tkinter as tk
from comodines import Publico, Mitad, Cambio_pregunta
from tkinter import messagebox

class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
    
# Esta funcion es la encargada de procesar el archivo .txt que almacena las preguntas, opciones, respuestas correctas y devuelv una lista de tuplas con la información.
    def cargar_todas_las_preguntas(archivos_preguntas):
        todas_las_preguntas = []
        for archivo in archivos_preguntas:
            with open(archivo, 'r', encoding="utf8") as file:
                lines = file.readlines()

            i = 0
            preguntas_ronda = []
            while i < len(lines):
                pregunta = lines[i].strip()
                opciones = [lines[i+j].strip() for j in range(1, 5)]

# Estructura encargada de buscar la línea que contiene la respuesta correcta
                for j in range(1, 6):
                    if lines[i+j].startswith("CORRECTA:"):
                        respuesta_correcta = lines[i+j].split(': ')[1].strip()[0].upper()
                        break

                preguntas_ronda.append(Pregunta(pregunta, opciones, respuesta_correcta))
                i += 6    # Avanza al siguiente conjunto de pregunta y opciones

            todas_las_preguntas.append(preguntas_ronda)

        return todas_las_preguntas

        
# Clase que encapsula la logica del juego.

class Juego_preguntas:
    def __init__(self, archivos_preguntas, root):
        self.archivos_preguntas = archivos_preguntas
        self.rondas = 7
        self.preguntas = Pregunta.cargar_todas_las_preguntas(archivos_preguntas)
        self.comodines = ["Mitad","Público","Cambiar pregunta"]
        self.root = root

    def mostrar_pregunta(self, gui_nivel):
        print(f"Nivel {self.nivel_actual} - Pregunta: {self.pregunta_actual.enunciado}\n")
        print("Opciones (escriba la letra):\n")

        global respuesta

        respuesta = tk.StringVar()
        pregunta = tk.Label(gui_nivel, text=f"{self.pregunta_actual.enunciado}", font=("Arial", 12), wraplength=800, justify="left")
        pregunta.place(x = 20, y=60)

        # botones para escoger una respuesta SE PODRÁ HACER CON UN FOR???
        

        botón_A = tk.Button(gui_nivel, text=f"{self.pregunta_actual.opciones[0]}", font=("Arial", 12), wraplength=300, justify="left", command=lambda: respuesta.set("A"))
        botón_A.place(x = 20, y=60+50*1)
        botón_B = tk.Button(gui_nivel, text=f"{self.pregunta_actual.opciones[1]}", font=("Arial", 12), wraplength=300, justify="left", command=lambda: respuesta.set("B"))
        botón_B.place(x = 20, y=60+50*2)
        botón_C = tk.Button(gui_nivel, text=f"{self.pregunta_actual.opciones[2]}", font=("Arial", 12), wraplength=300, justify="left", command=lambda: respuesta.set("C"))
        botón_C.place(x = 20, y=60+50*3)
        botón_D = tk.Button(gui_nivel, text=f"{self.pregunta_actual.opciones[3]}", font=("Arial", 12), wraplength=300, justify="left", command=lambda: respuesta.set("D"))
        botón_D.place(x = 20, y=60+50*4)

        # botones para escoger comodines
        comodin = tk.Label(gui_nivel, text=f"Comodines", font=("Arial", 12))
        comodin.place(x = 600, y=110)

        botón_comodin_1= tk.Button(gui_nivel, text=f"{0}) {self.comodines[0]}", font=("Arial", 12), wraplength=300, justify="right", command=lambda: respuesta.set("B"))
        botón_comodin_1.place(x = 600, y=60+50*2)
        botón_comodin_2= tk.Button(gui_nivel, text=f"{1}) {self.comodines[1]}", font=("Arial", 12), wraplength=300, justify="right", command=lambda: respuesta.set("B"))
        botón_comodin_2.place(x = 600, y=60+50*3)
        botón_comodin_3= tk.Button(gui_nivel, text=f"{2}) {self.comodines[2]}", font=("Arial", 12), wraplength=300, justify="right", command=lambda: respuesta.set("B"))
        botón_comodin_3.place(x = 600, y=60+50*4)

        botón_D.wait_variable(respuesta)
    # Invoca el comodín a utilizar 
    def invocar_comodines(self):
        try:
            eleccion_comodin = str(input("Comodín a elegir: ").upper())
        except ValueError:
            print("Por favor, ingresa una opcion valida.")
                
        while True:    
            if eleccion_comodin == "MITAD"  and "Mitad" in self.comodines:
                mitad = Mitad()
                mitad.accion_comodin(self.pregunta_actual.opciones, self.pregunta_actual.respuesta_correcta)
                self.comodines.remove("Mitad")
                break
            elif eleccion_comodin == "PÚBLICO"  and "Público" in self.comodines:
                publico = Publico()
                publico.accion_comodin(self.pregunta_actual.opciones, self.pregunta_actual.respuesta_correcta)
                self.comodines.remove("Público")
                break
            elif eleccion_comodin == "CAMBIAR PREGUNTA"  and "Cambiar pregunta" in self.comodines:
                cambio = Cambio_pregunta()
                #Necesitamos cambiar la respuesta correcta
                self.pregunta_actual.respuesta_correcta = cambio.accion_comodin(self.nivel_actual, self.pregunta_actual.enunciado)
                self.comodines.remove("Cambiar pregunta")
                break
            else:
                print("EL comodín que elegista ya fue utilizado o no existe.")
                try:
                    eleccion_comodin = str(input("Escriba otro comodín o 'Respuesta' si prefiere no usar comodines: ").upper())
                except ValueError:
                    print("Por favor, ingresa una opcion valida.")
                if eleccion_comodin == "RESPUESTA":
                    break
        # Ahora obtenemos la nueva respuesta       
        try:
            respuesta = str(input("Nueva respuesta: ").upper())
        except ValueError:
            print("Por favor, ingresa una opcion valida.")
        return respuesta

    # Esta función esta encargada de proporcionar una interfaz para mostrar las preguntas, opciones y respuesta.
    def jugar(self):
        for nivel, preguntas_nivel in enumerate(self.preguntas, start=1):
            self.nivel_actual = nivel
            
            gui_nivel = tk.Toplevel(self.root)
            gui_nivel.geometry("900x450")
            center(gui_nivel)

            label = tk.Label(gui_nivel, text=f"Nivel {self.nivel_actual}", font=("Arial", 18))
            label.place(x = 20, y=20)


            self.pregunta_actual = random.choice(preguntas_nivel) # Selecciona una pregunta aleatoria del nivel
            
            self.mostrar_pregunta(gui_nivel)

            """
            if respuesta.get() == "COMODÍN":
                respuesta = self.invocar_comodines()

            if respuesta.get() == "SALIR":
                print("La seccion de juego ha finalizado.")
                exit()
            """
            
            if respuesta.get() == self.pregunta_actual.respuesta_correcta:
                messagebox.showinfo("¿Quién quiere ser millonario?", "¡Respuesta correcta!")
                gui_nivel.destroy()
            else:
                messagebox.showinfo("¿Quién quiere ser millonario?", "Respuesta incorrecta. Fin del juego")
                gui_nivel.destroy()
                self.root.destroy()
                exit()

def center(ventana):
    # centrar ventana
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    ancho_borde = ventana.winfo_rootx() -ventana.winfo_x()
    win_width = ancho + 2 * ancho_borde
    altura = ventana.winfo_height()
    titlebar_height = ventana.winfo_rooty() - ventana.winfo_y()
    ancho_ventana = altura + titlebar_height + ancho_borde
    centro_x = ventana.winfo_screenwidth() // 2 - win_width // 2
    centro_y = ventana.winfo_screenheight() // 2 - ancho_ventana // 2
    ventana.geometry('{}x{}+{}+{}'.format(ancho, altura, centro_x, centro_y))
    ventana.deiconify()

if __name__ == "__main__":
    archivos_preguntas = ["Nivel_1.txt", "Nivel_2.txt", "Nivel_3.txt",
                        "Nivel_4.txt", "Nivel_5.txt", "Nivel_6.txt", "Nivel_7.txt"]

    juego = Juego_preguntas(archivos_preguntas, root)
    juego.jugar()