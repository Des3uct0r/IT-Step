# print("Hi Max!")
#
# n = input("Введіть своє ім'я: ")
# a= int(input("Введіть свій вік: "))
# print(f"Привіт {n}, тобі {a}!")
#
#
# a = int(input("Введіть свій вік: "))
# if a >= 18:
#     print("Вхід дозволено!")
# else:
#     print("Вхід заборонено!")
#
#
#
# import random
#
# num = random.randint(1, 10)
# a = 3
#
# print("Choose from 1 to 10")
#
# while a > 0:
#     g = int(input("Number: "))
#     if g == num:
#         print("Win!")
#     elif g > num:
#         print("-")
#     else:
#         print("+")
#     a -= 1
#
# if a == 0:
#     print("You losed")
#
#
# O_n = int(input("First number: "))
# S_n = int(input("Second number: "))
#
# if O_n > S_n:
#     O_n, S_n = S_n, O_n
#
# for i in range(O_n, S_n + 1):
#     print(i, S_n=" ")
#
#
# n = int(input("Write number: "))
#
# for i in range(n, 0, -1):
#     if i % 2 == 0:
#         print(i, end=" ")
#
#
#
# n = int(input("Write number "))
# f = 1
#
# for i in range(1, n + 1):
#     f *= i
#
# print(f"Factorial: {n}: {f}")
#
#
#
# score = int(input("How many points do you have "))
#
# if 0 <= score <= 49:
#     print("BAd")
# elif 50 <= score <= 69:
#     print("Normal")
# elif 70 <= score <= 89:
#     print("Good")
# elif 90 <= score <= 100:
#     print("Amazing")
# else:
#     print("WTF did you write???!!!")
