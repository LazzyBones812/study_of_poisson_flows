import random

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.distributions import chi2

number_in_group = 23
T_1 = number_in_group
T_2 = number_in_group + 100
var_lambda_1 = (number_in_group + 8)/(number_in_group + 24)
var_lambda_2 = (number_in_group + 9)/(number_in_group + 25)
var_lambda_3 = var_lambda_1 + var_lambda_2
xi_1 = []
xi_2 = []
xi_3 = []
u_1 = []
u_2 = []
u_3 = []
t_1 = []
t_2 = []
t_3 = []
u_1_sum = 0
u_2_sum = 0
u_3_sum = 0
stream_1 = [[0 for j in range(100)] for i in range(50)]
stream_2 = [[]]
stream_3 = [[0 for j_1 in range(100)] for i_1 in range(100)]
stream_t_3 = []
xi_3_1 = []

T = 50
SEPARATION = 25
separateY = [-0.5, 0.5]
separateX = np.arange(T_1, T_2 + 4, 4)

x_line_1 = np.linspace(T_1, T_2, 500)
y_line_1 = np.zeros(500)

countInRange_1 = []
countInRange_2 = []
countInRange_3 = []
countInRange_3_1 = []
listInRange_t_1 = []
listInRange_t_2 = []
listInRange_t_3 = []
listInRange_t_3_1 = []
freakInRange_t_1 = []
freakInRange_t_2 = []
freakInRange_t_3 = []
freakInRange_t_3_1 = []
nTheors_1 = []
nTheors_2 = []
nTheors_3 = []
nTheors_3_1 = []
xi_1_res = []
xi_2_res = []
xi_3_res = []
m_1 = []
m_2 = []
m_3 = []
m_3_1 = []
countInRange_1_noDub = []
countInRange_2_noDub = []
countInRange_3_noDub = []

'''fig_1, ax_1 = plt.subplots()
fig_2, ax_2 = plt.subplots()
fig_4, ax_4 = plt.subplots()

for i in range(50):
    ax_1.plot(x_line_1, y_line_1 + i, c="black")
    ax_2.plot(x_line_1, y_line_1 + i, c="black")
    ax_4.plot(x_line_1, y_line_1 + i, c="black")

for i in range(50):
    for sepX in separateX:
        new_list = [x + i for x in separateY]
        ax_1.plot([sepX] * 2, new_list, c="green")
        new_list = [x + i for x in separateY]
        ax_2.plot([sepX] * 2, new_list, c="green")
        new_list = [x + i for x in separateY]
        ax_4.plot([sepX] * 2, new_list, c="green")'''

result_1 = 0
result_2 = 0
result_3 = 0

