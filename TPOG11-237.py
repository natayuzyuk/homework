def maptolist(map) :
    lst = list(map)
    print("первый элемент списка: {0}".format(lst[0]))
    print("последний элемент списка: {0}".format(lst[len(lst)-1]))
maptolist(map(int, input("Введите целые значения через пробел: ").split()))
