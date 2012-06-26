# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 02:33:40 2012

@author: Bruno Schneider/ Eduardo Bitencourt
"""
from nose.tools import assert_equals
import nose
from maior_soma_v2 import algoritmo_cubico
from maior_soma_v2 import algoritmo_quadratico
from maior_soma_v2 import lista_entrada
from maior_soma_v2 import algoritmo_linear


# Testes para o Algoritmo Cúbico

def test_maior_soma_lista_vazia_algoritmo_cubico():
    assert_equals(algoritmo_cubico([]),(0))

def test_maior_soma_lista_com_1_elemento_zero_algoritmo_cubico():
    assert_equals(algoritmo_cubico([0]),(0))

def test_maior_soma_lista_com_1_elemento_negativo_algoritmo_cubico():
    assert_equals(algoritmo_cubico([-1]),(0))

def test_maior_soma_lista_com_2_elementos_zero_algoritmo_cubico():
    assert_equals(algoritmo_cubico([0,0]),(0))

def test_maior_soma_lista_com_elementos_negativos_algoritmo_cubico():
    assert_equals(algoritmo_cubico([-1,-1,-2]),(0))

def test_maior_soma_lista_com_1_elemento_positivo_algoritmo_cubico():
    assert_equals(algoritmo_cubico([1]),(1))

def test_maior_soma_lista_com_elementos_positivos_algoritmo_cubico():
    assert_equals(algoritmo_cubico([1,1,1,1,1,1,1,1]),(8))

def test_maior_soma_lista_maior_soma_na_primenra_metade_algoritmo_cubico():
    assert_equals(algoritmo_cubico([1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1]),(8))

def test_maior_soma_lista_maior_soma_na_segunda_metade_algoritmo_cubico():
    assert_equals(algoritmo_cubico([-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1]),(8))

def test_maior_soma_lista_maior_soma_na_metade_algoritmo_cubico():
    assert_equals(algoritmo_cubico([-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1]),(8))


# Testes para o Algoritmo Quadratico

def test_maior_soma_lista_vazia_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([]),(0))

def test_maior_soma_lista_com_1_elemento_zero_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([0]),(0))

def test_maior_soma_lista_com_1_elemento_negativo_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([-1]),(0))

def test_maior_soma_lista_com_2_elementos_zero_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([0,0]),(0))

def test_maior_soma_lista_com_elementos_negativos_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([-1,-1,-2]),(0))

def test_maior_soma_lista_com_1_elemento_positivo_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([1]),(1))

def test_maior_soma_lista_com_elementos_positivos_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([1,1,1,1,1,1,1,1]),(8))

def test_maior_soma_lista_maior_soma_na_primenra_metade_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1]),(8))

def test_maior_soma_lista_maior_soma_na_segunda_metade_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1]),(8))

def test_maior_soma_lista_maior_soma_na_metade_algoritmo_quadratico():
    assert_equals(algoritmo_quadratico([-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1]),(8))


# Testes para o Algoritmo Divisão e Conquista

def test_maior_soma_lista_vazia_lista_entrada():
    assert_equals(lista_entrada([]),(0))

def test_maior_soma_lista_com_1_elemento_zero_lista_entrada():
    assert_equals(lista_entrada([0]),(0))

def test_maior_soma_lista_com_1_elemento_negativo_lista_entrada():
    assert_equals(lista_entrada([-1]),(0))

def test_maior_soma_lista_com_2_elementos_zero_lista_entrada():
    assert_equals(lista_entrada([0,0]),(0))

def test_maior_soma_lista_com_elementos_negativos_lista_entrada():
    assert_equals(lista_entrada([-1,-1,-2]),(0))

def test_maior_soma_lista_com_1_elemento_positivo_lista_entrada():
    assert_equals(lista_entrada([1]),(1))

def test_maior_soma_lista_com_elementos_positivos_lista_entrada():
    assert_equals(lista_entrada([1,1,1,1,1,1,1,1]),(8))

def test_maior_soma_lista_maior_soma_na_primenra_metade_lista_entrada():
    assert_equals(lista_entrada([1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1]),(8))

def test_maior_soma_lista_maior_soma_na_segunda_metade_lista_entrada():
    assert_equals(lista_entrada([-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1]),(8))

def test_maior_soma_lista_maior_soma_na_metade_lista_entrada():
    assert_equals(lista_entrada([-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1]),(8))


# Testes para o Algoritmo Linear

def test_maior_soma_lista_vazia_algoritmo_linear():
    assert_equals(algoritmo_linear([]),(0))

def test_maior_soma_lista_com_1_elemento_zero_algoritmo_linear():
    assert_equals(algoritmo_linear([0]),(0))

def test_maior_soma_lista_com_1_elemento_negativo_algoritmo_linear():
    assert_equals(algoritmo_linear([-1]),(0))

def test_maior_soma_lista_com_2_elementos_zero_algoritmo_linear():
    assert_equals(algoritmo_linear([0,0]),(0))

def test_maior_soma_lista_com_elementos_negativos_algoritmo_linear():
    assert_equals(algoritmo_linear([-1,-1,-2]),(0))

def test_maior_soma_lista_com_1_elemento_positivo_algoritmo_linear():
    assert_equals(algoritmo_linear([1]),(1))

def test_maior_soma_lista_com_elementos_positivos_algoritmo_linear():
    assert_equals(algoritmo_linear([1,1,1,1,1,1,1,1]),(8))

def test_maior_soma_lista_maior_soma_na_primenra_metade_algoritmo_linear():
    assert_equals(algoritmo_linear([1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1]),(8))

def test_maior_soma_lista_maior_soma_na_segunda_metade_algoritmo_linear():
    assert_equals(algoritmo_linear([-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1]),(8))

def test_maior_soma_lista_maior_soma_na_metade_algoritmo_linear():
    assert_equals(algoritmo_linear([-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1]),(8))

nose.run()