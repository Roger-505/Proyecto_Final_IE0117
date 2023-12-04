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
    def cargar_preguntas_y_opciones(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        preguntas = []
        i = 0
        while i < len(lineas):
            pregunta = lineas[i].strip()
            opciones = [lineas[i+j].strip() for j in range(1, 5)]

# Estructura encargada de buscar la línea que contiene la respuesta correcta
            for j in range(1, 6):
                if lineas[i+j].startswith("CORRECTA:"):
                    respuesta_correcta = lineas[i+j].split(': ')[1].strip()[0].upper()
                    break

            preguntas.append(Pregunta(pregunta, opciones, respuesta_correcta))
            i += 6    # Avanza al siguiente conjunto de pregunta y opciones

        return preguntas

        
# Clase que encapsula la logica del juego.

class Juego_preguntas:
    def __init__(self, preguntas_archivo):
        self.preguntas = Pregunta.cargar_preguntas_y_opciones(preguntas_archivo)
        self.pregunta_actual = None
        self.respuesta_correcta = None

# Funcion temporizador

    def temporizador(self, tiempo_maximo, pregunta_respondida):
        time.sleep(tiempo_maximo)
        if not pregunta_respondida.is_set():
            print("\n¡Tiempo agotado! Fin del juego.")
            exit()

    def mostrar_pregunta(self):
        print(f"Pregunta: {self.pregunta_actual.enunciado}\n")
        print("Opciones:")
        for opcion in self.pregunta_actual.opciones:
            print(f"{opcion}")
            
# Esta función esta encargada de proporcionar una interfaz para mostrar las preguntas, opciones y respuesta.

    def jugar(self):
        print("¡Bienvenido a ¿Quién quiere ser millonario?!")
        time.sleep(2)  # Delay de 2 segundos

        for idx, pregunta in enumerate(self.preguntas):
            self.pregunta_actual = pregunta
            self.respuesta_correcta = pregunta.respuesta_correcta

            print(f"Pregunta {idx + 1}:")
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

            if respuesta == self.respuesta_correcta:
                print("¡Respuesta correcta!")
            else:
                print("Respuesta incorrecta. Fin del juego.")
                exit()


juego = Juego_preguntas("preguntas.txt")
juego.jugar()
