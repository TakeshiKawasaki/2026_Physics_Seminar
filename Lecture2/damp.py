import numpy as np

dt = 0.01
nstep = 500

v = np.zeros(nstep + 1)
t = np.zeros(nstep + 1)
v[0] = 1.0

for i in range(nstep):
    v[i+1] = v[i] - v[i] * dt
    t[i+1] = t[i] + dt

for i in range(nstep):
    print("{:.3g} {:.10g}".format(t[i], v[i]))
