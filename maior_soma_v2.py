# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:09:31 2012

@author: Bruno Schneider/ Eduardo Bitencourt
"""
def algoritmo_cubico(X):
    max_ate_agora = 0.0
    N = len(X)
    for L in range(1, N + 1):
        for U in range(L, N + 1):
            soma = 0.0
            for I in range(L, U + 1):
                soma = soma + X[I - 1]
            max_ate_agora = max(max_ate_agora, soma)
    return max_ate_agora


def algoritmo_quadratico(X):
    max_ate_agora = 0.0
    N = len(X)
    for L in range(1, N + 1):
        soma = 0.0
        for U in range(L, N + 1):
            soma = soma + X[U - 1]
            max_ate_agora = max(max_ate_agora, soma)
    return max_ate_agora


def lista_entrada(X):
    def algoritmo_divisao_e_conquista(L, U):
        if L > U:
            return 0.0
        if L == U:
            return max(0.0, X[L - 1])
           
        M = (L + U) / 2
        soma = 0.0
        max_a_esquerda = 0.0
        for I in range(M, 0, -1):
            soma = soma + X[I - 1]
            max_a_esquerda = max(max_a_esquerda, soma)
        soma = 0.0
        max_a_direita = 0.0
        for I in range(M + 1, U + 1):
            soma = soma + X[I - 1]
            max_a_direita = max(max_a_direita, soma)
        max_cruzamento_esqdir = max_a_esquerda + max_a_direita
                   
        max_em_A = algoritmo_divisao_e_conquista(L, M)
        max_em_B = algoritmo_divisao_e_conquista(M + 1, U)
        return max(max_cruzamento_esqdir, max_em_A, max_em_B)
    N = len(X)
    resposta = algoritmo_divisao_e_conquista(1, N)
    return resposta


def algoritmo_linear(X):
    max_ate_agora = 0.0
    max_terminando_aqui = 0.0
    N = len(X)
    for I in range(1, N + 1):
        max_terminando_aqui = max(0.0, max_terminando_aqui + X[I - 1])
        max_ate_agora = max(max_ate_agora, max_terminando_aqui)
    return max_ate_agora