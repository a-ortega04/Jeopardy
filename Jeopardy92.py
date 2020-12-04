from graphics import *
from Question import *
from funciones import *
import random

win = GraphWin("ventana", 1100, 750)
win.setBackground('blue')

categorias = ["Personajes", "IoT", "Hacking Tools", "AI", "SO", "Deportes", "Videojuegos", "Lugares", "Música", "Películas"]

texto = random.sample(categorias, k=6)

answered = []

cat1 = texto[0]
cat2 = texto[1]
cat3 = texto[2]
cat4 = texto[3]
cat5 = texto[4]
cat6 = texto[5]

dinero = ["--------", "200", "400", "600", "800", "1,000"]

nulo1 = dinero[0]
premio11 = dinero[1]
premio12 = dinero[2]
premio13 = dinero[3]
premio14 = dinero[4]
premio15 = dinero[5]

nulo2 = dinero[0]
premio21 = dinero[1]
premio22 = dinero[2]
premio23 = dinero[3]
premio24 = dinero[4]
premio25 = dinero[5]

nulo3 = dinero[0]
premio31 = dinero[1]
premio32 = dinero[2]
premio33 = dinero[3]
premio34 = dinero[4]
premio35 = dinero[5]

nulo4 = dinero[0]
premio41 = dinero[1]
premio42 = dinero[2]
premio43 = dinero[3]
premio44 = dinero[4]
premio45 = dinero[5]

nulo5 = dinero[0]
premio51 = dinero[1]
premio52 = dinero[2]
premio53 = dinero[3]
premio54 = dinero[4]
premio55 = dinero[5]

nulo6 = dinero[0]
premio61 = dinero[1]
premio62 = dinero[2]
premio63 = dinero[3]
premio64 = dinero[4]
premio65 = dinero[5]


def gridCategorias():
    def funGC(sx, x1, x2, x3, cat):
        sx = Rectangle(Point(x1, 50), Point(x2, 150))
        sx.draw(win)
        sx.setFill('white')
        txt = Text(Point(x3, 97), cat)
        txt.setSize(12)
        txt.setFace('courier')
        txt.draw(win)

    funGC(1, 50, 216.66, 125, cat1)
    funGC(2, 216.66, 383.33, 291.66, cat2)
    funGC(3, 383.33, 549.99, 458.32, cat3)
    funGC(4, 549.99, 716.66, 624.99, cat4)
    funGC(5, 716.66, 883.33, 791.66, cat5)
    funGC(6, 883.33, 1049.99, 958.33, cat6)

def gridPreguntas1():
    def funGP1(rx, y1, y2, y3, premio):
        rx = Rectangle(Point(50, y1), Point(216.66, y2))
        rx.draw(win)
        rx.setFill('cyan')
        txt = Text(Point(133, y3), premio)
        txt.setSize(16)
        txt.setFace('courier')
        txt.draw(win)

    funGP1(1, 150, 250, 200, premio11)
    funGP1(2, 250, 350, 300, premio12)
    funGP1(3, 350, 450, 400, premio13)
    funGP1(4, 450, 550, 500, premio14)
    funGP1(5, 550, 650, 600, premio15)

def gridPreguntas2():
    def funGP1(rx, y1, y2, y3, premio):
            rx = Rectangle(Point(216.66, y1), Point(383.33, y2))
            rx.draw(win)
            rx.setFill('cyan')
            txt = Text(Point(299.66, y3), premio)
            txt.setSize(16)
            txt.setFace('courier')
            txt.draw(win)

    funGP1(1, 150, 250, 200, premio21)
    funGP1(2, 250, 350, 300, premio22)
    funGP1(3, 350, 450, 400, premio23)
    funGP1(4, 450, 550, 500, premio24)
    funGP1(5, 550, 650, 600, premio25)

def gridPreguntas3():
    def funGP1(rx, y1, y2, y3, premio):
            rx = Rectangle(Point(383.33, y1), Point(549.99, y2))
            rx.draw(win)
            rx.setFill('cyan')
            txt = Text(Point(466.33, y3), premio)
            txt.setSize(16)
            txt.setFace('courier')
            txt.draw(win)

    funGP1(1, 150, 250, 200, premio31)
    funGP1(2, 250, 350, 300, premio32)
    funGP1(3, 350, 450, 400, premio33)
    funGP1(4, 450, 550, 500, premio34)
    funGP1(5, 550, 650, 600, premio35)

