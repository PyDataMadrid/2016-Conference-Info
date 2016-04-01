import numpy as np
import pylab as plt
from matplotlib import cm
from itertools import product

def julia_iteration(z, c, maxiter=256):
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return n

def julia_set(w, h, c, maxiter=256):
    m = np.empty((h, w), dtype=np.uint8)
    for j, i in product(range(h), range(w)):
        z = (i-w/2)/(h/2) + (j-h/2)/(h/2)*1j
        m[j,i] = julia_iteration(z, c, maxiter)

    return m

def plot_julia(w, h, cre, cim, cmap):
    m = julia_set(w, h, cre+cim*1j)
    colors = getattr(cm, cmap)
    plt.imshow(m, cmap=colors)
    plt.gca().axis('off')
    plt.show()
    

if __name__ == '__main__':
    # -0.8 + 0.156*1j
    #  0.3 + 0.230*1j
    plot_julia(800, 600, -0.8, 0.156, 'viridis')

    
