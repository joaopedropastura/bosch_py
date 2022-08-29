# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:12:16 2022

@author: DISRCT
"""

class Carro:
    
    def __init__(self, marca, modelo, ano, categoria, motor, portas, cambio):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.categoria = categoria
        self.motor = motor
        self.cambio = cambio

    @staticmethod
    def criaRoda():
        Carro.rodas = '4 rodas'
    @staticmethod
    def altera_roda(qt_rodas):
        Carro.rodas = qt_rodas
        
    def mostrar_dados(self):
        print(f'''
Marca: {self.marca}
Modelo: {self.modelo}
Ano: {self.ano}
Categoria: {self.categoria}
Motor: {self.motor}
Cambio: {self.cambio}
Rodas: {Carro.rodas}
''')

carro_joao = Carro("Honda", "Civic", 2022, "sedan", 1.5, 4, "CVT")
Carro.criaRoda()
carro_herm = Carro("Audi", "RS7", "2022", "esportivo", "4.0", "2", "automatico")
Carro.altera_roda('12 rodas')
carro_joao.mostrar_dados()
carro_herm.mostrar_dados()
