import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
            
      

class CustomData:
    def __init__(self,
                 cap-shape:str,
                 cap-surface:str,
                 cap-color:str,
                 bruises:str,
                 odor:str,
                 gill-attachment:str,
                 gill-spacing:str,
                 gill-size:str,
                 gill-color:str,
                 stalk-shape:str,
                 stalk-root:str,
                 stalk-surface-above-ring:str,
                 stalk-surface-below-ring:str,
                 stalk-color-above-ring:str,
                 stalk-color-below-ring:str,
                 veil-color:str,
                 ring-number:str,
                 ring-type:str,
                 spore-print-color:str,
                 population:str,
                 habitat:str):
    
    
    

    
        self.cap-shape=cap-shape
        self.cap-surface=cap-surface
        self.cap-color=cap-color
        self.bruises=bruises
        self.odor=odor
        self.gill-attachment=gill-attachment
        self.gill-spacing=gill-spacing
        self.gill-size=gill-size
        self.gill-color=gill-color
        self.stalk-shape=stalk-shape
        self.stalk-root=stalk-root
        self.stalk-surface-above-ring=stalk-surface-above-ring
        self.stalk-surface-below-ring=stalk-surface-below-ring
        self.stalk-color-above-ring=stalk-color-above-ring
        self.stalk-color-below-ring=stalk-color-below-ring
        self.veil-color=veil-color
        self.ring-number=ring-number
        self.ring-type=ring-type
        self.spore-print-color=spore-print-color
        self.population=population
        self.habitat=habitat


    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'cap-shape':[self.cap-shape],
                'cap-surface':[self.cap-surface],
                'cap-color':[self.cap-color],
                'bruises':[self.bruises],
                'odor':[self.odor],
                'gill-attachment':[self.gill-attachment],
                'gill-spacing':[self.gill-spacing],
                'gill-size':[self.gill-size],
                'gill-color':[self.gill-color],
                'stalk-shape':[self.stalk-shape],
                'stalk-root':[self.stalk-root],  
                'stalk-surface-above-ring':[self.stalk-surface-above-ring],
                'stalk-surface-below-ring':[self.stalk-surface-below-ring],
                'stalk-color-above-ring':[self.stalk-color-above-ring],
                'stalk-color-below-ring':[self.stalk-color-below-ring],
                'veil-color':[self.veil-color],
                'ring-number':[self.ring-number],
                'ring-type':[self.ring-type],
                'spore-print-color':[self.spore-print-color],
                'population':[self.population],
                'habitat':[self.habitat]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)