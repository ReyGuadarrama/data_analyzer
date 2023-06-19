import matplotlib.pyplot as plt
import seaborn as sns
from extractor import Extractor
import numpy as np
import pandas as pd

class Grapher:
    data = any
    modes = {}

    def __init__(self, *data):
        self.data = data
        
    def signal_plot(self, first, last):
        period, units = Extractor.sampling_period(self)
        time_axis = np.arange(len(self.data[0]))*period*(1e-9)
        plt.figure(figsize=(16, 8))
        for signal in self.data[first:last]:
            plt.plot(time_axis, signal)
        plt.title(f'Events {first}-{last-1}', fontsize = 25)
        plt.xlabel('Time [s]', fontsize = 15)
        plt.ylabel('Voltage [V]', fontsize = 15)
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.show()

    def dist(self, data, bins=50):
        plt.figure(figsize=(16, 8))
        sns.displot(data, kde=True, bins=50)
        plt.title('Noise distribution', fontsize = 25)
        plt.xlabel('Noise [V]')


    def histo(self, *data, flip = False, figure = True, stats = False, label = None):
        if figure:
            plt.figure(figsize=(16,8))
        for datum in data:
            if label is None:
                label = datum[-3:]
            else:
                label = label
            if flip:
                hist, bins, _ = plt.hist(-self.data[datum], bins=self.bins, label=label, histtype='step')
            else:
                hist, bins, _ = plt.hist(self.data[datum], bins=self.bins, label=label, histtype='step')
            max_index = np.argmax(hist)
            mode = bins[max_index]
            self.modes[datum] = mode
            if stats:
                mean = np.mean(self.data[datum])
                std = np.std(self.data[datum])
                plt.text(0.75, 0.7, f'Mean: {mean:.3f}\nStandard Deviation: {std:.3f}\nMost Probable Value: {mode:.3f}', transform=plt.gca().transAxes, fontsize=15)
        plt.legend(loc=1, prop={'size':20})
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)

    def stats(self):
        statistics = { columnName : [round(np.mean(columnData), 3), round(np.std(columnData), 3), round(self.modes[columnName], 3) ] for columnName, columnData in self.data.transpose().iterrows()}
        df = pd.DataFrame(statistics, index=['mean', 'std', 'Mode'])
        return df
    

