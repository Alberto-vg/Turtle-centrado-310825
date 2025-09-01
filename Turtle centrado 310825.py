#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 22:35:42 2025

@author: albertovargas
"""

import turtle


turtle.setup(800, 600)  # Tamaño de la ventana

turtle.penup()           # Levantar el lápiz
turtle.goto(-200, -100)  # Ajustar posición para centrar el fractal
turtle.pendown()         # Bajar el lápiz


rr = 'F-G-G'
r1 = 'F-G+F+G-F'
r2 = 'GG'
teta = 120
numiter = 4


for i in range(numiter):
    tem = ''
    for ss in rr:
        if ss == 'F':
            tem = tem + r1
        elif ss == 'G':
            tem = tem + r2
        else:
            tem = tem + ss
    rr = tem


S = rr
for ss in S:
    if ss == 'F' or ss == 'G':
        turtle.forward(10)  # Reducir tamaño para mejor visualización
    elif ss == '-':
        turtle.right(teta)
    else:
        turtle.left(teta)


turtle.mainloop()



