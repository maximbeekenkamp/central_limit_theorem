import numpy as np
import matplotlib.pyplot as plt
a=20
b=100

exp = [[0 for y in range(0,a) ] for x in range(0,b)]
N = [[0 for y in range(0,1) ] for x in range(0,b)]

for x in range(0,b):
	exp[x]= np.random.random_integers(0, 1,a )
	N[x] = sum(exp[x])
 
for x in range(0,b):
	print(exp[x])
num_bins = 21
plt.hist(N,num_bins,(-0.5,num_bins-0.5))
plt.show()

print("I am Maxim")
#print(N)

