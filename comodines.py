import random

class Comodines:
    def __init__(self):
        pass

    def accion_comodin(self, enunciado, preguntas, pregunta_correcta):
        pass

class Mitad(Comodines):
    def accion_comodin(self, enunciado, preguntas, pregunta_correcta):
        for i in range(2):
            while True:
                eliminar = preguntas[random.randint(0,len(preguntas)-1)]
                if eliminar != pregunta_correcta:
                    preguntas.remove(eliminar)
                    break
        return preguntas
prueba = Mitad()
enunciado = "¿Cuál es la función con la que se imprime un mensaje en Python"
preguntas = ["int", "echo", "print", "for"]
print(preguntas)
pregunta_correcta = "print"
preguntas = prueba.accion_comodin(enunciado, preguntas, pregunta_correcta)
print(preguntas)


