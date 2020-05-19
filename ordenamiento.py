
import sys
sys.setrecursionlimit(10**6)
import numpy as np
arreglo = []
x = int(input("Ingrese el tamanio del arreglo : "))
for i in range(0,x):
    print("Ingrese el elemento en la pocision",i,": ", end="")
    c = int(input())
    arreglo.append(c)

arreglo = np.array(arreglo)
def intercambia(i,j,aux):
    aux1 = aux[i]
    aux[i] = aux[j]
    aux[j] = aux1



def burbuja(aux):
    for i in range(0,len(aux)-1):
        for j in range(i+1,len(aux)):
            if aux[i]> aux[j]:
                intercambia(i,j,aux)
    aux = np.array(aux)
    return aux



def comprueba(aux):
    cont = 0
    if len(aux)>1:
        for i in range(0,len(aux)-1):
            if aux[i]<aux[i+1]:
                cont = cont+1
            else:
                return False
        if cont == len(aux)-1:
            return True
    else:
        return True


def minimo(x,y):
    if x<y:
        return x
    else:
        return y


def quicksort(aux):
    
    if comprueba(aux):
        return aux
    else:
        mim = minimo(aux[0],aux[len(aux)-1])
        nuevo = []
        otro = []

        for i in range(0,len(aux)):
            if aux[i] <= mim:
                nuevo.append(aux[i])
            else:
                otro.append(aux[i])
        
        return quicksort(nuevo)+quicksort(otro)


print(burbuja(arreglo)*2)

