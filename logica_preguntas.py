import random
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
        self.puntos = 0

    def mostrar_pregunta(self, gui_nivel):
        print(f"Nivel {self.nivel_actual} - Pregunta: {self.pregunta_actual.enunciado}\n")
        print("Opciones (escriba la letra):\n")

        global respuesta
        respuesta = tk.StringVar()

        # botones para escoger comodines
        comodin = tk.Label(gui_nivel, text=f"Comodines", font=("Arial", 12))
        comodin.place(x = 600, y=130)

        # generar botones para los comodines
        botones_comodines = {}
        for i in range(0, len(self.comodines)):     
            print(self.comodines)
            botones_comodines[f"{self.comodines[i]}"]= tk.Button(gui_nivel, text=f"{i}) {self.comodines[i]}", font=("Arial", 12), wraplength=300, justify="right", command=lambda i=i: respuesta.set(self.comodines[i].upper()))
            botones_comodines[f"{self.comodines[i]}"].place(x = 600, y=100+50*(i + 2))
            
        # generar botones para las opciones
        pregunta = tk.Label(gui_nivel, text=f"{self.pregunta_actual.enunciado}", font=("Arial", 12), wraplength=800, justify="left")
        pregunta.place(x = 20, y=60)

        botones_opciones = {}
        for i in range(0, len(self.pregunta_actual.opciones)):   
            botones_opciones[f"botón_opción_{i + 1}"]= tk.Button(gui_nivel, text=f"{self.pregunta_actual.opciones[i]}", font=("Arial", 12), wraplength=300, justify="right", command=lambda i=i: respuesta.set(chr(i + 65).upper()))
            botones_opciones[f"botón_opción_{i + 1}"].place(x = 20, y=80+50*(i + 1))

        botones_opciones[f"botón_opción_{len(self.pregunta_actual.opciones) - 1}"].wait_variable(respuesta)
    
        return respuesta, botones_opciones, botones_comodines
    # Invoca el comodín a utilizar 
    def invocar_comodines(self, elección_comodín, botones_comodines, botones_preguntas, gui_nivel, pregunta):
        while True:    
            if elección_comodín == "MITAD"  and "Mitad" in self.comodines:
                mitad = Mitad()
                opciones = mitad.accion_comodin(self.pregunta_actual.opciones, self.pregunta_actual.respuesta_correcta)
                messagebox.showinfo("¿Quién quiere ser millonario?", "Vamos a eliminar dos opciones incorrectas")
                self.comodines.remove("Mitad")

                # eliminar el comodín de mitad
                botón_mitad = botones_comodines["Mitad"]
                botón_mitad.destroy()

                respuesta = tk.StringVar()

                for botón in list(botones_preguntas.values()):
                    botón.destroy()

                # nuevos botones 
                botón_A = tk.Button(gui_nivel, text=f"{self.pregunta_actual.opciones[0]}", font=("Arial", 12), wraplength=300, justify="left", command=lambda : respuesta.set(opciones[0].split(".")[0].upper()))
                botón_A.place(x = 20, y=60+50*1)
                botón_B = tk.Button(gui_nivel, text=f"{self.pregunta_actual.opciones[1]}", font=("Arial", 12), wraplength=300, justify="left", command=lambda : respuesta.set(opciones[1].split(".")[0].upper()))
                botón_B.place(x = 20, y=60+50*2)
                 
                botón_B.wait_variable(respuesta) 
                break
            elif elección_comodín == "PÚBLICO"  and "Público" in self.comodines:
                publico = Publico()
                porcentajes_asignados = publico.accion_comodin(self.pregunta_actual.opciones, self.pregunta_actual.respuesta_correcta)
                messagebox.showinfo("¿Quién quiere ser millonario?", f"El público votará por la respuesta que crean que es correcta\n Estos son los resultados:\n{porcentajes_asignados}")
                self.comodines.remove("Público")

                # eliminar el comodín de público
                botón_publico = botones_comodines["Público"]
                botón_publico.destroy()

                # eliminar comodines en pantalla
                for botón in list(botones_comodines.values()):
                    botón.destroy()

                respuesta = tk.StringVar()

                respuesta, botones_opciones, botones_comodines = self.mostrar_pregunta(gui_nivel) 
                break
            elif elección_comodín == "CAMBIAR PREGUNTA"  and "Cambiar pregunta" in self.comodines:
                cambio = Cambio_pregunta()
                self.pregunta_actual.enunciado, self.pregunta_actual.opciones, self.pregunta_actual.respuesta_correcta = cambio.accion_comodin(self.nivel_actual, self.pregunta_actual.enunciado)
                messagebox.showinfo("¿Quién quiere ser millonario?","Vamos a hacer un cambio de pregunta")
                self.comodines.remove("Cambiar pregunta")
                
                # eliminar comodín de cambiar pregunta
                botón_cambiar = botones_comodines["Cambiar pregunta"]
                botón_cambiar.destroy()
                
                pregunta = tk.Label(gui_nivel, text=f"Nivel {self.nivel_actual}", font=("Arial", 18))
                pregunta.place(x = 20, y=20)

                # generar nueva pregunta
                for botón in list(botones_preguntas.values()):
                    botón.destroy()
                pregunta.destroy()
                
                print(self.comodines)
                respuesta, botones_opciones, botones_comodines = self.mostrar_pregunta(gui_nivel) 

                break
        # Ahora obtenemos la nueva respuesta      
        return respuesta
    
    # Esta función esta encargada de proporcionar una interfaz para mostrar las preguntas, opciones y respuesta.
    def jugar(self):
        for nivel, preguntas_nivel in enumerate(self.preguntas, start=1):
            self.nivel_actual = nivel
            
            # generar interfaz del nivel
            gui_nivel = tk.Toplevel(self.root)
            gui_nivel.geometry("900x450")
            center(gui_nivel)

            pregunta = tk.Label(gui_nivel, text=f"Nivel {self.nivel_actual}", font=("Arial", 18))
            pregunta.place(x = 20, y=20)

            # randomizar la pregunta actual
            self.pregunta_actual = random.choice(preguntas_nivel) 
            respuesta, botones_opciones, botones_comodines = self.mostrar_pregunta(gui_nivel) 

            # Elección de comodín
            if respuesta.get() in ["MITAD", "PÚBLICO", "CAMBIAR PREGUNTA"]:
                respuesta = self.invocar_comodines(respuesta.get(), botones_comodines,  botones_opciones, gui_nivel, pregunta)

            # Elección de respuesta
            if respuesta.get() == self.pregunta_actual.respuesta_correcta:
                self.puntos += 10
                messagebox.showinfo("¿Quién quiere ser millonario?", f"¡Respuesta correcta!\n Puntos totales: {self.puntos}")
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