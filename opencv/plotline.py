'''
Criar uma linha vertical no histograma
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
y = np.full((1000,),25)
ax.plot(y,x);
