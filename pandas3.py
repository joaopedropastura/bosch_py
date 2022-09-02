# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 08:24:39 2022

@author: disrct
"""

import pandas as pd

titanic = pd.read_csv("titanic.csv")

def faixa_etaria(linhas):
    idade = linhas["Age"]    
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 65:
        return "Adulto"
    elif idade >= 65:
        return "Idoso"
    else:
        return "Nada"

titanic["Faixa_etaria"] = titanic.apply(faixa_etaria, axis=1)
Pclass1 = titanic[titanic["Pclass"] == 1] 
Pclass2 = titanic[titanic["Pclass"] == 2]
Pclass3 = titanic[titanic["Pclass"] == 3]
Pclass = titanic["Pclass"].count() 
m_totais = titanic[titanic["Survived"] == 0]
v_totais = titanic[titanic["Survived"] == 1]    
   

def cal_porcentagem(val, total):
    percent = float(val/total)
    print_percent = ("%.2f" % (percent*100) + "%")
    return(print_percent)



p1_total = cal_porcentagem(Pclass1.Pclass.count(), Pclass)
p2_total = cal_porcentagem(Pclass2.Pclass.count(), Pclass)
p3_total = cal_porcentagem(Pclass3.Pclass.count(), Pclass)

p1_m = Pclass1.Survived[Pclass1["Survived"] == 0].count()
p2_m = Pclass2.Survived[Pclass2["Survived"] == 0].count()
p3_m = Pclass3.Survived[Pclass3["Survived"] == 0].count()

p1_m_totais = cal_porcentagem(p1_m, m_totais.Survived.count())
p2_m_totais = cal_porcentagem(p2_m, m_totais.Survived.count())
p3_m_totais = cal_porcentagem(p3_m, m_totais.Survived.count())

p1_v_totais = cal_porcentagem((Pclass1.Pclass.count() - p1_m), v_totais.Survived.count())
p2_v_totais = cal_porcentagem((Pclass2.Pclass.count() - p2_m), v_totais.Survived.count())
p3_v_totais = cal_porcentagem((Pclass3.Pclass.count() - p3_m), v_totais.Survived.count())

adultos_v = v_totais.Faixa_etaria[v_totais["Faixa_etaria"] == "Adulto"].count()
