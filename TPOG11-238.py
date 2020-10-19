import random
def fn():
    lst1 = random.sample(range(1, 100), 10)
    lst2 = random.sample(range(1, 100), 10)
    lst3 = []
    print(lst1)
    print(lst2)
    for idx in range(len(lst1)):
        if lst1[idx] in lst2:
            lst3.append(lst1[idx])

    print(lst3)
fn()