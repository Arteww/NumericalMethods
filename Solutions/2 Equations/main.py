from equations import *


def f(x): return x * x - 34


a, b = 0, 8

xDichotomy = dichotomy(f, a, b)
xChords = chords(f, a, b)
xBruteForce = brute_force(f, a, b)
xNewton = newton(f, lambda x: x * 2, x=3)

print("[x]\t\t[method]\n"
      f"{xDichotomy} \tBisection\n"
      f"{xChords} \tChord\n"
      f"{xBruteForce} \tBrute Force\n"
      f"{xNewton} \tNewton's")
