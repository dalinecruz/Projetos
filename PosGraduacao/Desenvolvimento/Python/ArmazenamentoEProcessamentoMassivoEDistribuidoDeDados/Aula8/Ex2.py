'''
Created on 31 de mai. de 2022

@author: daline
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2 * np.pi, 100)
f = np.sin(x)
plt.plot(x,f)
plt.show()