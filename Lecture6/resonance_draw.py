import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import numpy as np
plt.rcParams["text.usetex"] =True

plt.rcParams['font.family'] = 'Arial' #使用するフォント名
plt.rcParams["font.size"] = 40

fig = plt.figure(figsize=(20,10))

omega=[0.1,1.0,1.5]
ax = fig.add_subplot(1,1,1)
t, v0,x0  = np.loadtxt("./damp_osci_omega{:.4f}.dat".format(omega[0]), comments='#', unpack=True)
t, v0,x1  = np.loadtxt("./damp_osci_omega{:.4f}.dat".format(omega[1]), comments='#', unpack=True)
t, v0,x2  = np.loadtxt("./damp_osci_omega{:.4f}.dat".format(omega[2]), comments='#', unpack=True)

plt.plot(t, x0, "o-",markersize=10,color="b",label=r"$\omega_0={:.4f}$".format(omega[0]))
plt.plot(t, x1, "D-",markersize=10,color="g",label=r"$\omega_0={:.4f}$".format(omega[1]))
plt.plot(t, x2, "x-",markersize=10,color="r",label=r"$\omega_0={:.4f}$".format(omega[2]))
#########
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
ax.spines['top'].set_linewidth(4)
ax.spines['bottom'].set_linewidth(4)
ax.spines['left'].set_linewidth(4)
ax.spines['right'].set_linewidth(4)
plt.ylabel(r"$x(t)/a$",color='k', size=50)
plt.xlabel(r"$t/t_s$",color='k', size=50)

plt.legend(ncol=1, loc=2, borderaxespad=0, fontsize=35,frameon=False)
#################################
    #図のマージン設定
plt.subplots_adjust(wspace=0.3, hspace=0.35)

plt.savefig('./damp_resonance.png')
plt.savefig('./damp_resonance.pdf')
