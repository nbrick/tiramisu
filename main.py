xs = [1, 3, 5, 3]

mySum = 6

xs.append(-mySum)


class Node:
    def __init__(self, i, s, truth, parent):
        self.i = i
        self.s = s
        self.parent = None
        self.left = None
        self.right = None
        self.truth = truth

    def set_children(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self, depth=1):
        return_string = [str([self.i, self.s, self.truth])]
        if self.truth:
            return_string.append(" <-------")
        for child in filter(lambda x: x is not None, [self.left, self.right]):
            if child.truth:
                return_string.extend(
                    ["\n", "   " * (depth+1), child.__repr__(depth+1)])
            else:
                return_string.extend(
                    ["\n", "   " * (depth+1), child.__repr__(depth+1)])
        return "".join(return_string)


# Int -> Int -> Maybe Node -> Node
def q(i, s, parent):
    if i == 0:
        return Node(i, s, xs[i] == s, parent)
    else:
        n = Node(i, s, xs[i] == s, parent)
        left = q(i - 1, s, n)
        right = q(i - 1, s - xs[i], n)
        n.set_children(left, right)
        return n


print(q(len(xs) - 1, 0, None))
