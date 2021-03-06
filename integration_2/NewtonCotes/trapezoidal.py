# Trapezoidal rule
# Input  : Function f, limits a to b , and n partitions
# Output : Integral

import numpy as np

def trapeze(f,a,b,n):

    h = (b-a)*1.0/n
    x = np.linspace(a,b,n+1)
    C = np.ones([n+1,1])
    C[1:n] = 2
    z = 0.5*h*np.dot(f(x),C)
    return z
    
def func(x):

    z = x**2
    return z
    
print(trapeze(func,1,2,100)) 
# Error = -(f^(2)*(b-a)^3)/(12*n^2)
