# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint     # необходима данная библиотека

n_multiplicity = set(randint(1, 20) for i in range(int(input("Пожалуйста, введите кол-во элементов первого множества: "))))
print(n_multiplicity)

m_multiplicity = set(randint(1, 20) for i in range(int(input("Пожалуйста, введите кол-во элементов второго множества: "))))
print(m_multiplicity)

sort_multiplicity = sorted(n_multiplicity.intersection(m_multiplicity))      # сортировка элементов множества
print(*sort_multiplicity)