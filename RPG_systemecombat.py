from random import*
def stat_mob(level):
    if level <= 5:
        stat__mob = [randint(2,7),randint(3,8),randint(1,5)]
    elif level > 5 and level <= 10:
        stat__mob = [randint(5,9),randint(7,12),randint(5,10)]
    elif level > 10 and level <= 15:
        stat__mob = [randint(7,12),randint(12,16),randint(10,15)]
    elif level > 15:
        stat__mob = [randint(10,17),randint(15,22),randint(15,20)]
    return(stat__mob)
def LEVEL(level,exp,stat):
    multiplicateur = 1.22
    Pv = stat[0]
    Atk = stat[1]
    lvl = level
    level1 = level
    xpnecessaire = round(20 * (multiplicateur**lvl))
    xpnecessaire2 = xpnecessaire
    if level > 0:
        exptot = round(20*(multiplicateur**(lvl-1) )+ exp)
    else:
        exptot = exp
    if exp >= xpnecessaire:
        while exp >= xpnecessaire2:
            exp = exp-xpnecessaire2
            level1 = level1 +1
            xpnecessaire2 = round(20 * (multiplicateur**level1))
    diff = level1 - lvl
    if diff > 0:
        Pv =round(Pv*(1.1**diff))
        Atk = round(Atk*(1.1**diff))
    return(level1,exp,exptot,lvl,diff,Pv,Atk,xpnecessaire,xpnecessaire2)
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
def combat(mob,stat_mob,stat,level,exp):
    print("Attention un "+str(mob)+" sauvage apparait, il a "+str(stat_mob[0])+" d'attque et "+str(stat_mob[1])+" point de vie")
    Loot = "rien"
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
            print("tu attaques avec la puissance de... tes poings, tu fais "+str(ATK)+" point de degat")
            PVmob = PVmob - ATK
            if PVmob <= 0 :
                print("il lui reste 0 point de vie")
                PVmob = 0
            else:
                print("il lui reste "+str(PVmob)+" point de vie")
            if PVmob <= 0:
                print("tu as battu ce machin truc")
    if PVmob == 0 and PV > 0:
        ExpGagner = loot(mob,stat_mob)[1]
        exp = exp + ExpGagner
        level3 = LEVEL(level,exp,stat)
        level = level3[0]
        PV = level3[5]
        ATK = level3[6]
    return(exp,level,Loot,PV,ATK)
def loot(mob,stat):
    Nb = 1
    if Nb == 1:
        loot = "quelque chose"
    exp = stat[2]
    return(loot,exp)
PV = 20
ATK = 5
level = 0
stat = [PV,ATK]
experience = 0
a=combat(spawn_mob("foret",level)[0],spawn_mob("foret",level)[1],stat,level,experience)
print(a)
experience = a[0]
level = a[1]
iteration = 1
while level != 10:
    a=combat(spawn_mob("foret",level)[0],spawn_mob("foret",level)[1],stat,level,experience)
    experience = a[0]
    level = a[1]
    iteration = iteration + 1
    PV = a[3]
    ATK = a[4]
    stat = [PV,ATK]
print(iteration,experience,level)