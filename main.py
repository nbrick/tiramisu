xs = [1, 3, 5, 3]

mySum = 4

xs.append(-mySum)


def q(i, s):
    if i == 0:
        r = xs[i] == s
        if r:
            print(xs[i])
        return r
    else:
        if q(i - 1, s - xs[i]):
            print(xs[i])
            return True
        else:
            return q(i - 1, s) or xs[i] == s


q(len(xs) - 1, 0)
