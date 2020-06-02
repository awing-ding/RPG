# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:07:09 2020

@author: Antoine
"""

# Créé par Perso, le 02/06/2020 en Python 3.4
from random import*

from random import*
def stat_mob(level):
    if level <= 5:
        stat__mob = [randint(2,5),randint(5,8),randint(1,5)]
    elif level > 5 and level <= 10:
        stat__mob = [randint(3,7),randint(7,10),randint(5,10)]
    elif level > 10 and level <= 15:
        stat__mob = [randint(5,10),randint(10,14),randint(10,15)]
    elif level > 15:
        stat__mob = [randint(10,15),randint(15,20),randint(15,20)]
    return(stat__mob)
def spawn_mob(zone,level):
    if zone == "foret":
        mob = "sanglier"
        stats_mob = stat_mob(level)
    elif zone == "grotte":
        mob = "ours"
        stats_mob = stat_mob(level)
    elif zone == "lac":
        mob = "poisson"
        stats_mob = [1,1]
    elif zone == "village":
        mob = "bandit"
        stats_mob = stat_mob(level)
    elif zone == "montagne":
        mob = "loup"
        stats_mob = stat_mob(level)
    return(mob,stats_mob)
def combat(mob,stat_mob,stat,level):
    print("Attention un "+str(mob)+" sauvage apparait, il a "+str(stat_mob[0])+" d'attque et "+str(stat_mob[1])+" point de vie")
    Loot = None
    ExpGagner = 0
    PV = stat[0]
    ATK = stat[1]
    ATKmob = stat_mob[0]
    PVmob = stat_mob[1]
    while PV > 0 and PVmob > 0:
        print(str(mob)+" attaque, il vous fait:"+str(ATKmob)+" pts de degat")
        PV = PV - ATKmob
        if PV <= 0:
            print("Tu es mort-Adele")
        elif PV > 0:
            print("il vous reste "+str(PV)+" point de vie")
        else :
            print("tu attaques avec la puissance de... tes poings, tu fais "+str(ATK)+" point de degat")
            PVmob = PVmob - ATK
            if PVmob <= 0 :
                print("il lui reste 0 point de vie")
            else:
                print("il lui reste "+str(PVmob)+" point de vie")
            if PVmob <= 0:
                print("tu as battu ce machin truc")
    if PVmob == 0 and PV > 0:
        Loot = loot(mob,stat_mob[2])[0]
        ExpGagner = loot(mob,stat_mob)[1]
    return(ExpGagner,Loot)
def loot(mob,stat):
    Nb = 1
    if Nb == 1:
        loot = "quelque chose"
    exp = stat[2]
    return(loot,exp)
PV = 20
ATK = 5
stat = [PV,ATK]


def foret():
    print("t'es dans la foret")
    return(foret)

def lac():
    print("t'es au lac")
    return(lac)


def montagnes():
    print("t'es dans les montagnes")
    return(montagnes)

def village():
    print("t'es au village")
    deplacementvillage= str(input("veux tu aller vers: la forge ou la bibliotheque ?         "))
    if deplacementvillage== "forge":
        zone= forge()
    elif deplacementvillage== "bibliotheque":
        zone= bibliotheque()
    return(village)

def forge():
    print("t'es dans la forge")
    return(forge)

def bibliotheque():
    print("t'es dans la bibliotheque")
    return(bibliotheque)

def grotte():
    print("t'es dans la grotte")
    return(grotte)


verification = False
while verification != True :
  deplacement= str(input("veux tu aller vers: la foret, le village, la grotte, les montagnes ou le lac ?        "))
  if deplacement== "foret":
       zone= foret()
       verification = True
  elif deplacement == "grotte":
       zone = grotte()
       verification = True
  elif deplacement == "montagnes":
       zone = montagnes()
       verification = True
  elif deplacement == "village":
       zone= village()
       verification = True
  elif deplacement== "lac":
       zone= lac()
       verification = True

