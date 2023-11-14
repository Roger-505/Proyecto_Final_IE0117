import random
import time

# Esta funcion es la encargada de procesar el archivo .txt que almacena las preguntas, opciones, respuestas correctas y devuelve una lista de tuplas con la información.

def cargar_preguntas_y_opciones(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    preguntas_y_opciones = []
    i = 0
    while i < len(lineas):
        pregunta = lineas[i].strip()
        opciones = [lineas[i+j].strip() for j in range(1, 5)]
        
        # Esta estructura esta encargada de buscar la línea que contiene la respuesta correcta
        for j in range(1, 6):
            if lineas[i+j].startswith("CORRECTA:"):
                respuesta_correcta = lineas[i+j].split(': ')[1].strip()[0].upper()  # Toma la primera letra y convertirla a mayúscula
                break

        preguntas_y_opciones.append((pregunta, opciones, respuesta_correcta))
        i += 6  # Avanza al siguiente conjunto de pregunta y opciones

    return preguntas_y_opciones


# Esta función esta encargada de proporcionar una interfaz para mostrar las preguntas, opciones y respuesta. 

def main():
    preguntas = cargar_preguntas_y_opciones("preguntas.txt")
    pregunta_actual = random.choice(preguntas)

    print("¡Bienvenido a ¿Quién quiere ser millonario?!")
    time.sleep(2)  # Delay de 2 segundos
    print(f"Pregunta 1: {pregunta_actual[0]}\n")
    print("Opciones:")
    for opcion in pregunta_actual[1]:
        print(f"{opcion}")

    respuesta_correcta = pregunta_actual[2]  # Almacena la respuesta correcta

    respuesta = input("Respuesta: ").upper()

    if respuesta == respuesta_correcta:
        print("¡Respuesta correcta!")
    else:
        print(f"¡Respuesta incorrecta!. La respuesta correcta es {respuesta_correcta}.")

main()

