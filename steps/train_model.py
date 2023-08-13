import logging
import pandas as pd 
from zenml import step

@step
def train_model(df:pd.dataframe) -> pd.dataframe:
    pass  
