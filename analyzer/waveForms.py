from grapher import Grapher
from extractor import Extractor
import numpy as np
import pandas as pd
import random

class Signal_analyzer(Extractor, Grapher):
    wave_forms = []


    def __init__(self, path, channel):
        Extractor.__init__(self, path, channel)
        self.wave_forms = super().wave_forms(channel)
        Grapher.__init__(self, self.wave_forms)

    def noise(self, n_signals = None, n_samples = 100):
        if n_signals is None:
            n_signals = len(self.wave_forms)
        noise_sample = []
        signal_samples = random.sample(self.wave_forms, n_signals)
        for signal in signal_samples:
            noise_sample += signal[-n_samples:]
        statistics = {'statistics' : [round(np.mean(noise_sample), 4),
                round(np.std(noise_sample), 4)]}
        
        return pd.DataFrame(statistics, index = ['mean', 'std'])
    
'''    def rise_time(self, n_signals = None, initial_percentage = 10, final_percentage = 90):
        if n_signals is None:
            n_signals = len(self.wave_forms)
        signal_samples = random.sample(self.wave_forms, n_signals)
        rise_time = []
        #period = super().sampling_period()[0]
        for signal in signal_samples:
            max = np.max(signal)
            start_value = initial_percentage*max
            final_value = final_percentage*max

            start_time = np.argmax(signal >= start_value)
            final_time = np.argmax(signal >= final_value)

            delta_time = (final_time - start_time)
            rise_time.append(delta_time)
        
        statistics = {'statistics' : [round(np.mean(rise_time), 4),
                round(np.std(rise_time), 4)]}
        
        return pd.DataFrame(statistics, index = ['mean', 'std'])'''
        

