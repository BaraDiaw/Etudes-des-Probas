#@author: ABD
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

exp = np.linspace(0,8,100000)
plt.figure(figsize = (7,7))#taille de la figure
plt.plot(exp,expon.pdf(exp,scale = 1),label = "fonction de densité", lw = "4", ls = "-", c = "orange")
plt.title("Loi exponentielle", color = "blue")
plt.legend()
plt.xlabel("abcisses", color = "blue")
plt.ylabel("ordonnées", color = "blue")