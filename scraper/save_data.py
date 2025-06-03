import pandas as pd
import os
from pathlib import Path
import scraper.configer as configer

class Save:

    def csv(data : dict):
        '''
            Get the data and save it as a csv file
        
            Args:
                data (dict) : the data to save
        '''

        # check if the output.csv exsits or not for headers
        header = not os.path.isfile(f'{os.getcwd()}/{configer.SAVE_DATA_DIR}/output.csv')

        # save data as csv file
        pd.DataFrame([data]).to_csv(
            f"{os.getcwd()}/{configer.SAVE_DATA_DIR}/output.csv", mode="a", header=header, index=False)


