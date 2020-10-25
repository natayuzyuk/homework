def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def create_two_dicts(x, y):
    z = merge_two_dicts(dict(x), dict(y))
    print(z)


x = {"a": 1, "b": 2, "c": 3}
y = {"c": 4, "e": 5, "f": 6}

create_two_dicts(x, y)
