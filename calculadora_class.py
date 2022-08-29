# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 11:25:43 2022

@author: DISRCT
"""
import math

class Calculadora:
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        
    def soma(self):
        return (self.n1 + self.n2)
    
    def multiplica(self):
        return (self.n1 * self.n2)
    
    def divide(self):
        return (self.n1 / self.n2)
    
    def subtrai(self):
        return (self.n1 - self.n2)
    
class Calculadora_master(Calculadora):
    
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def raiz(self):
        return (math.sqrt(self.n1))
    
    def 


calcula = Calculadora(10, 10)
ca = Calculadora_master(10, 10)
print("Soma: ", calcula.soma())
print("Soma: ", ca.raiz())