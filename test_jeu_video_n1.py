# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:07:09 2020

@author: Antoine
"""

# Créé par Perso, le 02/06/2020 en Python 3.4
import random
def foret():
    print("t'es dans la foret")

def lac():
    print("t'es au lac")


def montagnes():
    print("t'es dans les montagnes")

def village():
    print("t'es au village")



def grotte():
    print("t'es dans la grotte")


verification = False
while verification != True :
  deplacement= input("veux tu aller vers: la foret, le village, la grotte, les montagnes, le lac ?")
  if deplacement== "foret":
       zone = "foret"
       foret()
       verification = True
  elif deplacement == "grotte":
       zone = "grotte"
       grotte()
       verification = True
  elif deplacement == "montagnes":
       zone = "montagnes"
       montagnes()
       verification = True
  elif deplacement == "village":
       zone = "village"
       village()
       verification = True
  elif deplacement== "lac":
       zone = "lac"
       lac()

       verification = True

