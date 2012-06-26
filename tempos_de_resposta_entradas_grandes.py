# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 19:43:10 2012

@author: Bruno Schneider/ Eduardo Bitencourt
"""
import random
import time
from pylab import show, plot, grid, title, ylabel, xlabel, legend
from maior_soma_v2 import algoritmo_cubico
from maior_soma_v2 import algoritmo_quadratico
from maior_soma_v2 import lista_entrada
from maior_soma_v2 import algoritmo_linear
import numpy as np
import matplotlib.pyplot as plt

def gerador_de_listas(n):
    lista_teste = [random.randrange(-100, 100, 1) for f in range(0,n)]
    return lista_teste



# Entrada
n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Inicialização das variáveis
tempo_cubico = []
tempo_quadratico = []
tempo_div_conq = []
tempo_linear = []

m = 1
t = len(n)
for h in range(0, t):
    l = gerador_de_listas(n[h])

    # Medição do tempo de resposta do algoritmo cubico
    fator_de_teste_cubico = m
    ini = time.time()           
    for v in range(0,fator_de_teste_cubico):
        a = algoritmo_cubico(l)
    fim = time.time()
    tempo_cubico.append((fim-ini)/fator_de_teste_cubico)
    print "Cub", n[h], tempo_cubico[h]
    
    # Medição do tempo de resposta do algoritmo quadratico
    fator_de_teste_quadratico = m * 10
    ini = time.time()           
    for v in range(0,fator_de_teste_quadratico):
        a = algoritmo_quadratico(l)
    fim = time.time()
    tempo_quadratico.append((fim-ini)/fator_de_teste_quadratico)
    print "Qua", n[h], tempo_quadratico[h]    
    
    # Medição do tempo de resposta do algoritmo divisao e conquista
    fator_de_teste_div_conq = m * 10
    ini = time.time()           
    for v in range(0,fator_de_teste_div_conq):
        a = lista_entrada(l)
    fim = time.time()
    tempo_div_conq.append((fim-ini)/fator_de_teste_div_conq)
    print "Div", n[h], tempo_div_conq[h]
    
    # Medição do tempo de resposta do algoritmo linear
    fator_de_teste_linear = m * 1000
    ini = time.time()           
    for v in range(0,fator_de_teste_linear):
        a = algoritmo_linear(l)
    fim = time.time()
    tempo_linear.append((fim-ini)/fator_de_teste_linear)
    print "Lin", n[h], tempo_linear[h]

print tempo_cubico
print tempo_quadratico
print tempo_div_conq
print tempo_linear

# Apresentação dos resultados de forma gráfica
ax = plt.subplot(111)
ax.plot(n, tempo_cubico,n, tempo_quadratico,n, tempo_div_conq,n, tempo_linear)
ax.legend(("Cubico", "Quadratico", "Div Conq","Linear"),'upper left', shadow=True, fancybox=True)
ax.grid(True)
ax.set_title("Desempenho dos Algoritmos")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo de Resposta [s]")
ax.set_yscale("log")
ax.set_ylim(1e-5, 1e3)

plt.draw()
plt.show()