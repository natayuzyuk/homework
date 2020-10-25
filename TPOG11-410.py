num = int(input("Введите целое: "))
sum1 = 0
while num != 0:
    sum1 = sum1 + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum1)
