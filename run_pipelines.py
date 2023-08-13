from pipelines.training_pipeline import training_pipeline

if __name__ == "__main__":
    """
    Run pipeline
    """
    data_path = "/home/linux/Desktop/helmi/Customer_Satisfaction/data/olist_customers_dataset.csv"
    training_pipeline(data_path)