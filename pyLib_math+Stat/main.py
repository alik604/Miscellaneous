from myMathLib import myMathLib
from myStatLib import myStatLib

''''
tutorial https://www.pythoncentral.io/how-to-create-a-python-package/
'''

ml = myMathLib()
sl = myStatLib()

print(sl.combinatorics.PermutationsWithoutRepetition(16, 3) == 3360)
print(sl.combinatorics.CombinationsWithoutRepetition(16, 3) == 560)
print(sl.combinatorics.PermutationsWithRepetition(5, 3) == 35)
print(ml.LinearAlg.dotProduct([4, 1], [2, 10]) == 18)
print(ml.LinearAlg.norm(ml.LinearAlg.crossProduct([3, -2, -2], [-1, 0, 5])) == 16.522711641858304)

print(ml.LinearAlg.crossProduct([3, -2, -2], [-1, 0, 5])) == 16.522711641858304
