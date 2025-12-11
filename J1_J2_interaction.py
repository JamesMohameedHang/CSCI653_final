import numpy as np
import math
import tenpy
from tenpy.networks.mps import MPS
import time
from tenpy.models.spins_nnn import SpinChainNNN2
from tenpy.algorithms import dmrg

deltas = np.arange(0.95,1.5,0.05)
#deltas1=np.arange(-1.00,-0.60,0.05)
#deltas2=np.arange(0.65,1.05,0.05)
#deltas=np.arange(-1.0,1.05,0.05)
delta = 0.30
Ls=np.arange(50,530,20)
L = 150
J = 1.0
Jz = 0.0
f=open("J1_J2_interaction_strong_Jz_0_L_"+str(L)+"_del_varying.txt","w")
for delta in deltas:
	N=L*2
	J2 = J+delta
	model_params = {
            'L': N,
            'Jx': J,
            'Jy':J,
            'Jxp':J2,
            'Jyp':J2,
            'Jz':Jz,
            'Jzp':Jz*J2,
            'hz':0,  # just free fermions, but you can generalize...
            'bc_MPS':'finite'
	   }
	M = SpinChainNNN2(model_params)
	product_state = ['up', 'down']*(L)
	psi = MPS.from_product_state(M.lat.mps_sites(), product_state, bc=M.lat.bc_MPS)
	dmrg_params = {
            'mixer': None,
            #  'mixer_params': {'amplitude': 1.e-3, 'decay': 5., 'disable_after': 50},
            'trunc_params': {
                'chi_max': 300,
                #Dimension of the system
                'svd_min': 1.e-10
            },
            'max_E_err': 1.e-9,
            'combine': True
        }
    #chi_list = np.arange(7, 31, 2)
	s_list = []
	E_list=[]
	eng = dmrg.TwoSiteDMRGEngine(psi, M, dmrg_params)
 # necessary if you for example have a fixed numer of sweeps, if you don't set this you option your simulation stops after initial number of sweeps!
        ##   DMRG Calculation    ##
	print("Start IDMRG CALCULATION")
	E,psi=eng.run()
	eng.options['mixer'] = None
	psi.canonical_form()

        ##   Calculating bond entropy and correlation length  ##
	s=psi.entanglement_entropy()[L-1]
	s2=psi.entanglement_entropy()[L]
	corr_func=psi.correlation_function("Sz","Sz")[0][L]
         # the bond 0 is between MPS unit cells and hence sensible even for 2D lattices.
        #xi_list.append(psi.correlation_length())
        #print(result)
	expec=psi.expectation_value("Sz")
	#expec2=psi.expectation_value("Sz")
	print(
          #np.mean(psi.expectation_value(M.H_bond)),
        L,
        s,
        s2,
        E,
        corr_func,
        delta,
          #xi_list[-1],
        flush=True)
	tenpy.tools.optimization.optimize(3)  # quite some speedup for small chi
	#f.write(str(int(L))+"       "+str(expec)+"\n")
	print("SETTING NEW BOND DIMENSION")
	# f.write(str(int(L))+"       "+str(expec)+str(delta)+"\n")
	f.write(str(int(L))+"       "+str(s)+"      "+str(s2)+"      "+str(corr_func)+"     "+str(E)+"       "+str(delta)+"\n")
f.close()
