from pprint import pprint

xs = [1, 3, 5, 3]

mySum = 4

xs.append(-mySum)


class Node:
    def __init__(self, i, s, left, right, truth):
        self.i = i
        self.s = s
        self.left = left
        self.right = right
        self.truth = truth

    def __repr__(self):
        return str((self.i, self.s, self.left, self.right, self.truth))


# Int -> Int -> Node
def q(i, s):
    if i == 0:
        return Node(i, s, None, None, xs[i] == s)
    else:
        left = q(i - 1, s)
        right = q(i - 1, s - xs[i])
        return Node(i, s, left, right, xs[i] == s)


pprint(q(len(xs) - 1, 0))
