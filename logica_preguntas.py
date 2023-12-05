import random
import time
import threading

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
        self.comodines = ["Mitad","Público","Cambiar pregunta"]
        self.usuario = usuario
        self.puntos = 0


    def mostrar_pregunta(self):
        print(f"Nivel {self.nivel_actual} - Pregunta: {self.pregunta_actual.enunciado}\n")
        time.sleep(1)
        print("Opciones (escriba la letra):\n")
        for opcion in self.pregunta_actual.opciones:
            print(f"{opcion}")
        time.sleep(2)
        print("\nComodines (Escriba 'comodín'):\n")
        for i, comodin in enumerate(self.comodines, start=1):
            print(i,comodin)
        
        print("\nSi quiere salir del juego, escriba: Salir\n")

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
        print("\nComenzando nuevo juego...")
        time.sleep(2)  # Delay de 2 segundos

    
        for nivel, preguntas_nivel in enumerate(self.preguntas, start=1):
            self.nivel_actual = nivel
            print(f"\n----- Nivel {self.nivel_actual} -----\n")


            self.pregunta_actual = random.choice(preguntas_nivel) # Selecciona una pregunta aleatoria del nivel
            self.mostrar_pregunta()

            pregunta_respondida = threading.Event()
    
            try:
                respuesta = str(input("Respuesta: ").upper())
            except ValueError:
                print("Por favor, ingresa una opcion valida.")
                self.guardar_resultados()
                exit()

            pregunta_respondida.set()


            if respuesta == "COMODÍN":
                respuesta = self.invocar_comodines()


            if respuesta == "SALIR":
                print(f"La sección de juego ha finalizado. Puntos acumulados: {self.puntos}")
                self.guardar_resultados()
                exit()

            if respuesta == self.pregunta_actual.respuesta_correcta:
                print("¡Respuesta correcta!")
                self.puntos += 10
                print(f"Puntos acumulados: {self.puntos}")
            else:
                print(f"Respuesta incorrecta. Fin del juego. Puntos acumulados: {self.puntos}")
                self.guardar_resultados()
                exit()

        print(f"¡Felicidades! Has completado todas las rondas. Puntos totales: {self.puntos}")
        self.guardar_resultados()



    def guardar_resultados(self):
        with open("resultados.txt", "a") as file:
            file.write(f"Nombre: {self.usuario.nombre}\n")
            file.write(f"Trabajo: {self.usuario.trabajo}\n")
            file.write(f"Edad: {self.usuario.edad}\n")
            file.write(f"Puntos obtenidos: {self.puntos}\n")
            file.write("\n")

    def mostrar_puntajes_antiguos(self):
        print("\n----- Puntajes Antiguos -----\n")
        try:
            with open("resultados.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("Aún no hay puntajes antiguos.")

def mostrar_menu():
    print("\n----- Menú Principal -----\n")
    print("1. Jugar")
    print("2. Mostrar Puntajes Antiguos")
    print("3. Salir")



def main():
    print("¡Bienvenido a ¿Quién quiere ser millonario?!")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1, 2, 3): ")

        if opcion == "1":
            usuario_objeto = Usuario()
            archivos_preguntas = ["Nivel_1.txt", "Nivel_2.txt", "Nivel_3.txt",
                                  "Nivel_4.txt", "Nivel_5.txt", "Nivel_6.txt", "Nivel_7.txt"]
            juego = Juego_preguntas(archivos_preguntas, usuario_objeto)
            juego.jugar()
        elif opcion == "2":
            juego = Juego_preguntas([]) 
            juego.mostrar_puntajes_antiguos()
        elif opcion == "3":
            print("¡Hasta luego!")
            exit()
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

main()
