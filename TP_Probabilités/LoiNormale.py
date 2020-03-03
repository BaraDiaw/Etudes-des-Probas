#@author: ABD
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm
norm.rvs()
x = np.linspace(-4,4,1000) 
plt.plot(x, norm.pdf(x),label = "", lw = "4", ls = "-", c = "orange")
plt.title("Loi normale", color = "orange")
plt.legend()
plt.xlabel("abcisses", color = "blue")
plt.ylabel("ordonnées", color = "blue")
