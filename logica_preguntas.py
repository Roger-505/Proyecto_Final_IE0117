import random
import time
import threading

# Clase que encapsula los atributos del juego.

class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
    
# Esta funcion es la encargada de procesar el archivo .txt que almacena las preguntas, opciones, respuestas correctas y devuelv una lista de tuplas con la información.
    def cargar_todas_las_preguntas(archivos_preguntas):
        todas_las_preguntas = []
        for archivo in archivos_preguntas:
            with open(archivo, 'r') as file:
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
    def __init__(self, preguntas_archivo):
        self.archivos_preguntas = archivos_preguntas
        self.rondas = 7
        self.preguntas = Pregunta.cargar_todas_las_preguntas(archivos_preguntas)
        self.puntos = 0  # Puntos iniciales

# Funcion temporizador

    def temporizador(self, tiempo_maximo, pregunta_respondida):
        time.sleep(tiempo_maximo)
        if not pregunta_respondida.is_set():
            print("\n¡Tiempo agotado! Fin del juego.")
            exit()

    def mostrar_pregunta(self):
        print(f"Nivel {self.nivel_actual} - Pregunta: {self.pregunta_actual.enunciado}\n")
        print("Opciones:")
        for opcion in self.pregunta_actual.opciones:
            print(f"{opcion}")
        print("Salir")

            
# Esta función esta encargada de proporcionar una interfaz para mostrar las preguntas, opciones y respuesta.

    def jugar(self):
        print("¡Bienvenido a ¿Quién quiere ser millonario?!")
        time.sleep(2)  # Delay de 2 segundos

    
        for nivel, preguntas_nivel in enumerate(self.preguntas, start=1):
            self.nivel_actual = nivel
            print(f"\n----- Nivel {self.nivel_actual} -----\n")


            self.pregunta_actual = random.choice(preguntas_nivel) # Selecciona una pregunta aleatoria del nivel
            self.mostrar_pregunta()

            pregunta_respondida = threading.Event()
            temporizador_hilo = threading.Thread(target=self.temporizador, args=(10, pregunta_respondida))
            temporizador_hilo.start()

            try:
                respuesta = input("Respuesta: ").upper()
            except ValueError:
                print("Por favor, ingresa una opcion valida.")
                exit()

            pregunta_respondida.set()

            if respuesta == "SALIR":
                print("La seccion de juego ha finalizado.")
                exit()

            if respuesta == self.pregunta_actual.respuesta_correcta:
                print("¡Respuesta correcta!")
                self.puntos += 10   # Se suman puntos por cada pregunta correcta
                print(f"Puntos acumulados: {self.puntos}")

            else:
                print("Respuesta incorrecta. Fin del juego. Puntos acumulados: {self.puntos}")
                exit()



archivos_preguntas = ["Nivel_1.txt", "Nivel_2.txt", "Nivel_3.txt",
                      "Nivel_4.txt", "Nivel_5.txt", "Nivel_6.txt", "Nivel_7.txt"]

juego = Juego_preguntas(archivos_preguntas)
juego.jugar()



