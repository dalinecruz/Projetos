import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(3, -2, 200)
y = x ** 2 - 2 * x + 1
plt.plot(x, y)
plt.show()