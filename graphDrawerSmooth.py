
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('/data/projects/AH-IoT/data_case_2.csv', delimiter=';', unpack=True)

for index, item in enumerate(y):
    if (index < (len(y) - 2)) and (index > 2):
        y[index] = (y[index - 2] + y[index - 1] + y[index + 1] + y[index + 2] + y[index]) / 5.0

plt.plot(x,y, label='Light Intensity')

plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title('Light Intensity Graph')
plt.legend()
plt.show()
