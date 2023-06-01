import pandas as pd
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

