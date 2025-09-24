import numpy as np

def cube(n):
    return n**3
        
def volume_sphere(r):
    return 4 / 3 * np.pi * cube(r)

r = float(input("Entrez la valeur du rayon : "))
print("Le volume de cette sphere vaut", volume_sphere(r))
