import random

per200 = [
    {
        'prompt': "¿Quién fue Alan Turing? A:creador de la máquina de turing B:inventor de los booleanos C:el primo de alberto",
        'answer': 'a'
    },
    {
        'prompt': "qué compañía fundó Steve Jobs? A: Windows B:Apple C:Amazon",
        'answer': "B"
    }
]

p200 = random.choice(per200)

print(p200['prompt'])
print(p200['answer'])


def selPreguntasRandom(categoria, px, ix, hx, ax, sx, dx, vx, lx, mx, pelx):
    if categoria == "personajes":
        return px
    elif categoria == "Iot":
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
