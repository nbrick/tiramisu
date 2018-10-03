xs = [1, 3, 5, 3]

mySum = 4

xs.append(-mySum)


def q(i, s, subset):
    if i == 0:
        r = xs[i] == s
        if r:
            subset.append(xs[i])
        return r
    else:
        r = q(i - 1, s - xs[i], subset)
        if r:
            subset.append(xs[i])
        return any([r, q(i - 1, s, subset), xs[i] == s])


subset = []

q(len(xs) - 1, 0, subset)

print(subset)