# Реализация 50 потоков
for number_stream in range(50):
    xi_1.clear()
    u_1.clear()
    t_1.clear()
    u_1_sum = 0
    xi_2.clear()
    u_2.clear()
    t_2.clear()
    u_2_sum = 0
    t_3.clear()
    leftRange = T_1
    rightRange = leftRange + 4
    listInRange_t_1.clear()
    listInRange_t_2.clear()
    listInRange_t_3.clear()
    countInRange_1.clear()
    countInRange_2.clear()
    countInRange_3.clear()
    countInRange_1_noDub.clear()
    countInRange_2_noDub.clear()
    countInRange_3_noDub.clear()
    freakInRange_t_1.clear()
    freakInRange_t_2.clear()
    freakInRange_t_3.clear()
    nTheors_1.clear()
    nTheors_2.clear()
    nTheors_3.clear()
    xi_3.clear()
    xi_1_res.clear()
    xi_2_res.clear()
    xi_3_res.clear()
    i = 0

    # Цикл, в котором реализуется алгоритм построения пуассоновского
    # потока
    while True:
        i = i + 1
        r = random.random()
        xi_1.append(r)
        u_1.append( -(math.log((xi_1[-1]), math.e)) / (var_lambda_1) )
        u_1_sum = u_1[-1] + u_1_sum
        t_1.append(T_1 + u_1_sum)
        if t_1[-1] > T_2:
            t_1.pop()
            break
    i = 0
    while True:
        i = i + 1
        r = random.random()
        xi_2.append(r)
        u_2.append( -(math.log((xi_2[-1]), math.e)) / (var_lambda_2) )
        u_2_sum = u_2[-1] + u_2_sum
        t_2.append(T_1 + u_2_sum)
        if t_2[-1] > T_2:
            t_2.pop()
            break

    # Построение точек на графике
    '''for j in range(len(t_1)):
        ax_1.scatter(t_1[j],
                number_stream,
                marker='.',
                c='red')
    for j in range(len(t_2)):
        ax_2.scatter(t_2[j],
                     number_stream,
                     marker='.',
                     c='red')'''

    # Получение третьего потока путем сложения двух предыдущих
    t_3 = t_1 + t_2

    # Построение точек событий на графике
    '''for j in range(len(t_3)):
        ax_4.scatter(t_3[j],
                     number_stream,
                     marker='.',
                     c='red')'''

    # Получение вариантов - количество значений в определенном
    # промежутке времени
    for i in range(25):
        listInRange_t_1 = list(filter(lambda x: leftRange < x < rightRange, t_1))
        countInRange_1.append(len(listInRange_t_1))
        leftRange = rightRange
        rightRange = leftRange + 4
    leftRange = T_1
    rightRange = leftRange + 4
    for i in range(25):
        listInRange_t_2 = list(filter(lambda x: leftRange < x < rightRange, t_2))
        countInRange_2.append(len(listInRange_t_2))
        leftRange = rightRange
        rightRange = leftRange + 4
    leftRange = T_1
    rightRange = leftRange + 4
    for i in range(25):
        listInRange_t_3 = list(filter(lambda x: leftRange < x < rightRange, t_3))
        countInRange_3.append(len(listInRange_t_3))
        leftRange = rightRange
        rightRange = leftRange + 4

    # Подсчет частоты появления вариантов в потоке
    for n in range(max(countInRange_1) + 1):
        f = list(filter(lambda x: x == n, countInRange_1))
        freakInRange_t_1.append(len(f))
        f.clear()
    for n in range(max(countInRange_2) + 1):
        f = list(filter(lambda x: x == n, countInRange_2))
        freakInRange_t_2.append(len(f))
        f.clear()
    for n in range(max(countInRange_3) + 1):
        f = list(filter(lambda x: x == n, countInRange_3))
        freakInRange_t_3.append(len(f))
        f.clear()

    # Убирваются нули
    freakInRange_t_1 = [i for i in freakInRange_t_1 if i != 0]
    freakInRange_t_2 = [i for i in freakInRange_t_2 if i != 0]
    freakInRange_t_3 = [i for i in freakInRange_t_3 if i != 0]

    # Дублирующиеся значения удаляются и поток сортируется
    countInRange_1_noDub = list(set(countInRange_1))
    countInRange_1_noDub.sort()
    countInRange_2_noDub = list(set(countInRange_2))
    countInRange_2_noDub.sort()
    countInRange_3_noDub = list(set(countInRange_3))
    countInRange_3_noDub.sort()

    # Сумма всех значений частот
    nSum_1 = sum(freakInRange_t_1)
    nSum_2 = sum(freakInRange_t_2)
    nSum_3 = sum(freakInRange_t_3)

    # Находим интенсивность для всех трех потоков
    for g in range(len(freakInRange_t_1)):
        m_1.append(freakInRange_t_1[g] * countInRange_1_noDub[g])
    lambda_1 = (sum(m_1)) / nSum_1
    m_1.clear()
    for g in range(len(freakInRange_t_2)):
        m_2.append(freakInRange_t_2[g] * countInRange_2_noDub[g])
    lambda_2 = (sum(m_2)) / nSum_2
    m_2.clear()
    for g in range(len(freakInRange_t_3)):
        m_3.append(freakInRange_t_3[g] * countInRange_3_noDub[g])
    lambda_3 = (sum(m_3)) / nSum_3
    m_3.clear()

    # Находим теоретическую вероятность и теоретическую частоту вариантов
    for i in range(len(freakInRange_t_1)):
        p_1 = pow(lambda_1, countInRange_1_noDub[i]) / math.factorial(countInRange_1_noDub[i]) * pow(math.e, -lambda_1)
        #nTheor = p_1 * nSum_1
        nTheors_1.append(p_1 * nSum_1)
    for i in range(len(freakInRange_t_2)):
        p_2 = pow(lambda_2, countInRange_2_noDub[i]) / math.factorial(countInRange_2_noDub[i]) * pow(math.e, -lambda_2)
        #nTheor = p_2 * nSum_2
        nTheors_2.append(p_2 * nSum_2)
    for i in range(len(freakInRange_t_3)):
        p_3 = pow(lambda_3, countInRange_3_noDub[i]) / math.factorial(countInRange_3_noDub[i]) * pow(math.e, -lambda_3)
        #nTheor = p_3 * nSum_3
        nTheors_3.append(p_3 * nSum_3)

    # Вычисляем практическое значение критерия кси-квадрата
    for u in range(len(freakInRange_t_1)):
        xi_1_res.append((pow(freakInRange_t_1[u] - nTheors_1[u], 2) / nTheors_1[u]))
    for u in range(len(freakInRange_t_2)):
        xi_2_res.append((pow(freakInRange_t_2[u] - nTheors_2[u], 2) / nTheors_2[u]))
    for u in range(len(freakInRange_t_3)):
        xi_3_res.append((pow(freakInRange_t_3[u] - nTheors_3[u], 2) / nTheors_3[u]))

# Вычисление критического значения критерия кси-квадрат
ch_1 = chi2.ppf(0.05, 23)
ch_2 = chi2.ppf(0.05, 23)
ch_3 = chi2.ppf(0.05, 23)
xi_1_prac = sum(xi_1_res)
xi_2_prac = sum(xi_2_res)
xi_3_prac = sum(xi_3_res)

