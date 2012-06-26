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

def gerador_de_listas(n):
    lista_teste = [random.randrange(-100, 100, 1) for f in range(0,n)]
    return lista_teste

n = int(raw_input('Digite o Tamanho da Lista (n): '))
m = 1000

l = gerador_de_listas(n)
tempo_cubico = []
tempo_quadratico = []
tempo_div_conq = []
tempo_linear = []

print ""
# Medição do tempo de resposta do algoritmo cúbico
print "Tempo de Execucao Algoritmo Cubico"
fator_de_teste_cubico = m *12
if n == 0:
    ini = time.time() 
    for t in range(0,fator_de_teste_cubico):
        a = algoritmo_cubico(l)
    fim = time.time()
    tempo_cubico.append((fim-ini)/fator_de_teste_cubico)
    print n, tempo_cubico[n]
else:
    for f in range(0,n):
        ini = time.time()                    
        for t in range(0,fator_de_teste_cubico):
            a = algoritmo_cubico(l[0:f])
        fim = time.time()
        tempo_cubico.append((fim-ini)/fator_de_teste_cubico)
        print f+1, tempo_cubico[f]

print ""
# Medição do tempo de resposta do algoritmo quadratico
print "Tempo de Execucao Algoritmo Quadratico"
fator_de_teste_quadratico = m * 100
if n == 0:
    ini = time.time()
    for t in range(0,fator_de_teste_quadratico):
        a = algoritmo_quadratico(l)
    fim = time.time()
    tempo_quadratico.append((fim-ini)/fator_de_teste_quadratico)
    print n, tempo_quadratico[n]
else:
    for f in range(0,n):
        ini = time.time()                    
        for t in range(0,fator_de_teste_quadratico):
            a = algoritmo_quadratico(l[0:f])
        fim = time.time()
        tempo_quadratico.append((fim-ini)/fator_de_teste_quadratico)
        print f+1, tempo_quadratico[f]
print ""
# Medição do tempo de resposta do algoritmo divisão e conquista
print "Tempo de Execucao Algoritmo Divisao e Conquista"
fator_de_teste_div_conq = m * 100
if n == 0:
    ini = time.time() 
    for t in range(0,fator_de_teste_div_conq):
        a = lista_entrada(l)
    fim = time.time()
    tempo_div_conq.append((fim-ini)/fator_de_teste_div_conq)
    print n, tempo_div_conq[n]
else:
    for f in range(0,n):
        ini = time.time()                    
        for t in range(0,fator_de_teste_div_conq):
            a = lista_entrada(l[0:f])
        fim = time.time()
        tempo_div_conq.append((fim-ini)/fator_de_teste_div_conq)
        print f+1, tempo_div_conq[f]
print ""

# Medição do tempo de resposta do algoritmo linear
fator_de_teste_linear = m * 100
print "Tempo de Execucao Algoritmo Linear"
if n == 0:
    ini = time.time() 
    for t in range(0,fator_de_teste_linear):
        a = algoritmo_linear(l)
    fim = time.time()
    tempo_linear.append((fim-ini)/fator_de_teste_linear)
    print n, tempo_linear[n]
else:
    for f in range(0,n):
        ini = time.time()                    
        for t in range(0,fator_de_teste_linear):
            a = algoritmo_linear(l[0:f])
        fim = time.time()
        tempo_linear.append((fim-ini)/fator_de_teste_linear)
        print f+1, tempo_linear[f]

if n <> 0:
    x = [n for n in range(1, n+1)]
    grid(True)
    title("Desempenho dos Algoritmos")
    ylabel("Tempo de Resposta [s]")
    xlabel("Tamanho da Lista")
    lines = plot(x, tempo_cubico, x, tempo_quadratico, x, tempo_div_conq, x, tempo_linear)
    legend(('cubico', 'quadratico', 'div conq', 'linear'), loc='upper left')
    show()