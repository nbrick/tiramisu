xs = [1, 3, 5, 3]

mySum = 4

xs.append(-mySum)

a = sum(filter(lambda x: x < 0, xs))
b = sum(filter(lambda x: x > 0, xs))

q = {}

for s in range(a, b + 1):
    q[(1, s)] = xs[0] == s

print(q)

q = {}

# print(sorted(xs))