print()
print("Лямбда практического первого потока = ", var_lambda_1)
print("Лямбда практического второго потока = ", var_lambda_2)
print("Лямбда практического потока, полученный из первого и второго потока = ", var_lambda_1 + var_lambda_2)
print()
print("Лямбда теоретического первого потока = ", lambda_1 / 4)
print("Лямбда теоретического второго потока = ", lambda_2 / 4)
print("Лямбда теоретического потока, полученный из первого и второго потока = ", lambda_3 / 4)
print()

print("Хи-квадрат критическое = ", ch_3)
print("Хи-квадрат практическое 1 = ", xi_1_prac)
print("Хи-квадрат практическое 2 = ", xi_2_prac)
print("Хи-квадрат практическое 1&2 = ", xi_3_prac)
print()

# Принимаем решение, является ли поток пуассоновским
if xi_1_prac < ch_1:
    print('Гипотеза о пуассоновском потоке принимается для потока t_1')
    result_1 += 1
else:
    print('Гипотеза о пуассоновском потоке отвергается для потока t_1')

if xi_2_prac < ch_2:
    print('Гипотеза о пуассоновском потоке принимается для потока t_2')
    result_2 += 1
else:
    print('Гипотеза о пуассоновском потоке отвергается для потока t_2')

if xi_3_prac < ch_3:
    print('Гипотеза о пуассоновском потоке принимается для потока t_3')
    result_3 += 1
else:
    print('Гипотеза о пуассоновском потоке отвергается для потока t_3')
print()

'''fig_1.set_figwidth(12)
fig_1.set_figheight(6)
fig_1.set_facecolor('floralwhite')
ax_1.set_facecolor('seashell')
fig_2.set_figwidth(12)
fig_2.set_figheight(6)
fig_2.set_facecolor('floralwhite')
ax_2.set_facecolor('seashell')
fig_4.set_figwidth(12)
fig_4.set_figheight(6)
fig_4.set_facecolor('floralwhite')
ax_4.set_facecolor('seashell')

fig_3, ax_3 = plt.subplots()

for i in range(50):
    ax_3.plot(x_line_1, y_line_1 + i, c="black")

for i in range(50):
    for sepX in separateX:
        new_list = [x + i for x in separateY]
        ax_3.plot([sepX] * 2, new_list, c="green")'''

for number_stream in range(50):
    xi_3.clear()
    u_3.clear()
    t_3.clear()
    u_3_sum = 0
    nTheors_3_1.clear()
    xi_3_1.clear()
    leftRange = T_1
    rightRange = leftRange + 4
    listInRange_t_3_1.clear()
    freakInRange_t_3_1.clear()
    countInRange_3_1.clear()
    xi_3_1.clear()
    while True:
        r = random.random()
        xi_3.append(r)
        u_3.append( -(math.log(xi_3[-1]))/ (var_lambda_3) )
        u_3_sum = u_3[-1] + u_3_sum
        t_3.append(T_1 + u_3_sum)
        if t_3[-1] > T_2:
            t_3.pop()
            break
    '''for j in range(len(t_3)):
        ax_3.scatter(t_3[j],
                     number_stream,
                     marker='.',
                     c='red')'''

    for i in range(25):
        listInRange_t_3_1 = list(filter(lambda x: leftRange < x < rightRange, t_3))
        countInRange_3_1.append(len(listInRange_t_3_1))
        leftRange = rightRange
        rightRange = leftRange + 4

    for n in range(max(countInRange_3_1)):
        f = list(filter(lambda x: x == n, countInRange_3_1))
        freakInRange_t_3_1.append(len(f))
        f.clear()

    nSum_3_1 = sum(freakInRange_t_3_1)

    for g in range(len(freakInRange_t_3_1)):
        m_3_1.append(freakInRange_t_3_1[g] * g)
    lambda_3_1 = (sum(m_3_1)) / nSum_3_1
    m_3_1.clear()

    for i in range(len(freakInRange_t_3_1)):
        p_3_1 = (pow(lambda_3_1, i) / math.factorial(i)) * pow(math.e, -lambda_3_1)
        nTheor = p_3_1 * nSum_3_1
        nTheors_3_1.append(p_3_1 * nSum_3_1)

    for u in range(len(freakInRange_t_3_1)):
        xi_3_1.append((pow(freakInRange_t_3_1[u] - nTheors_3_1[u], 2) / nTheors_3_1[u]))

ch_3 = chi2.ppf(0.05, 23)
xi_3_1_prac = sum(xi_3_1)

print()
print("Лямбда практического третьего потока = ", var_lambda_3)
print("Лямбда теоретического третьего потока = ", lambda_3_1 / 4)
print()
print("Хи-квадрат критическое = ", ch_3)
print("Хи-квадрат практического третьего потока = ",xi_3_1_prac)
print()

if xi_3_1_prac < ch_3:
    print('Гипотеза о пуассоновском потоке принимается для потока t_3_1')
else:
    print('Гипотеза о пуассоновском потоке отвергается для потока t_3_1')

'''fig_3.set_figwidth(12)
fig_3.set_figheight(6)
fig_3.set_facecolor('floralwhite')
ax_3.set_facecolor('seashell')'''

#plt.show()


