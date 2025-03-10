import random 
import numpy as np 
import matplotlib.pyplot as plt 

a = 0
b = np.pi 
N = 1000

def f(x): 
	return np.sin(x) 

plt_vals = [] 

 
for i in range(N): 
	
	ar = np.zeros(N) 


	for i in range (len(ar)): 
		ar[i] = random.uniform(a,b) 

 
	integral = 0.0

	for i in ar: 
		integral += f(i) 

	ans = (b-a)/float(N)*integral 

	plt_vals.append(ans) 

plt.title("Distributions of areas calculated") 

plt.hist (plt_vals, bins=30, ec="black") 


plt.xlabel("Areas") 
plt.show()
