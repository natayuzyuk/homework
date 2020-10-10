# Пока While не разлучит нас
def dosomething(A, B, C) :
    while A <= B:
        print("Значение A {0} пока что нет".format(A))
        A = A + C
    print("Дождались! Финальный A : {0}".format(A))

A=float(input("введите число A: "))
B=float(input("введите число B: "))
C=float(input("введите число C: "))

dosomething(A, B, C)