import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import numpy as np

plt.rcParams["text.usetex"] =True

plt.rcParams['font.family'] = 'Arial' #使用するフォント名
plt.rcParams["font.size"] = 40

fig = plt.figure(figsize=(45,20))

x0_list = [-0.1, 0.1, 1.0]
f0=0.5
ax = fig.add_subplot(1,2,1)
t, v1,x1  = np.loadtxt("./duffing_x0_{:.4f}_f0_{:.4f}.dat".format(x0_list[0],f0), comments='#', unpack=True)
t, v2,x2  = np.loadtxt("./duffing_x0_{:.4f}_f0_{:.4f}.dat".format(x0_list[1],f0), comments='#', unpack=True)
t, v3,x3  = np.loadtxt("./duffing_x0_{:.4f}_f0_{:.4f}.dat".format(x0_list[2],f0), comments='#', unpack=True)

plt.plot(t, x1, "-",markersize=10,color="b",label=r"$x_0={:.4f}$".format(x0_list[0]))
plt.plot(t, x2, "-",markersize=10,color="g",label=r"$x_0={:.4f}$".format(x0_list[1]))
plt.plot(t, x3, "-",markersize=10,color="r",label=r"$x_0={:.4f}$".format(x0_list[2]))

#########
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
ax.spines['top'].set_linewidth(4)
ax.spines['bottom'].set_linewidth(4)
ax.spines['left'].set_linewidth(4)
ax.spines['right'].set_linewidth(4)
plt.ylabel(r"$x(t)/a$",color='k', size=50)
plt.xlabel(r"$t/t_s$",color='k', size=50)

plt.legend(ncol=1, loc=4, borderaxespad=0, fontsize=35,frameon=True)


ax = fig.add_subplot(1,2,2)
t, v1,x1  = np.loadtxt("./duffing_x0_{:.4f}_f0_{:.4f}.dat".format(x0_list[0],f0), comments='#', unpack=True)
t, v2,x2  = np.loadtxt("./duffing_x0_{:.4f}_f0_{:.4f}.dat".format(x0_list[1],f0), comments='#', unpack=True)
t, v3,x3  = np.loadtxt("./duffing_x0_{:.4f}_f0_{:.4f}.dat".format(x0_list[2],f0), comments='#', unpack=True)

plt.plot(x1,v1, "-",markersize=10,color="b",label=r"$x_0={:.4f}$".format(x0_list[0]))
plt.plot(x2,v2, "-",markersize=10,color="g",label=r"$x_0={:.4f}$".format(x0_list[1]))
plt.plot(x3,v3, "-",markersize=10,color="r",label=r"$x_0={:.4f}$".format(x0_list[2]))

#########
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
ax.spines['top'].set_linewidth(4)
ax.spines['bottom'].set_linewidth(4)
ax.spines['left'].set_linewidth(4)
ax.spines['right'].set_linewidth(4)
plt.xlabel(r"$x(t)/a$",color='k', size=50)
plt.ylabel(r"$\dot{x}(t)t_0/a$",color='k', size=50)
plt.xlim(-2.0, 2.0)
plt.ylim(-2.0, 2.0)


plt.legend(ncol=1, loc=4, borderaxespad=0, fontsize=35,frameon=True)
#################################
    #図のマージン設定
plt.subplots_adjust(wspace=0.3, hspace=0.35)


#################################
    #図のマージン設定
plt.subplots_adjust(wspace=0.3, hspace=0.35)

plt.savefig('./duffing_f0_{:.4f}.png'.format(f0))
plt.savefig('./duffing_f0_{:.4f}.pdf'.format(f0))
