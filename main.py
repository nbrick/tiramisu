xs = [1, 3, 5, 3]

mySum = 6

xs.append(-mySum)


class Node:
    def __init__(self, i, s, left, right, truth):
        self.i = i
        self.s = s
        self.left = left
        self.right = right
        self.truth = truth

    def __repr__(self, depth = 1):
        return_string = [str([self.i, self.s, self.truth])]
        if self.truth:
            return_string.append(" <-------")
        for child in filter(lambda x: x is not None, [self.left, self.right]):
            if child.truth:
                return_string.extend(["\n", "   " * (depth+1), child.__repr__(depth+1)])
            else:
                return_string.extend(["\n", "   " * (depth+1), child.__repr__(depth+1)])
        return "".join(return_string)

# Int -> Int -> Node
def q(i, s):
    if i == 0:
        return Node(i, s, None, None, xs[i] == s)
    else:
        left = q(i - 1, s)
        right = q(i - 1, s - xs[i])
        return Node(i, s, left, right, xs[i] == s)


print(q(len(xs) - 1, 0))
