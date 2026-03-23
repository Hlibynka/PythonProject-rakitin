import math_logic
from validation import is_valid_number

a = input("Введіть перше число: ")
b = input("Введіть друге число: ")

if is_valid_number(a) and is_valid_number(b):
    print("Результат додавання:", math_logic.add(float(a), float(b)))
else:
    print("Помилка: введено некоректні дані! Будь ласка, вводьте лише числа.")