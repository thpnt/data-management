import os
from dotenv import load_dotenv
from google.cloud import bigquery
import pandas as pd
from pandas_gbq import to_gbq

# Load environment variables
load_dotenv()
service_account_path = os.getenv('GCP_SERVICE_ACCOUNT')


# Get BigQuery client
def get_client(service_account_path=service_account_path):
    """
    Given a path to a service account, return a BigQuery client
    """
    client = bigquery.Client.from_service_account_json(service_account_path)
    return client

# Run a query and return the results as a pandas DataFrame
def run_query(query, client):
    """
    Given a query and a bigquery client, run the query and return the results as a pandas DataFrame
    """
    return client.query(query).to_dataframe()

# Write a table via query
def write_table(query, dataset, table, client):
    """
    Given a query, dataset, table, and bigquery client, write the results of the query to the specified table
    """
    try:
        job_config = bigquery.QueryJobConfig(destination=f'{client.project}.{dataset}.{table}', write_disposition='WRITE_TRUNCATE')
        query_job = client.query(query, job_config=job_config)
        query_job.result()
        print(f'Successfully wrote table {table} to {dataset}')
    except Exception as e:
        print(f'Error writing table {table} to {dataset}')
        print(e)
        return 1
    return 0

# Get a list of tables in a dataset
def list_tables(dataset: str):
    """
    Given a dataset, return a list of tables in that dataset
    """
    client = get_client()
    dataset_ref = client.dataset(dataset)
    tables = client.list_tables(dataset_ref)
    return [table.table_id for table in tables]

# Push dataframe to bq
def push_to_bq(df, dataset, table, client):
    """
    Given a dataframe, dataset, table, and bigquery client, push the dataframe to the specified table
    """
    try:
        to_gbq(df, f'{dataset}.{table}', if_exists='replace', project_id=client.project,
                  credentials=client._credentials)
        print(f'Successfully pushed {table} to {dataset}')
    except Exception as e:
        print(f'Error pushing {table} to {dataset}')
        print(e)
        return 1
    return 0


# GCP Storage
bucket = os.getenv('GCP_BUCKET')
RAW_DATA_FILE = os.getenv('RAW_DATA_FILE')
PROCESSED_DATA_FILE = os.getenv('PROCESSED_DATA_FILE')


# Retrieve data from GCS
def get_data_from_storage(bucket=bucket, file_name=RAW_DATA_FILE):
    """
    Given a bucket and a file name, return the file as a pandas DataFrame
    """
    try:
        client = get_client()
        bucket = client.get_bucket(bucket)
        blob = bucket.blob(file_name)
        data = pd.read_csv(blob.download_as_string())
        return data
    except Exception as e:
        print(f'Error retrieving data from {bucket}/{file_name}')
        print(e)
        return None

# Push data to GCS
def push_data_to_storage(bucket=bucket, file_name=PROCESSED_DATA_FILE, data=None):
    """
    Given a bucket, file name, and data, push the data to the specified file in GCS
    """
    try:
        client = get_client()
        bucket = client.get_bucket(bucket)
        blob = bucket.blob(file_name)
        blob.upload_from_string(data.to_csv(index=False), 'text/csv')
        print(f'Successfully pushed data to {bucket}/{file_name}')
        return 0
    except Exception as e:
        print(f'Error pushing data to {bucket}/{file_name}')
        print(e)
        return 1


