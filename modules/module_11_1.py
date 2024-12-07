# Домашнее задание по теме "Обзор сторонних библиотек Python"

# from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# numpy
# print(np.__version__)
# pprint(dir(np))
np.random.seed(0)
print(a := np.random.rand(10))
print(b := np.random.rand(10))
print(c := a + b)
print(d := a * b)

A = np.array([[1, 2], [3, 4]])
print(A)
B = np.array([[1, 3], [2, 4]])
C = np.multiply(A, B)
print(C)
D = np.reshape(A, shape=(1, 4), order='C')
print(D)
E = np.reshape(A, shape=(1, 4), order='F')
print(E)
F = np.reshape(A, shape=(1, 4), order='A')
print(F)


# matplotlib
x = [1, 2, 3, 4]
y = [1, 4, 1, 2]
z = plt.plot(x, y)
plt.show(block=False)
plt.pause(1)

np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

plt.pause(1)

mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# the histogram of the data
n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax.grid(True)

plt.pause(1)

X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

fig, axs = plt.subplots(2, 2, layout='constrained')
pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0, 0])
axs[0, 0].set_title('pcolormesh()')

co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
fig.colorbar(co, ax=axs[0, 1])
axs[0, 1].set_title('contourf()')

pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma', norm=LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=axs[1, 0], extend='both')
axs[1, 0].set_title('imshow() with LogNorm()')

plt.pause(1)

fig, axd = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained')
axd['upleft'].set_title('upleft')
axd['lowleft'].set_title('lowleft')
axd['right'].set_title('right')

plt.pause(3)

# input("hit[enter] to end.")
plt.close("all")

