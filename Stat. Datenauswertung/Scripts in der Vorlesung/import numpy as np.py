import numpy as np
import matplotlib.pyplot as plt
import sys
npoints=10000

inx=[]
iny=[]
outx=[]
outy=[]
for i in range(npoints):
    rvec=np.random.rand(2)
    if (np.sum(rvec**2)<=1.):
        inx.append(rvec[0])
        iny.append(rvec[1])
    else:
        outx.append(rvec[0])
        outy.append(rvec[1])
plt.scatter(inx, iny, s=1, color='g')
plt.scatter(outx, outy, s=1, color='r')
pi=4.*float(len(inx)) / \
 float((len(inx)+len(outx)))

plt.show()
