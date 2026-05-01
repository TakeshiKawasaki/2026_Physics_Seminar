import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
%config InlineBackend.figure_format = 'retina'

import numpy as np

# Texフォント（必要ならON）
# plt.rcParams["text.usetex"] = True 

# ---- データ生成 ----
dt = 0.01
tmax = 4.*np.pi
nstep = int(tmax / dt)

x = np.zeros(nstep + 1)
v = np.zeros(nstep + 1)
t = np.zeros(nstep + 1)

# 初期条件
x[0] = 1.0
v[0] = 0.0

# ---- 数値計算（symplectic Euler）----
for i in range(nstep):
    v[i+1] = v[i] - x[i] * dt
    x[i+1] = x[i] + v[i+1] * dt
    t[i+1] = t[i] + dt

# ---- プロット ----
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)

ax.set_xlim(0, t[-1])
ax.set_ylim(-1.2, 1.2)

plt.plot(t, x, "o", linewidth=2, color="b",
         label=r"${\rm d}^2\tilde{x}/{\rm d}\tilde{t}^2 = -\tilde{x}$ (numerical)")

# ---- 理論解 ----
x_exact = np.cos(t)
plt.plot(t, x_exact, "-", linewidth=3, color="r",
         label=r"$\tilde{x}=\cos(\tilde{t})$")

# ---- 図の設定 ----
plt.tick_params(which='major', width=1, length=10)
plt.tick_params(which='minor', width=1, length=5)
plt.minorticks_on()

ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)

# ---- 軸のラベル ----
plt.xlabel(r"$\tilde{t}~~(=t/t_0)$", color='k', size=25)
plt.ylabel(r"$\tilde{x}(\tilde{t})~~(=x/a)$", color='k', size=25)

plt.xticks(color='k', size=25)
plt.yticks(color='k', size=25)

plt.legend(ncol=1, loc=1, borderaxespad=0, fontsize=25, frameon=True)
plt.subplots_adjust(wspace=0.0, hspace=0.25)

plt.tight_layout()

# ---- 保存 ----
plt.savefig('x_t.png')
plt.savefig('x_t.pdf')
