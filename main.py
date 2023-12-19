# Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні,
# вивести їх на екран у порядку зростання


while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if num1 == num2:
            print("Числа рівні.")
        else:
            sorted_numbers = sorted([num1, num2])
            print("Числа у порядку зростання:", sorted_numbers)

    except ValueError:
        print("Невірне введення. Будь ласка, введіть числа.")
