import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a=20
b=1000000

exp = [[0 for y in range(0,a) ] for x in range(0,b)]
N = [[0 for y in range(0,1) ] for x in range(0,b)]

for x in range(0,b):
	exp[x]= np.random.random_integers(0, 1,a )
	N[x] = sum(exp[x])

#for x in range(0,b):
	#print(exp[x])
num_bins = 22
count, num_bins, ignored = plt.hist(N,num_bins,(-0.5,num_bins-0.5),normed=True)

m, s = stats.norm.fit(N) # get mean and standard deviation

#xmin, xmax = min(N), max(N)
#lnspc = np.linspace(xmin, xmax, 100)
#pdf_g = stats.norm.pdf(lnspc, m, s)
#plt.plot(lnspc, pdf_g, label="Norm") # plot it

plt.plot(num_bins, 1/(s * np.sqrt(2 * np.pi)) * np.exp( - (num_bins - m)**2 / (2 * s**2) ),linewidth=2, color='r')

print("m = ",m)
print("s = ",s)


#print(N)
plt.show()

#print("I am Maxim")