def gridPreguntas4():
    def funGP1(rx, y1, y2, y3, premio):
        rx = Rectangle(Point(549.99, y1), Point(716.66, y2))
        rx.draw(win)
        rx.setFill('cyan')
        txt = Text(Point(633.99, y3), premio)
        txt.setSize(16)
        txt.setFace('courier')
        txt.draw(win)

    funGP1(1, 150, 250, 200, premio41)
    funGP1(2, 250, 350, 300, premio42)
    funGP1(3, 350, 450, 400, premio43)
    funGP1(4, 450, 550, 500, premio44)
    funGP1(5, 550, 650, 600, premio45)

def gridPreguntas5():
    def funGP1(rx, y1, y2, y3, premio):
        rx = Rectangle(Point(716.66, y1), Point(883.33, y2))
        rx.draw(win)
        rx.setFill('cyan')
        txt = Text(Point(800.66, y3), premio)
        txt.setSize(16)
        txt.setFace('courier')
        txt.draw(win)

    funGP1(1, 150, 250, 200, premio51)
    funGP1(2, 250, 350, 300, premio52)
    funGP1(3, 350, 450, 400, premio53)
    funGP1(4, 450, 550, 500, premio54)
    funGP1(5, 550, 650, 600, premio55)

def gridPreguntas6():
    def funGP1(rx, y1, y2, y3, premio):
        rx = Rectangle(Point(883.33, y1), Point(1049.99, y2))
        rx.draw(win)
        rx.setFill('cyan')
        txt = Text(Point(966.33, y3), premio)
        txt.setSize(16)
        txt.setFace('courier')
        txt.draw(win)

    funGP1(1, 150, 250, 200, premio61)
    funGP1(2, 250, 350, 300, premio62)
    funGP1(3, 350, 450, 400, premio63)
    funGP1(4, 450, 550, 500, premio64)
    funGP1(5, 550, 650, 600, premio65)

def reglas():
    print("Jeopardy!!!!!!!!!!!!!!!!!!")
    print("haz click en el numero para obtener tu pregunta")
    print("contesta en el programa con la letra de la respuesta solamente")

def gridPreguntasTotal():
    gridPreguntas1()
    gridPreguntas2()
    gridPreguntas3()
    gridPreguntas4()
    gridPreguntas5()
    gridPreguntas6()

reglas()
gridCategorias()
gridPreguntasTotal()

