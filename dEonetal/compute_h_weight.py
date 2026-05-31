import numpy as np

n = 35
h, w = np.polynomial.legendre.leggauss(n)

filename_h = "./value/h.txt"
filename_w = "./value/w.txt"

with open(filename_h, 'w') as f_h:
    for elt in h:
        f_h.write(str(elt) + ", ")

with open(filename_w, 'w') as f_w:
    for elt in w:
        f_w.write(str(elt) + ", ")
