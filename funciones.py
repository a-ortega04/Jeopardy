from Question import *
import random

categorias = ["Personajes", "IoT", "Hacking Tools", "AI", "SO", "Deportes", "Videojuegos", "Lugares", "Música", "Películas"]

texto = random.sample(categorias, k=6)

cat1 = texto[0]
cat2 = texto[1]
cat3 = texto[2]
cat4 = texto[3]
cat5 = texto[4]
cat6 = texto[5]

p200 = random.sample(per200, k=1)
i200 = random.sample(IeO200, k=1)
h200 = random.sample(Ht200, k=1)
a200 = random.sample(Ai200, k=1)
s200 = random.sample(So200, k=1)
d200 = random.sample(dep200, k=1)
v200 = random.sample(vid200, k=1)
l200 = random.sample(lug200, k=1)
m200 = random.sample(mus200, k=1)
pe200 = random.sample(peli200, k=1)

p400 = random.sample(per400, k=1)
i400 = random.sample(IeO400, k=1)
h400 = random.sample(Ht400, k=1)
a400 = random.sample(Ai400, k=1)
s400 = random.sample(So400, k=1)
d400 = random.sample(dep400, k=1)
v400 = random.sample(vid400, k=1)
l400 = random.sample(lug400, k=1)
m400 = random.sample(mus400, k=1)
pe400 = random.sample(peli400, k=1)

p600 = random.sample(per600, k=1)
i600 = random.sample(IeO600, k=1)
h600 = random.sample(Ht600, k=1)
a600 = random.sample(Ai600, k=1)
s600 = random.sample(So600, k=1)
d600 = random.sample(dep600, k=1)
v600 = random.sample(vid600, k=1)
l600 = random.sample(lug600, k=1)
m600 = random.sample(mus600, k=1)
pe600 = random.sample(peli600, k=1)

p800 = random.sample(per800, k=1)
i800 = random.sample(IeO800, k=1)
h800 = random.sample(Ht800, k=1)
a800 = random.sample(Ai800, k=1)
s800 = random.sample(So800, k=1)
d800 = random.sample(dep800, k=1)
v800 = random.sample(vid800, k=1)
l800 = random.sample(lug800, k=1)
m800 = random.sample(mus800, k=1)
pe800 = random.sample(peli800, k=1)

p1000 = random.sample(per1000, k=1)
i1000 = random.sample(IeO1000, k=1)
h1000 = random.sample(Ht1000, k=1)
a1000 = random.sample(Ai1000, k=1)
s1000 = random.sample(So1000, k=1)
d1000 = random.sample(dep1000, k=1)
v1000 = random.sample(vid1000, k=1)
l1000 = random.sample(lug1000, k=1)
m1000 = random.sample(mus1000, k=1)
pe1000 = random.sample(peli1000, k=1)

def selPreguntasRandom(categoria, px, ix, hx, ax, sx, dx, vx, lx, mx, pelx):
    if categoria == "personajes":
        print(px)
    elif categoria == "Iot":
        print(ix)
    elif categoria == "Hacking Tools":
        print(hx)
    elif categoria == "AI":
        print(ax)
    elif categoria == "SO":
        print(sx)
    elif categoria == "Deportes":
        print(dx)
    elif categoria == "Videojuegos":
        print(vx)
    elif categoria == "Lugares":
        print(lx)
    elif categoria == "Música":
        print(mx)
    else:
        print (px)

selPreguntasRandom(cat1, p200, i200, h200, a200, s200, d200, v200, l200, m200, pe200)
selPreguntasRandom(cat2, p400, i400, h400, a400, s400, d400, v400, l400, m400, pe400)
selPreguntasRandom(cat3, p600, i600, h600, a600, s600, d600, v600, l600, m600, pe600)
selPreguntasRandom(cat4, p800, i800, h800, a800, s800, d800, v800, l800, m800, pe800)
selPreguntasRandom(cat5, p1000, i1000, h1000, a1000, s1000, d1000, v1000, l1000, m1000, pe1000)