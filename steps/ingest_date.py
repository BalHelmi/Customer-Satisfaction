"""First Pipeline , we need to ingest the data , that's mean we read the data ad returns it"""

"""Import Libreries"""

import logging
import pandas as pd 
from zenml import step 

class Ingest_data:
    """
    Ingesting the data from the data path
    """
    def __init__(self, data_path:str):
        """
        Initialisation of the class 
        Args : 
            data_path : path to the data 
        """
        self.data_path = data_path

    def get_data(self):
        logging.info(f"Logging data from ${self.data_path}")
        return pd.read_csv(self.data_path)


@step
def ingest_data(data_path:str) -> pd.DataFrame:
    """
    Ingesting data from the data path 
    Args : 
        data_path : path to the data 
    Returns : 
        pd.dataftrame: the ingested data
    """    
    try:
        ingest_data = Ingest_data(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error whilr ingesting data : {e}")