import os
import pandas as pd
from dotenv import load_dotenv
from google.cloud import bigquery
load_dotenv()

from etl.clean_data import preprocess_data
from etl.exchange_rates import get_exchange_rates, price_to_euro
from etl.gcp_utils import get_client, run_query, push_to_bq
from etl.queries import query_raw_data
import google.auth

# Get environment variables
BRAND = os.getenv("BRAND")
service_account_path = os.getenv('GCP_SERVICE_ACCOUNT')
COLUMNS = "uid,reference_code,brand,url,image_url,collection,life_span_date,price,currency,price_euro".split(",")

def etl():
    
    # Load data from biqquery table
    client = get_client(service_account_path=service_account_path)
    
    # Retrieve raw data
    raw_query = query_raw_data(BRAND)
    
    # Run query and retrivee dataframe
    raw_data = run_query(raw_query, client)
    
    # Add exchange rates
    exchange_rates = get_exchange_rates()
    if exchange_rates is None:
        return 1
    elif not isinstance(exchange_rates, pd.DataFrame):
        raise ValueError("Exchange rates should be a DataFrame")
    
    # Add price_euro column
    data = price_to_euro(raw_data, exchange_rates)
    
    # Clean data
    clean_data = preprocess_data(data, columns=COLUMNS)
    
    # Push data to BigQuery
    push_to_bq(clean_data, BRAND.lower(), f"preprocessed_{BRAND.lower()}", client)
    
    return 0

if __name__ == "__main__":
    etl()