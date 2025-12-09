from mpl_toolkits import mplot3d
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dels = np.arange(-1.0,1.05,0.1)
Jzs = [-1.0,-0.8,-0.7,-0.6,-0.55]
for delta in dels[5:]:
	Jzs.append(-0.5)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(dels,Jzs,color="red",linewidth=3.0)
plt.vlines(x=-0.5,ymin=-0.5,ymax=1.0,linewidth=3.0,linestyle='--')
plt.hlines(y=1, xmin=-1.0,xmax=1.0,color="green")
plt.gcf().set_size_inches(14, 12)
plt.ylim(-1.1,1.5)
plt.xticks()
plt.yticks()
plt.tick_params(axis='x', labelsize=40,length=10,width=2)  # X-axis values
plt.tick_params(axis='y', labelsize=40,length=10,width=2)  # Y-axis values
plt.savefig("images/J1J2_phase.png")
plt.show()
