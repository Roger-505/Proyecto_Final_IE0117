import random

class Comodines:
    def __init__(self):
        pass
#Método a modificar en cada clase hija para cumplir con sus diferentes acciones
    def accion_comodin(self, enunciado, preguntas, pregunta_correcta):
        pass

class Mitad(Comodines):
    def accion_comodin(self, enunciado, preguntas, pregunta_correcta):
        for i in range(len(preguntas)//2): #For con la mitad de las preguntas totales para eliminar la mitad
            while True:
                eliminar = preguntas[random.randint(0,len(preguntas)-1)]
                if eliminar != pregunta_correcta: #Verificamos que la respuesta a eliminar no sea la correcta
                    preguntas.remove(eliminar)
                    break
        return preguntas

#Prubea del comodín Mitad
prueba = Mitad()
enunciado = "¿Cuál es la función con la que se imprime un mensaje en Python"
preguntas = ["int", "echo", "print", "for"]
print(preguntas)
pregunta_correcta = "print"
preguntas = prueba.accion_comodin(enunciado, preguntas, pregunta_correcta)
print(preguntas)


