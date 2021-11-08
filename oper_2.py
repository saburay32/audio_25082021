

# def g(x):
# 	y = []
# 	for i in range(x+1):
# 		n = x - i
# 		y.append(sum([int(j) for j in str(i)]) + sum([int(j) for j in str(n)]))
# 	print('X = ', x,'MAX = ',max(y), '  MIN = ', min(y), min(y) == max(y))
#
#
# g(int(input()))

#---------------------------------------
# a,b = map(int,(input().split()))
# if (a+b)%2==1:
#     print('Замостить можно')
# else:
#     print('Замостить нельзя')
#------------------------

# s = [int(i) for i in input().split()]
# if len(s)<2:
#     print('Ошибка. Кучек слишком мало, чтобы можно было решить задачу.')
# elif len(s)==2 and s[0]!=s[1]:
#         print('Кучки нельзя уравнять')
# else:
#     z = True
#
#     for i in range(len(s) - 1):
#         if s[i] != s[i + 1]:
#             z = False
#             break
#
#     if z == True:
#         print('Кучки можно уравнять')
#
#     elif z == False:
#         if len(s) % 2 == 0 and (sum(s) % 2 == 0):
#             print('Кучки можно уравнять')
#         elif len(s) % 2 == 1 and (sum(s) % 2 == 1):
#             print('Кучки можно уравнять')
#         elif len(s) % 2 == 1 and (sum(s) % 2 == 0):
#             print('Кучки можно уравнять')
#         else:
#             print('Кучки нельзя уравнять')







#-----------------
# from scipy.optimize import golden
#
# a = 3
# b = 4
#
# def f(x):
#     return (x+a)**2-b
#
# def g(x):
#     return abs(f(x))
#
# min_f = golden(f,brack=(-10,-4))
# min_g = golden(g,brack=(-10,-4))
#
# print(f(min_f), g(min_g))
#-------------------------
#import math
#
# a = int(input())
#
# def S(x):
#     s_5 = ((5**0.5)*((5+2*(5**0.5))**0.5))/4*(x**2)
#     s_6 = (3*(3**0.5))/2*(x**2)
#     return 20*s_6+12*s_5
#
#
# def S_ceil(x):
#     return math.ceil(S(x))
#
# print(S(a))
# print(S_ceil(a))
# #------------
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# #Для следующего задания используйте 6 точек: (0,1), (1,1), (2,25), (-1,1), (-2,-23), (0.5,0.90625)
# ins = [[0,1], [1,1], [2,25], [-1,1], [-2,-23], [0.5,0.90625]]
# #M = int(input())
# M = len(ins)
# M1 = np.zeros(M*M).reshape(M,M)
# v = np.zeros(M)
# answer = []
# for i in range(M):
#     x = ins[i][0]
#     #x,y = ([float(i) for i in input().split()])
#     v[i] = ins[i][1]
#     for e in range(M):
#         M1[i][e] = x**e
#
# if np.linalg.det(M1)!=0:
#     z =np.linalg.solve(M1,v)
#     #for i in range(len(z)):
#         #print(z[i],end=' ')
# else:
#     print( "Матрица системы вырожденная")
#
# c = z
#
# def f(x, c):
#     return c[0]+c[1]*x+c[2]*x**2+c[3]*x**3+c[4]*x**4+c[5]*x**5
#
#
# # x = np.arange(0, 5.01, 0.1) #Массив значений аргумента
# # plt.plot(x, f(x, c)) #Построение графика
# # plt.xlabel(r'$x$') #Метка по оси x в формате TeX
# # plt.ylabel(r'$f(x)$') #Метка по оси y в формате TeX
# # plt.grid(True) #Сетка
# # plt.show() #Показать график
# x = -0.802630
# print(f(x,c))