# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 09:35:12 2022

@author: DISRCT
"""
import pandas as pd

cars = pd.read_csv("Cars93_miss.csv")
cars = cars.loc[:, ["Manufacturer", "Make", "Price", "MPG.city", "Type", "Passengers"]]
cars = cars.dropna()
passengers = cars[cars["Passengers"] == 5]
mpg = passengers.sort_values(by = "MPG.city", ascending=False).head(10)
price = mpg.sort_values(by = "Price")
top5 = price.head(5)
print(top5)
