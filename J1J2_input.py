from mpl_toolkits import mplot3d
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
f1=open("J1_J2_interaction_strong_Jz_varying_L_50_del_0.0.txt","r")
length=[100,150,200,250,300,350,400]
s_even,s_odd = [],[]
dels = []
for line in f1:
    s_even.append(float(line.split()[1]))
    s_odd.append(float(line.split()[2]))
    dels.append(float(line.split()[5]))
plt.scatter(dels,s_even,color="orange",s=150)
plt.xticks()
plt.yticks()
plt.tick_params(axis='x', labelsize=40,length=10,width=2)  # X-axis values
plt.tick_params(axis='y', labelsize=40,length=10,width=2)  # Y-axis values
# plt.xlabel("δ")
# plt.ylabel("S")
# plt.legend(loc='lower right',fontsize=32)
plt.gcf().set_size_inches(14, 12)
plt.savefig("images/J1J2_S_Jz_varying_del_0.0.png")
plt.show()
