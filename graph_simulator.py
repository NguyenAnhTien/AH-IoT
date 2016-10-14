import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 100))


def animate(a0, a1): 
    graph_data = open('sample.csv', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))

    a0.set_data(range(100), xs)
    a1.set_data(range(100), ys)
    #ax.clear()
    #ax.plot(a0, a1)


a0, = ax.plot([], [])
a1, = ax.plot([], [])
animate(a0, a1)

#anim = animation.FuncAnimation(fig, animate, fargs=(a0, a1), interval=50)

plt.show()


