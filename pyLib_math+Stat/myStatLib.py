import math


class myStatLib:
    def __init__(self):
        self.combinatorics = self.combinatorics()

    class combinatorics():
        def PermutationsWithRepetition(self, n, r):
            return n ** r

        def PermutationsWithoutRepetition(self, n, r):
            return int(math.factorial(n) / (math.factorial(n - r)))

        def CombinationsWithoutRepetition(self, n, r):
            return int(self.PermutationsWithoutRepetition(n, r) / math.factorial(r))

        def PermutationsWithRepetition(self, n, r):
            return self.CombinationsWithoutRepetition(n - 1 + r, r)
