# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:11:37 2022

@author: DISRCT
"""
import pandas as pd
import matplotlib.pyplot as plt

herois = pd.read_csv("superheroes.csv")
herois = herois.dropna()
creator = herois[(herois["creator"] == "Marvel Comics") | (herois["creator"] == "DC Comics") | (herois["creator"] == "Dark Horse Comics") | (herois["creator"] == "George Lucas") | (herois["creator"] == "Lego")]


marvel = creator[creator["creator"] == "Marvel Comics"]
mediaMarvel = marvel.sum()['strength_score']/marvel.strength_score.count()

DC = creator[creator["creator"] == "DC Comics"]
mediaDc = DC.sum()['strength_score']/DC.strength_score.count()

george = creator[creator["creator"] == "George Lucas"]
mediaGeorge = george.sum()['strength_score']/george.strength_score.count()

lego = creator[creator["creator"] == "Lego"]
mediaLego = lego.sum()['strength_score']/lego.strength_score.count()

Dark = creator[creator["creator"] == "Dark Horse Comics"]
mediaDark = Dark.sum()['strength_score']/Dark.strength_score.count()


x = ["Marvel Comics", "George Lucas", "DC Comics", "Lego", "Dark Horse Comics"]
y = [mediaMarvel, mediaGeorge, mediaDc, mediaLego, mediaDark]
plt.bar(x, y, color="black", zorder=3)
plt.xticks(rotation=45)
plt.grid(linestyle='-',zorder=0)
plt.ylabel("Strength Mean")


creator = creator[creator["has_immortality"] == 1]
creator = creator.sort_values(["combat_score"], ascending=False)
j = 1
for i in creator.name:
    print (f"{j} - {i}")
    j+=1
    if j == 6:
        break