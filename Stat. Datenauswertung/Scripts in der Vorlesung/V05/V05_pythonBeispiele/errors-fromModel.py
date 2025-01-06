import numpy as np
import matplotlib.pyplot as plt
from PhyPraKit import wmean

#plt.xkcd() # set xkcd style (looks like hand-drawn)
plt.xkcd(scale=.5, randomness=2.5) # set xkcd style (looks like hand-drawn)

# plot the results (with matplotlib)
fig=plt.figure(figsize=(7.5, 7.5))

nd = 10
rerr = 0.2
dat = 0.5 + rerr*(np.random.rand(nd)-0.5) # data around 0.5
ave = np.mean(dat)
emp_err = rerr*dat
mod_err = rerr*ave*np.ones(nd)

biased_ave = wmean(dat, emp_err, pr=False)[0]

ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

xb=np.linspace(1.,10., 10)
ax1.errorbar(xb, dat, emp_err,fmt='x') 
ax1.axhline(ave, color='darkgreen', linestyle='--', lw=2)
ax1.axhline(biased_ave, color='red', linestyle='-.', lw=2)
#ax1.set_xlabel('# of measurement')
ax1.set_ylim(0.)
ax1.set_xlim(0.5,10.5)
ax1.set_ylabel('m')
ax1.text(0.6, 0.9,'errors from observation', 
          color='darkred', transform=ax1.transAxes)
ax2.errorbar(xb, dat, mod_err,fmt='x') 
ax2.axhline(ave, color='darkgreen', linestyle='--', lw=2)
ax2.set_xlim(0.5,10.5)
ax2.set_ylim(0.)
ax2.set_xlabel('# of measurement')
ax2.text(0.7, 0.9, 'errors from model', 
          color='darkred', transform=ax2.transAxes)
ax2.set_ylabel('m')

plt.show()
