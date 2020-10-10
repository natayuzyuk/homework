# Пока While не разлучит нас
def dosomething(A, B, C) :
    while A <= B:
        print("Значение A {0} пока что нет".format(A))
        A = A + C
    print("Дождались! Финальный A : {0}".format(A))

A=float(input("Введите число A: "))
B=float(input("Введите число B: "))
C=float(input("Введите число C: "))

dosomething(A, B, C)