﻿# Créé par Perso, le 02/06/2020 en Python 3.4
from random import*
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

direction=randint(1,5)
if direction==1:
    zone= foret()
elif direction==2:
    zone= grotte()
elif direction==3:
    zone= village()
elif direction==4:
    zone= montagnes()
elif direction==5:
    zone= lac()

deplacement = input("veux tu aller vers: la foret, le village, la grotte, les montagnes, le lac ?")
if deplacement== "foret":
    zone= foret()
elif deplacement== "grotte":
    zone= grotte()
elif deplacement== "montagnes":
    zone= montagnes()
elif deplacement== "village":
    zone= village()
elif deplacement== "lac":
    zone= lac()

