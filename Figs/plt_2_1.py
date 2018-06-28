import numpy as np
import matplotlib.pyplot as plt

time = 500
space = time // 5
ka = 1e+4
ini = [1e-6, 1e-6, 0, 0]

def differ(ini, ka, time, space, ret='delta'):
    
    A = np.linspace(0, 0, time+space+1)
    B = np.linspace(0, 0, time+space+1)
    C = np.linspace(0, 0, time+space+1)
    D = np.linspace(0, 0, time+space+1)
    for i in range(space+1):
        A[i], B[i] = ini[:2]
    delta = np.linspace(0, 0, time+space+1)
    noise = np.random.randn(1, time+space+1) * np.sqrt(ini[0]*ini[1])/150

    for i in range(time):
        delta[space+i+1] = ka * A[space+i] * B[space+i]
        A[space+i+1] = A[space+i] - delta[space+i+1]
        B[space+i+1] = B[space+i] - delta[space+i+1]
        C[space+i+1] = C[space+i] + delta[space+i+1]
        D[space+i+1] = D[space+i] + delta[space+i+1]
    if 'n' not in ret:
        noise = np.linspace(0, 0, time+space+1)
    if 'A' in ret:
        return (A + noise).reshape(-1)
    elif 'B' in ret:
        return (B + noise).reshape(-1)
    elif 'C' in ret:
        return (C + noise).reshape(-1)
    elif 'D' in ret:
        return (D + noise).reshape(-1)
    else:
        return delta

y = differ(ini, ka, time, space, ret='Cn')
x = np.linspace(0, time+space, time+space+1)

plt.figure(figsize=(15,4.5))
plt.subplot(131)
plt.plot(x, y*1e6, '.', label='experimental-[C]', color='C0', linewidth=2)
plt.xlabel('Time / steps')
plt.ylabel('Concentration / uM')
plt.legend()

y = differ(ini, ka, time, space, ret='C')
plt.subplot(132)
plt.plot(x, y*1e6, label='simulative-[C]', color='C0', linewidth=1.5)
plt.xlabel('Time / steps')
plt.ylabel('Concentration / uM')

plt.legend()

y = differ(ini, ka, time, space, ret='')
plt.subplot(133)
plt.plot(x, y*1e6, '.', label='simulative-rate', color='C0', linewidth=2)
plt.xlabel('Time / steps')
plt.ylabel('Rate / uM $\cdot$ Step$^{-1}$')
plt.legend()
#plt.show()
plt.tight_layout()
plt.savefig('fig_2_1.png', format='png', dpi=150)