while len(answered) < 30:
    dinero = 0
    tier1 = 200
    tier2 = 400
    tier3 = 600
    tier4 = 800
    tier5 = 1000

    click = win.getMouse()
    posX = click.getX()
    posY = click.getY()

    if 50 < posX < 216.66 and 150 < posY < 250 and not 'c1_200' in answered:
        pregunta = selPreguntasRandom(cat1, p200, i200, h200, a200, s200, d200, v200, l200, m200, pe200)
        answered.append('c1_200')
        respuesta = pregunta['answer']
        print(pregunta['prompt'])
        keyString = win.getKey()
        if keyString == respuesta:
            dinero += 200
            print("Respuesta correcta. +$200. Tu dinero:", dinero) 
        else:
            dinero -= 200
            print("Respuesta incorrecta. -$200. Tu dinero:", dinero)
        premio11 = nulo1
    if 50 < posX < 216.66 and 250 < posY < 350:
        selPreguntasRandom(cat1, p400, i400, h400, a400, s400, d400, v400, l400, m400, pe400)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio12 = nulo1
    if 50 < posX < 216.66 and 350 < posY < 450:
        selPreguntasRandom(cat1, p600, i600, h600, a600, s600, d600, v600, l600, m600, pe600)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio13 = nulo1
    if 50 < posX < 216.66 and 450 < posY < 550:
        selPreguntasRandom(cat1, p800, i800, h800, a800, s800, d800, v800, l800, m800, pe800)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio14 = nulo1
    if 50 < posX < 216.66 and 550 < posY < 650:
        selPreguntasRandom(cat1, p1000, i1000, h1000, a1000, s1000, d1000, v1000, l1000, m1000, pe1000)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio15 = nulo1
    # columna 2
    elif 216.66 < posX < 383.33 and 150 < posY < 250:
        selPreguntasRandom(cat2, p200, i200, h200, a200, s200, d200, v200, l200, m200, pe200)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio21 = nulo2
    if 216.66 < posX < 383.33 and 250 < posY < 350:
        selPreguntasRandom(cat2, p400, i400, h400, a400, s400, d400, v400, l400, m400, pe400)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio22 = nulo2
    if 216.66 < posX < 383.33 and 350 < posY < 450:
        selPreguntasRandom(cat2, p600, i600, h600, a600, s600, d600, v600, l600, m600, pe600)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio23 = nulo2
    if 216.66 < posX < 383.33 and 450 < posY < 550:
        selPreguntasRandom(cat2, p800, i800, h800, a800, s800, d800, v800, l800, m800, pe800)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio24 = nulo2
    if 216.66 < posX < 383.33 and 550 < posY < 650:
        selPreguntasRandom(cat2, p1000, i1000, h1000, a1000, s1000, d1000, v1000, l1000, m1000, pe1000)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio25 = nulo2

    # columna3
    if 383.33 < posX < 549.99 and 150 < posY < 250:
        selPreguntasRandom(cat3, p200, i200, h200, a200, s200, d200, v200, l200, m200, pe200)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio31 = nulo3
    if 383.33 < posX < 549.99 and 250 < posY < 350:
        selPreguntasRandom(cat3, p400, i400, h400, a400, s400, d400, v400, l400, m400, pe400)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio32 = nulo3
    if 383.33 < posX < 549.99 and 350 < posY < 450:
        selPreguntasRandom(cat3, p600, i600, h600, a600, s600, d600, v600, l600, m600, pe600)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio33 = nulo3
    if 383.33 < posX < 549.99 and 450 < posY < 550:
        selPreguntasRandom(cat3, p800, i800, h800, a800, s800, d800, v800, l800, m800, pe800)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio34 = nulo3
    if 383.33 < posX < 549.99 and 550 < posY < 650:
        selPreguntasRandom(cat3, p1000, i1000, h1000, a1000, s1000, d1000, v1000, l1000, m1000, pe1000)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio35 = nulo3
    # columna4
    if 549.99 < posX < 716.66 and 150 < posY < 250:
        selPreguntasRandom(cat4, p200, i200, h200, a200, s200, d200, v200, l200, m200, pe200)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio41 = nulo4
    if 549.99 < posX < 716.66 and 250 < posY < 350:
        selPreguntasRandom(cat4, p400, i400, h400, a400, s400, d400, v400, l400, m400, pe400)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio42 = nulo4
    if 549.99 < posX < 716.66 and 350 < posY < 450:
        selPreguntasRandom(cat4, p600, i600, h600, a600, s600, d600, v600, l600, m600, pe600)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio43 = nulo4
    if 549.99 < posX < 716.66 and 450 < posY < 550:
        selPreguntasRandom(cat4, p800, i800, h800, a800, s800, d800, v800, l800, m800, pe800)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio44 = nulo4
    if 549.99 < posX < 716.66 and 550 < posY < 650:
        selPreguntasRandom(cat4, p1000, i1000, h1000, a1000, s1000, d1000, v1000, l1000, m1000, pe1000)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio45 = nulo4
    # columna5
    if 716.66 < posX < 883.33 and 150 < posY < 250:
        selPreguntasRandom(cat5, p200, i200, h200, a200, s200, d200, v200, l200, m200, pe200)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio51 = nulo5
    if 716.66 < posX < 883.33 and 250 < posY < 350:
        selPreguntasRandom(cat5, p400, i400, h400, a400, s400, d400, v400, l400, m400, pe400)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio52 = nulo5
    if 716.66 < posX < 883.33 and 350 < posY < 450:
        selPreguntasRandom(cat5, p600, i600, h600, a600, s600, d600, v600, l600, m600, pe600)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio53 = nulo5
    if 716.66 < posX < 883.33 and 450 < posY < 550:
        selPreguntasRandom(cat5, p800, i800, h800, a800, s800, d800, v800, l800, m800, pe800)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio54 = nulo5
    if 716.66 < posX < 883.33 and 550 < posY < 650:
        selPreguntasRandom(cat5, p1000, i1000, h1000, a1000, s1000, d1000, v1000, l1000, m1000, pe1000)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio55 = nulo5
    # columna6
    if 883.33 < posX < 1049.99 and 150 < posY < 250:
        selPreguntasRandom(cat6, p200, i200, h200, a200, s200, d200, v200, l200, m200, pe200)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio61 = nulo6
    if 883.33 < posX < 1049.99 and 250 < posY < 350:
        selPreguntasRandom(cat6, p400, i400, h400, a400, s400, d400, v400, l400, m400, pe400)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio62 = nulo6
    if 883.33 < posX < 1049.99 and 350 < posY < 450:
        selPreguntasRandom(cat6, p600, i600, h600, a600, s600, d600, v600, l600, m600, pe600)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio63 = nulo6
    if 883.33 < posX < 1049.99 and 450 < posY < 550:
        selPreguntasRandom(cat6, p800, i800, h800, a800, s800, d800, v800, l800, m800, pe800)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio64 = nulo6
    if 883.33 < posX < 1049.99 and 550 < posY < 650:
        selPreguntasRandom(cat6, p1000, i1000, h1000, a1000, s1000, d1000, v1000, l1000, m1000, pe1000)
        respuesta = "a"
        keyString = win.getKey()
        if keyString == respuesta:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
        premio65 = nulo6
    gridPreguntasTotal()

win.getMouse()
win.close()
