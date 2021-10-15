#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import array

#Uriarte Avelar Jesus Eduardo

print('\n')
print('')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('|Problema del paracaidista|')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-')


G = 9.8
t_inicial = 0
v_inicial = 0
idx = 0
v_final = 1


m = float(input('Ingresa el valor de la masa en kg: '))
c = float(input('Ingresa el valor del coeficiente de resistencia en kg/s: '))

delta_time = 2.0
t_final = delta_time

#ejes para graficar
x_axys = [t_inicial]
y_axys = [v_inicial]

#Uso del ciclo while
while  (v_inicial % v_final)!=0:
    v_final = v_inicial
    print('v_{} = {} m/s'.format(idx,round(v_final,4)))
    v_final = v_inicial + (G - ((c/m)*v_inicial)) * (t_final - t_inicial)

    x_axys.append(int(t_final))
    y_axys.append(v_final)
    v_inicial = v_final
    t_inicial = t_final
    t_final += delta_time
    idx += 1

print(x_axys)
print(y_axys)
plt.plot(x_axys,y_axys)
plt.axis([0, 18, 0, 60])
plt.show()