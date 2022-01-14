from metricas_de_distancia import euclidean_distance, manhattan_distance, minkowski_distance
import random

def distancia_euclidean(x,y):
     ''' return euclidean distance between two lists '''
     return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
 
def distancia_manhattan(x,y):
    ''' return manhattan distance between two lists ''' 
    return sum(abs(a-b) for a,b in zip(x,y))

def generar_puntos (cantidad_puntos,rango):
    puntos = []
    
    for _ in range (cantidad_puntos):
        x_vals = random.randint(0,rango)
        y_vals= random.randint(0,rango)
        puntos.append((x_vals,y_vals))
       
    return puntos

def distancia_entre_puntos (puntos, cantidad_puntos):

    for punto in puntos:
        x=punto[0]
        y=punto[1]
    


        


   

def agrupacion_de_clousters:
    pass

def main():
    datos = int (input('Ingrese la cantidad de puntos aleatoreos que desea generar: '))
    rango = int (input ('Ingrese el rango en x & y en el que estaran de datos: '))
    puntos = generar_puntos(datos,rango)
    distancia = distancia_entre_puntos(puntos)


if __name__=='__main__':
    main()