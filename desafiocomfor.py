# -*- coding: utf-8 -*-
"""
Created on Wed May  9 20:43:14 2018

@author: cvmar
"""
import random

print("Desafio -> Dado um número diferente de 0 e 1, somar seus anteriores")

numero = random.randrange(2, 10)

print("Número informado ", numero)

numeros = range(1, numero + 1)

total = sum(numeros)

print("total da soma: ", total)

print("Sem for: ")

inicio = numero + 1

semFor = (numero * inicio)/ 2

print("resultado ", semFor)
    
