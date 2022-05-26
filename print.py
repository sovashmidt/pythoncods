import numpy as np
x = np.arande(10)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)

y = np.zeros(10)
np.power(2, x, out= y[::2])
print(y)