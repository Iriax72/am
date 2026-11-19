import time
import numpy as np
import matplotlib.pyplot as plt

N = 50

def fac_rec(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    return n * fac_rec(n-1)

def fac_it(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

def mesure_time(N, f, args):
    times = []
    for i in range(N):
        debut = time.perf_counter()
        f(*args)
        times.append(time.perf_counter() - debut)
    return np.mean(times)

X = np.arange(51)
Yrec = []
Yit = []
for x in X:
    Yrec.append(mesure_time(N, fac_rec, [x]))
    Yit.append(mesure_time(N, fac_it, [x]))

plt.title(f"Temps d'execution de l'algorithme récusrsif vs itératif sur {N} valeurs")
plt.scatter(X, Yrec, label="Méthode récursive")
plt.scatter(X, Yit, label="Méthode itérative")
plt.legend()
plt.show()