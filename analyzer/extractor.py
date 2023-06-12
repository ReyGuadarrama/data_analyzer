import re
import pandas as pd
import glob

class Extractor:
    path = str
    channels = int
    data = pd.DataFrame

    def __init__(self, path:str, *channels:int):
        '''The Extractor class is designed to retrieve specific data from raw textual information.

        Args:
                path (str): It is the location or directory where the raw textual information is stored.
                channels (int): It refers to the numeric identifier of each channel from which the data will be retrieved. The numbers should be comma-separated.
        '''
        self.path = path
        self.channels = channels

    def extractor(self, matches:list):
        '''The extractor method is designed to identify matches with the provided coincidence patterns and store their values in a data frame.

        Args:
            matches (list): A list of strings representing the coincidence patterns is used to extract specific data from the raw data.

        Returns:
            data (DataFrame): The data frame stores the extracted data from the raw data in a structured format for analysis and manipulation.
        '''
        dir_list = glob.glob(self.path)
        data_frames = []

        for file_path in dir_list:
            file_data = pd.DataFrame()

            with open(file_path, 'r') as file:
                lines = file.readlines()
                for match in matches:
                    for channel in self.channels:
                        extracted_data = []
                        for line in lines:
                            if f'CH: {channel}' in line:
                                value = re.search(rf'{match}:\s+([-0-9.]+)', line)
                                if value:
                                    extracted_data.append(float(value.group(1)))
                        file_data[f'{match}_ch{channel}'] = extracted_data

            data_frames.append(file_data)  
            self.data = pd.concat(data_frames, ignore_index=True)  

        return self.data
    

    def wave_forms(self, channel):
        '''The wave_form method extracts the waveform of each event from the raw data and stores them in a list.

        Args:
                channel (int): Specifies from which channel the waveforms will be extracted.

        Returns:
                wave_forms (list): A list is used to store all the waveforms of the events in the provided channel.
        '''
        dir_list = glob.glob(self.path)
        wave_forms = []
        found_match = False

        for file_path in dir_list:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if re.search(rf'CH: {channel}', line):
                        found_match = True
                    elif found_match:
                        line_values = line.split()
                        wave_forms.append(list(map(float, line_values)))
                        found_match = False
                
        return wave_forms
    
    def sampling_period(self):
        dir_list = glob.glob(self.path)
        found_match = False

        while found_match == False:

            for file_path in dir_list:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        if r'Sampling Period' in line:
                            value = re.search(r'Sampling Period:\s+([-0-9.]+)\s*([a-zA-Z]+)', line)
                            if value:
                                period = float(value.group(1))
                                units = value.group(2)
                                found_match = True
                                break
        
        return period, units
