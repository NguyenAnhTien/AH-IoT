
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('/data/projects/AH-IoT/data_case_2.csv', delimiter=';', unpack=True)

plt.plot(x,y, label='Light Intensity')

plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title('Light Intensity Graph')
plt.legend()
plt.show()
