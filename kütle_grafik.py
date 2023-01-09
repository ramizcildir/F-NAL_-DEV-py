# KÜTLEE nin konumu grafiği

import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from sys import exit

# sınır koşulları
k = 4 # yay kalınlığı
m = 5 # bloğun kütlesi
sınırlar = np.array([2,0.2,1,0.5,100])
k_m = np.sqrt(k/m) # açısal frekans

def matrix_oscillation(n):

    matrix = np.zeros((n,n))

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                if i == 0:
                    matrix[i,j] = 2
                    matrix[i,j+1] = -1
                elif i == n-1:
                    matrix[i,j-1] = -1
                    matrix[i,j] = 2
                else:
                    matrix[i, j - 1] = -1
                    matrix[i, j] = 2
                    matrix[i, j + 1] = -1

    return matrix

def özdeğerbulucu(matrix):

    w, v = LA.eig(matrix)
    return w, v


matrix = matrix_oscillation(len(sınırlar))
özdeğerler, özvektör = özdeğerbulucu(matrix)


def equation_system(özdeğerler, özvektör,sınırlar): # b ' nin matris denklemi Ac = b ' yi çözme

    inv_eigen = np.linalg.inv(özvektör)
    constants = inv_eigen.dot(sınırlar)

    return constants

constants = equation_system(özdeğerler, özvektör, sınırlar)

def graph(özdeğerler, özvektör, constants):

    dt = 0.001
    ts = np.arange(0, 10, dt)
    ys = []

    # her blok için yer değiştirme dizileri oluşturma
    for i in range(0, len(sınırlar)):
        arr = []
        for m in range(0, len(ts)):
            sum = 0
            t = ts[m]
            for k in range(0,len(sınırlar)):
                sum += constants[k]*özvektör[i,k]*np.cos(np.sqrt(özdeğerler[k])*k_m*t)
            arr.append(sum)
        ys.append(arr)

    # zamana göre bloğun yer değiştirmesini çizme 
    for i in range(0, len(ys)):
        plt.plot(ts, ys[i], label = "KÜTLE numarası {}".format(i+1))
    plt.xlabel("süre(saniye)")
    plt.ylabel("konum (cm) ")
    plt.legend()
    plt.show()

    return ys, len(ts)

ys, lt = graph(özdeğerler, özvektör, constants)

