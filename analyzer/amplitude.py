import pandas as pd
import matplotlib.pyplot as plt
from extractor import Extractor
from grapher import Grapher

class Amplitude_analyzer(Extractor, Grapher):
    path = str
    channels = []
    data = pd.DataFrame
    modes = {}
    bins = int


    def __init__(self,path, *channels, bins = 100):
        super().__init__(path, *channels)
        self.bins = bins
        self.data = super().extractor(['Amplitude'])

    def histo_channels(self, *channels, flip=False):
        data = []
        for channel in channels:
            datum = f'Amplitude_ch{channel}'
            data.append(datum)
        data = tuple(data)
        super().histo(*data, flip=flip, figure=True, label=None)
        plt.title('Amplitude', fontsize = 25)
        plt.ylabel('events', fontsize = 15)
        plt.xlabel('Amplitude [V]', fontsize = 15)
        plt.show()

    def histo(self, *channels, flip=False, label=None):
        data = []
        for channel in channels:
            datum = f'Amplitude_ch{channel}'
            data.append(datum)
        data = tuple(data)
        super().histo(*data, flip=flip, figure=False, label=label)
        
    @classmethod
    def histo_runs(cls, *instancias, channel = 4, flip=False, labels=None, title=None):
        plt.figure(figsize=(16, 8))

        for i, instancia in enumerate(instancias):
            label = None
            if labels is not None and i < len(labels):
                label = labels[i]
            instancia.histo(channel, flip=flip, label=label)
        if title is None:
            plt.title('Amplitude', fontsize=25)
        else:
            plt.title(f'Amplitude {title}', fontsize=20)
        plt.ylabel('events', fontsize=15)
        plt.xlabel('Amplitude [V]', fontsize=15)
        plt.legend(prop={'size': 20})
        plt.show()
