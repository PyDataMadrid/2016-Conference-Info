import numpy as np


cpdef long julia_iteration(double complex z, double complex c, long maxiter=256):
    cdef long n
    for n in range(maxiter):
        if abs(z) > 2.0:
            return n
        z = z**2 + c
        
    return n


def julia_set(long w, long h, double complex c, long maxiter=256):
    cdef long i, j
    m = np.empty((h, w), dtype=np.long)
    cdef long [:,:] mview = m
    for j in range(h):
        for i in range(w):
            z = (i - <double>w/2.0)/(<double>h/2.0) + \
                (j - <double>h/2.0)/(<double>h/2.0)*1j
            mview[j,i] = julia_iteration(z, c, maxiter)

    return m
