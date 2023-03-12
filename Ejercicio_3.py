green = 1
blue = 2
red = 3

numero_color = {1: "green", 2: "blue", 3: "red"}

colores = [ red , blue, blue, red, green, blue, blue, red, green, red, blue, green  ]

def ordenar(colores):
    red = 1
    blue = 2
    green = 3
    for i in range(len(colores)):
        for x in range(len(colores)-1):
            if colores[x] > colores[x+1]:
                colores[x], colores[x+1] = colores[x+1], colores[x]
    return colores

colores_ordenados = ordenar(colores)
for num in colores_ordenados:
    print(numero_color[num])