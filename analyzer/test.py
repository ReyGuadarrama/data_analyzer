import re
import pandas as pd
import glob

class Test:
    matches = []
    channels = []
    path = str
    data = pd.DataFrame()

    def __init__(self, path, matches, channels):
        self.path = path
        self.matches = matches
        self.channels = channels

    def extraction(self):
        dir_list = glob.glob(self.path)
        data_frames = []

        for file_path in dir_list:
            file_data = pd.DataFrame()

            with open(file_path, 'r') as file:
                lines = file.readlines()
                for match in self.matches:
                    for channel in self.channels:
                        extracted_data = []
                        for line in lines:
                            if f'CH: {channel}' in line:
                                value = re.search(rf'{match}:\s+([-0-9.]+)', line)
                                if value:
                                    extracted_data.append(float(value.group(1)))
                        file_data[f'{match} CH: {channel}'] = extracted_data

            data_frames.append(file_data)  
            self.data = pd.concat(data_frames, ignore_index=True)  

        return self.data
    
    def wave_forms(self, channel):
        wave_forms = []
        found_match = False

        with open(self.path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if re.search(rf'CH: {channel}', line):
                    found_match = True
                elif found_match:
                    line_values = line.split()
                    wave_forms.append(list(map(float, line_values)))
                    found_match = False
                
        return wave_forms
