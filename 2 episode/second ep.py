import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 4):
    f, axs = plt.subplots(2, 2, figsize=(8, 5))
    data1 = np.loadtxt('signal0' + str(i) + '.dat')
    data2 = np.ones(data1.shape[0])
    data2[0:9] = np.cumsum(data1[0:9]) / np.arange(1, 10)
    data2[9:] = np.convolve(data1, np.ones(10) / 10, mode='valid')

    x1 = [i for i in range(0, len(data1))]
    x2 = [i for i in range(0, len(data2))]

    plt.subplot(1, 2, 1)
    plt.grid()
    plt.plot(x1, data1, color='purple')
    plt.title('Сырой сигнал ' + str(i))
    plt.subplot(1, 2, 2)
    plt.grid()
    plt.plot(x2, data2, color='magenta')
    plt.title('После фильтра')
    plt.savefig('chart_signal0' + str(i) + '.png')
    # plt.show()