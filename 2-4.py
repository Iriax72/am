import math
import time
import numpy as np
import matplotlib.pyplot as plt

N = 50

def isPremier(n):
    if n < 2:
        return False
    for i in range(2, math.floor(n/2) + 1):
        if n%i == 0:
            return False
    return True

def nbr_premiers_doubleboucle(n):
    ret = []
    for i in range(1, n+1):
        if isPremier(i):
            ret.append(i)
    return ret

def nbr_premiers_eratostene(n):
    possibles = [*range(2, n+1)]
    for possible in possibles:
        if isPremier(possible):
            multiple_max = math.floor(n/possible)
            for multiple in range(2, multiple_max+1):
                if multiple*possible in possibles:
                    possibles.remove(multiple*possible)
    return possibles

def mesure_time(N, f, args):
    times = []
    for i in range(N):
        debut = time.perf_counter()
        f(*args)
        times.append(time.perf_counter - debut)
    return np.mean(times)

X = np.arange(201)
Ydoubleboucle = []
Yeratostene = []
for x in X:
    Ydoubleboucle.append(mesure_time(N, nbr_premiers_doubleboucle, [x]))
    Yeratostene.append(mesure_time(N, nbr_premiers_eratostene, [x]))

plt.title("Temps d'execution de l'algorithme par double boucle vs d'Eratostène")
plt.scatter(X, Ydoubleboucle, label="Méthode par double boucle")
plt.scatter(X, Yeratostene, label="Méthode d'Eratostène")
plt.legend()
plt.show()