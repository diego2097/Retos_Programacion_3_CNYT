import math

def marbles(m,v,clicks):
    if (len(m[0]) == len(v)):
        for i in range(clicks):
            matriz_vector = crearMatrizVacia(len(v),1)
            for i in range(len(matriz_vector)):
                matriz_vector[i][0] = v[i]
            matriz_multiplicacion = multiplicar(m,matriz_vector)
            vectorFinal = []
            for i in matriz_multiplicacion:
                vectorFinal.append(i[0])    
            v = vectorFinal
        return vectorFinal
    return None 

def multiplicar(m1,m2):
    if (len(m1[0]) == len(m2)):
        matriz = crearMatrizVacia(len(m1),len(m2[0]))    
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                acumulador = 0
                for k in range(len(m1[0])):
                    acumulador = acumulador + (m1[i][k] * m2[k][j])
                matriz[i][j] = acumulador
        return matriz
    return None

def crearMatrizVacia(m,n):
    matriz = [[[0,0] for col in range(n)] for ren in range(m)]
    return matriz
   

    




