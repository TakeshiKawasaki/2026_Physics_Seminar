import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline
%config InlineBackend.figure_format = 'retina'

import numpy as np

# Texフォント
plt.rcParams["text.usetex"] = True 

# ---- データ生成 ----
dt = 0.01
nstep = 500

v = np.zeros(nstep + 1)
t = np.zeros(nstep + 1)

v[0] = 1.0

for i in range(nstep):
    v[i+1] = v[i] - v[i] * dt
    t[i+1] = t[i] + dt

# ---- プロット ----
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)

ax.set_xlim(0, t[-1])
ax.set_ylim(0, 1.0)

plt.plot(t, v, "o", linewidth=2, color="b", label=r"${\rm d}\tilde{v}/{\rm d}\tilde{t} = -\tilde{v}$")

# ---- 理論解 ----
v_exact = np.exp(-t)
plt.plot(t, v_exact, "-", linewidth=3, color="r", label=r"$\tilde{v}=e^{-\tilde{t}}$")

# ---- 図の設定 ----
plt.tick_params(which='major', width=1, length=10)
plt.tick_params(which='minor', width=1, length=5)
plt.minorticks_on()
ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)


# ---- 軸のラベル ----
plt.xlabel(r"$\tilde{t}~~(=t/t_0)$", color='k', size=30)
plt.ylabel(r"$\tilde{v}(\tilde{t})~~(=v/v_0)$", color='k', size=30)

plt.xticks(color='k', size=25)
plt.yticks(color='k', size=25)

plt.legend(ncol=1, loc=1, borderaxespad=0, fontsize=25, frameon=True)
plt.subplots_adjust(wspace=0.0, hspace=0.25)


plt.tight_layout()
# ---- 保存（同一ディレクトリ） ----
plt.savefig('v_t.png')
plt.savefig('v_t.pdf')
