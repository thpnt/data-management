import os
import pandas as pd


def preprocess_data(data: pd.DataFrame, columns: list):
    """
    Take a dataframe and return a preprocessed version dataframe
    - Keep only columns of interest
    - Drop rows with missing values
    - Drop duplicate rows
    """
    # Keep columns of interest
    data = data[columns]
    
    # Keep only the rows where the price is not null
    data = data[data["price"].notnull()]
    
    # Order data by collections and life_span_date
    data = data.sort_values(by=["collection", "life_span_date"])
    
    # Round price in euro
    data["price_euro"] = data["price_euro"].round(2)
    
    # Drop NA and duplicates
    data = data.dropna()
    data = data.drop_duplicates()
    
    return data
    
    