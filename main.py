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
        if q(i - 1, s - xs[i], subset):
            subset.append(xs[i])
            return True
        else:
            return q(i - 1, s, subset) or xs[i] == s

subset = []

q(len(xs) - 1, 0, subset)

print(subset)
