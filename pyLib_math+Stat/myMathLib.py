import math

'''
   def __init__(self):
        self.name = name
    '''


class myMathLib:
    def __init__(self):
        self.LinearAlg = self.LinearAlg()

    class LinearAlg():
        def norm(self, u):
            return self.magnitude(u)

        def magnitude(self, u):
            return math.sqrt(sum([pow(x, 2) for x in u]))

        def normalize(self, u):
            mag = self.magnitude(u)
            if mag == 0 or mag == 1:
                return u
            return [i / mag for i in u]

        def isPerp(self, a, b):
            return self.dotProduct(a, b) == 0

        def identity(n):
            return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

        def dotProduct(self, v, u):
            if (len(v) == len(u)):
                return sum(i * j for i, j in zip(v, u))
            else:
                raise ValueError("Invalid vectors - must be of same length.")

        # TODO fix print(ml.LinearAlg.norm(ml.LinearAlg.crossProductWithAngle([3, -2, -2], [-1, 0, 5], 90)))
        def crossProductWithAngle(self, v, u, sin):
            if (len(v) == len(u) == 3):
                return self.magnitude(v) * self.magnitude(u) * math.sin(sin)
            else:
                raise ValueError("Invalid vectors - must be of same length.")

        def crossProduct(self, u, v):
            if (len(v) == len(u) == 3):
                return [
                    (u[1] * v[2] - u[2] * v[1]),
                    (u[2] * v[0] - u[0] * v[2]),
                    (u[0] * v[1] - u[1] * (v[0]))
                ]
            else:
                raise ValueError("Invalid vectors - must be of same length.")
