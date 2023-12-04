import random
import time

class Comodines:
    def __init__(self):
        pass
# Método a modificar en cada clase hija para cumplir con sus diferentes acciones
    def accion_comodin(self):
        pass

class Mitad(Comodines):
    def accion_comodin(self, enunciado, opciones, respuesta_correcta):
        print("Vamos a eliminar dos opciones incorrectas")
        time.sleep(3)
        for i in range(len(opciones)//2): #For con la mitad de las opciones totales para eliminar la mitad
            while True:
                eliminar = opciones[random.randint(0,len(opciones)-1)]
                if eliminar != respuesta_correcta: #Verificamos que la respuesta a eliminar no sea la correcta
                    opciones.remove(eliminar)
                    break
        return opciones

class Publico(Comodines):
    def accion_comodin(self, opciones, respuesta_correcta):
        acumulado = 0 # Valor bandera que se encarga que el porcentaje total sea 100

        porcentajes_asignados = {"a":"0%","b":"0%","c":"0%","d":"0%"} #Porcentaje final de cada respuesta

        clave = list(porcentajes_asignados.keys()) #Obtenemos las claves para modificar el valor

        for i in range(len(opciones)):
            if i == len(opciones) - 1: #La respuesta "d" tiene que poseer el porcentaje sobrante para componer un 100%
                porcentaje = 100 - acumulado
                porcentajes_asignados[clave[i]] = str(porcentaje) + "%"

            elif opciones[i] == respuesta_correcta:
            # Mejoramos el código para que la respuesta correcta tenga mayor probabilidad de obtener números altos
                factor_atenuacion = 1.05 #factor que modifica las probabilidades

                rango_numeros = range(1, 101)  # Empieza desde 1 en lugar de 0 para evitar dividir entre 0
                probabilidades = [factor_atenuacion ** i for i in rango_numeros] # Definir las probabilidades basadas en la inversa del número
                suma_probabilidades = sum(probabilidades) # Normalizar las probabilidades para asegurarse de que sumen 1.0
                probabilidades = [prob / suma_probabilidades for prob in probabilidades]
                
                porcentaje = random.choices(range(100), probabilidades)[0] # Porcentaje que posee la respuesta correcta
                
                if (acumulado <100) & (porcentaje + acumulado <= 100): # Caso sin problemas
                    porcentajes_asignados[clave[i]] = str(porcentaje) + "%"
                    acumulado += porcentaje
                elif (acumulado <100) & (porcentaje + acumulado > 100): # Si la suma da mayor a 100, restamos el sobrante
                    porcentaje = porcentaje - (acumulado+porcentaje - 100)
                    porcentajes_asignados[clave[i]] = str(porcentaje) + "%"
                    acumulado += porcentaje
            
            else:
                # Misma situación que con las respuesta correcta, pero ahora mayor probabilidad de números bajos
                factor_atenuacion = 0.93
                
                rango_numeros = range(1, 101)  
                probabilidades = [factor_atenuacion ** i for i in rango_numeros]
                suma_probabilidades = sum(probabilidades)
                probabilidades = [prob / suma_probabilidades for prob in probabilidades]

                porcentaje = random.choices(range(100), probabilidades)[0]
                if (acumulado <100) & (porcentaje + acumulado <= 100):
                    porcentajes_asignados[clave[i]] = str(porcentaje) + "%"
                    acumulado += porcentaje
                elif (acumulado <100) & (porcentaje + acumulado > 100):
                    porcentaje = porcentaje - (acumulado+porcentaje - 100)
                    porcentajes_asignados[clave[i]] = str(porcentaje) + "%"
                    acumulado += porcentaje

        print("El público votará por la respuesta que crean que es correcta\n")
        time.sleep(3)
        print("Estos han sido los resultados")
        return porcentajes_asignados

# Prueba de la clase Público
enunciado = "¿Cuál es la función con la que se imprime un mensaje en Python"
opciones = ["int", "echo", "print", "for"]
respuesta_correcta = "print"
prueba = Publico()
porcentajes = prueba.accion_comodin(opciones, respuesta_correcta)
print(porcentajes)




