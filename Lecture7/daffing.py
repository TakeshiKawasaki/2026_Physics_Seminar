import numpy as np
import os

f0 = 0.3
x0_list = [-0.1, 0.1, 1.0]

def duffing(x_ini):
    v = 0.0
    x = x_ini
    i = 0
    omega0 = 1.0
    out = 0.0
    zeta = 0.25
    dt = 0.001

    filename = "./duffing_x0_{:.4f}_f0_{:.4f}.dat".format(x_ini,f0)

    with open(filename, "w") as f:
        while i < int(200.0/dt):
            t = i*dt
            v += -zeta*v*dt + (x - x**3)*dt + f0*np.cos(omega0*t)*dt
            x += v*dt
            i += 1

            if i*dt >= out:
                f.write("{:.4f} {:.20f} {:.20f}\n".format(i*dt, v, x))
                out += 0.5

    print(filename, "created:", os.path.exists(filename))

for xi in x0_list:
    print("x0_list = {:.4f}".format(xi))
    duffing(xi)
