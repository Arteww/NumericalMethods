from equations import *
import numpy as np
import matplotlib.pyplot as plt


def f(x): return x * x - 34


a, b = 0, 8

xDichotomy = dichotomy(f, a, b)
xChords = chords(f, a, b)
xBruteForce = brute_force(f, a, b)
xNewton = newton(f, lambda x: x * 2, x=3)

print("[x]\t[method]\n"
      f"{round(xDichotomy, 1)} \tBisection\n"
      f"{round(xChords, 1)} \tChords\n"
      f"{round(xBruteForce, 1)} \tBruteForce\n"
      f"{round(xNewton, 1)} \tNewton's")

_, ax = plt.subplots()
ax.set_title('Equations')
plt.axhline(y=0, lw=2, color='k')
plt.axvline(x=0, lw=2, color='k')

x = np.linspace(a, b, 100)
plt.plot(x, f(x))
plt.plot(xDichotomy, f(xDichotomy), 'yo', label="Bisection")
plt.plot(xChords, f(xChords), 'bo', label="Chords")
plt.plot(xBruteForce, f(xBruteForce), 'go', label="BruteForce")
plt.plot(xNewton, f(xNewton), 'ro', label="Newton's")

plt.legend()
plt.grid()
plt.show()
