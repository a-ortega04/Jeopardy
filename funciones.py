from Question import *
import random

p200 = random.choice(per200)
i200 = random.choice(Iot200)
h200 = random.choice(Ht200)
a200 = random.choice(Ai200)
s200 = random.choice(So200)
d200 = random.choice(dep200)
v200 = random.choice(vid200)
l200 = random.choice(lug200)
m200 = random.choice(mus200)
pe200 = random.choice(peli200)

p400 = random.choice(per400)
i400 = random.choice(Iot400)
h400 = random.choice(Ht400)
a400 = random.choice(Ai400)
s400 = random.choice(So400)
d400 = random.choice(dep400)
v400 = random.choice(vid400)
l400 = random.choice(lug400)
m400 = random.choice(mus400)
pe400 = random.choice(peli400)

p600 = random.choice(per600)
i600 = random.choice(Iot600)
h600 = random.choice(Ht600)
a600 = random.choice(Ai600)
s600 = random.choice(So600)
d600 = random.choice(dep600)
v600 = random.choice(vid600)
l600 = random.choice(lug600)
m600 = random.choice(mus600)
pe600 = random.choice(peli600)

p800 = random.choice(per800)
i800 = random.choice(Iot800)
h800 = random.choice(Ht800)
a800 = random.choice(Ai800)
s800 = random.choice(So800)
d800 = random.choice(dep800)
v800 = random.choice(vid800)
l800 = random.choice(lug800)
m800 = random.choice(mus800)
pe800 = random.choice(peli800)

p1000 = random.choice(per1000)
i1000 = random.choice(Iot1000)
h1000 = random.choice(Ht1000)
a1000 = random.choice(Ai1000)
s1000 = random.choice(So1000)
d1000 = random.choice(dep1000)
v1000 = random.choice(vid1000)
l1000 = random.choice(lug1000)
m1000 = random.choice(mus1000)
pe1000 = random.choice(peli1000)

def selPreguntasRandom(categoria, px, ix, hx, ax, sx, dx, vx, lx, mx, pelx):
    if categoria == "Personajes":
        return px
    elif categoria == "IoT":
        return ix
    elif categoria == "Hacking Tools":
        return hx
    elif categoria == "AI":
        return ax
    elif categoria == "SO":
        return sx
    elif categoria == "Deportes":
        return dx
    elif categoria == "Videojuegos":
        return vx
    elif categoria == "Lugares":
        return lx
    elif categoria == "Música":
        return mx
    elif categoria == "Películas":
        return pelx

