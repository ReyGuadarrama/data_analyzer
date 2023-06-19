from grapher import Grapher
from extractor import Extractor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

class Signal_analyzer(Extractor, Grapher):
    waves = []
    channel = int


    def __init__(self, path, channel, offset_subtraction = True):
        Extractor.__init__(self, path, channel)
        self.waves = super().wave_forms(channel, offset_subtraction)
        self.channel = channel
        Grapher.__init__(self, *self.waves)

        
    def noise(self, n_signals=None, n_samples=50, sigma=5, graph=False):
        if n_signals is not None:
            signal_samples = random.sample(self.waves, n_signals)
        else:
            signal_samples = self.waves
        noise_sample = np.array([])
        for signal in signal_samples:
            noise_sample = np.concatenate((noise_sample, signal[:n_samples]))
        if graph:
            plt.figure(figsize=(16, 8))
            plt.hist(noise_sample, histtype='step', bins=50)
            plt.title(f'Noise distribution channel {self.channel}', fontsize = 25)
            plt.ylabel('counts', fontsize = 15)
            plt.xlabel('Noise [V]', fontsize = 15)
            plt.xticks(fontsize=15)
            plt.yticks(fontsize=15)
            plt.show()
        statistics = {
            'statistics': [round(np.mean(noise_sample), 4), round(np.std(noise_sample), 4), round(np.std(noise_sample)*sigma, 4)]
        }

        return pd.DataFrame(statistics, index=['mean [V]', 'std [V]', f'{sigma} sigma [V]'])

        

    def amplitude(self, negative_signal = False):
        amplitudes = []
        
        if negative_signal:
            for signal in self.waves:
                amplitude = np.min(signal)
                amplitudes.append(amplitude)
            return -np.array(amplitudes)
    
        else:
            for signal in self.waves:
                amplitude = np.max(signal)
                amplitudes.append(amplitude)

            return np.array(amplitudes)



    def charge(self, negative_signal = False, integration_window = [200, 500]):
        charges = []
        start, end = integration_window

        for signal in self.waves:
            window = np.array(signal[start:end])
            charge = (np.sum(window)*312.5)/50
            charges.append(charge)
        
        if negative_signal:
            return -np.array(charges)
        else:
            return np.array(charges) 


