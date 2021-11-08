import numpy as np
import matplotlib.pyplot as plt


#Для следующего задания используйте 6 точек: (0,1), (1,1), (2,25), (-1,1), (-2,-23), (0.5,0.90625)
ins = [[0,1], [1,1], [2,25], [-1,1], [-2,-23], [0.5,0.90625]]
#M = int(input())
M = len(ins)
M1 = np.zeros(M*M).reshape(M,M)
v = np.zeros(M)
answer = []
for i in range(M):
    x = ins[i][0]
    #x,y = ([float(i) for i in input().split()])
    v[i] = ins[i][1]
    for e in range(M):
        M1[i][e] = x**e
c = [1., 1., 25., 1., -23.,0.90625]

def f(x, c):
    return c[0]+c[1]*x+c[2]*x**2+c[3]*x**3+c[4]*x**4+c[5]*x**5


x = np.arange(-7.01, 7.01, 0.01) #Массив значений аргумента
plt.plot(x, f(x, c)) #Построение графика
plt.xlabel(r'$x$') #Метка по оси x в формате TeX
plt.ylabel(r'$f(x)$') #Метка по оси y в формате TeX
plt.grid(True) #Сетка
plt.show() #Показать график
#
# if np.linalg.det(M1)!=0:
#     z =np.linalg.solve(M1,v)
#     for i in range(len(z)):
#         print(z[i],end=' ')
# else:
#     print( "Матрица системы вырожденная")




# if np.linalg.det(M1)!=0:
#     z =np.linalg.solve(M1,v1)
#     print(float(z[0]),float(z[1]),float(z[2]))
# else:
#     print( "Матрица системы вырожденная")

# import numpy # импортируем библиотеку
# a = [int(s) for s in input().split()]
# b = [int(s) for s in input().split()]
# c = [int(s) for s in input().split()]
# M1 = np.array([a[:3],b[:3],c[:3]])
# v1 = np.array([a[-1],b[-1],c[-1]])
# M1 = np.array([[1,-2,4],
#               [1,2,4],
#               [1,0,0]])
# v1 = np.array([0,0,-4])
# if np.linalg.det(M1)!=0:
#     z =np.linalg.solve(M1,v1)
#     print(float(z[0]),float(z[1]),float(z[2]))
# else:
#     print( "Матрица системы вырожденная")
#------------------
# a, b = ([int(i) for i in input().split()])
#
# if b <= a and (a + b) % 2 == 0  :
#     print((a + b) // 2, (a - b) // 2)
# else:
#     print("Такой класс не существует")


#-----------------
# import plotly
# import plotly.graph_objs as go
# import plotly.express as px
# from plotly.subplots import make_subplots
#
# import numpy as np
# import pandas as pd
#
# x = np.arange(0,5,0.1)
#
# def f(x):
#     return x**2
#
# fig = px.scatter(x=x,y=f(x))
# fig.show()



#----------------------------------------------------------

# import numpy
# import matplotlib as mpl
# import matplotlib.pyplot as plt
#
# M6 = numpy.array([[1., 1., 1.], [1., -1., 1], [2, 1, 0]]) # Матрица (левая часть системы)
# v6 = numpy.array([1., 1., 1.]) # Вектор (правая часть системы)
#
# mpl.rc('font',family = 'Verdana',size = 16)
# w = numpy.linalg.solve(M6, v6) # запишем найденные коэффициенты в переменную
# def f(x):
#     return w[0]*x**2 + w[1]*x + w[2] # уравнение параболы
#
#
# fig, ax = plt.subplots(figsize=(10,5))
#
# x = numpy.linspace(-2,2,200)
# ax.axis([-2., 2., 0., 2.])
# ax.grid()
# ax.plot(x, f(x), label = 'Парабола')
# ax.plot(x, x, label = 'Биссектриса 1й\nкоординатной четверти')
# ax.set_xlabel(u'x',{'fontname':'Arial', 'size': 24})
# ax.set_ylabel(u'f(x)',{'fontname':'Arial', 'size': 24})
# plt.plot([-1, 1], [1, 1], 'ro', label = 'Точки для\nпостроения графика')
# ax.annotate('Точка\nкасания', xy=(1., 1.), xytext=(1.5, 0.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )
#
# ax.legend(bbox_to_anchor=(1.6, 1.))
#
# plt.show()
#
# plt.show()


#___________________________________________
# import numpy as np
#
# M1 = np.array([[2.,5.],[1.,-10.]])
# v1 = np.array([1.,3.])
#
# ans = np.linalg.solve(M1,v1)
# print(ans[0])


