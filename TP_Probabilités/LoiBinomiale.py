#@author: ABD
import numpy as np 
import scipy.stats as sps 
import matplotlib.pyplot as plt 
n= 20
p= 0.3
N = int(1e4) 
B = np.random.binomial(n, p, N) 
f = sps.binom.pmf(np.arange(n+1), n, p) 
plt.hist(B, bins = n+1, normed = 1, range = (5,n+.5),\ color = "white", label = "loi empirique")
plt.stem(np.arange(n+1),f,"r", label = "loi theorique") 
plt.legend()