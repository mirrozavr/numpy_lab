import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.genfromtxt('func.dat')

A = 0.5 * (np.eye(len(data)) - np.eye(len(data), k=-1))
A[0, len(data) - 1] = -0.5

GIF_FPS = 15
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i):
    global data
    data1 = data - A @ data
    data = data1

    ax.clear()
    ax.set_ylim([0, 10])
    ax.set_xlim([0, 50])

    ax.grid()
    ax.set_title('Frame ' + str(i + 1))
    ax.plot(data1, color=(170 / 255, i / 255, i / 255), linewidth=6)

result = animation.FuncAnimation(fig, animate, frames=255)
result.save('animation.gif', fps=GIF_FPS)
print()