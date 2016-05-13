def find_outlier(integers):
    if integers[0] % 2 == 0 and integers[1] % 2 == 0:
        for i in range(2, len(integers)):
            if integers[i] % 2 != 0:
                return integers[i]
    elif integers[0] % 2 != 0 and integers[1] % 2 != 0:
        for i in range(2, len(integers)):
            if integers[i] % 2 == 0:
                return integers[i]
    elif integers[0] % 2 == 0 and integers[1] % 2 != 0 and integers[2] % 2 == 0:
        return integers[1]
    elif integers[0] % 2 != 0 and integers[1] % 2 == 0 and integers[2] % 2 != 0:
        return integers[1]
    elif integers[0] % 2 != 0 and integers[1] % 2 == 0 and integers[1] % 2 == 0:
        return integers[0]
    elif integers[0] % 2 == 0 and integers[1] % 2 != 0 and integers[1] % 2 != 0:
        return integers[0]
    else:
        return 0


def find_outlier_expr(integers):
    odds = [x for x in integers if x % 2 != 0]
    evens = [x for x in integers if x % 2 == 0]

    return odds[0] if len(odds) < len(evens) else evens[0]


def find_outlier_lambda(integers):
    odds = filter(lambda x: x % 2 != 0, integers)
    evens = filter(lambda x: x % 2 == 0, integers)

    return odds[0] if len(odds) < len(evens) else evens[0]