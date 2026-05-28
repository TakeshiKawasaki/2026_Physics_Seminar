import numpy as np
import sys

omega0=[0.1,1.0,1.5]


def damp_osci(omega0):
    v=0.
    x=0.
    t=0.
    i=0
    out=0.
    zeta =0.01
    dt=0.01
    f = open("./damp_osci_omega{:.4f}.dat".format(omega0), 'w')
    while i < (int)(500./dt): 
        v += -zeta*v*dt-x*dt + np.sin(omega0*i*dt)*dt
        x+=v*dt
        i+=1
        if(i*dt >=out):
            print("{:.4f} {:.20f} {:.20f}".format(i*dt,v,x))
            f.write("{:.4f} {:.20f} {:.20f}\n".format(i*dt,v,x))
            out+=0.5
    f.close()
    

for i in range(0,3):
    print("omega0={:.4f}".format(omega0[i]))
    damp_osci(omega0[i]) 
