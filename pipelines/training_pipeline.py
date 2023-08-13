from zenml import pipeline
from steps.ingest_date import ingest_data
from steps.clean_data import clean_df
from steps.train_model import  train_model
from steps.evaluate_model import evaluate_model

@pipeline
def training_pipeline(data_path: str):
    df = ingest_data(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)
