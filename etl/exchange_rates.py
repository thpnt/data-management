import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("ERATE_API")


# Retrieve exchange rates
def get_exchange_rates():
    """
    Retrieve exchange rates from the API
    """
    try:
        response = requests.get(API_URL)
        res = response.json()
        conversion_rates = res["conversion_rates"]
        er_df = pd.DataFrame(list(conversion_rates.items()), columns=["Currency", "Exchange Rate"])
        return er_df
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    
def price_to_euro(data: pd.DataFrame, exchange_rates: pd.DataFrame):
    """
    Convert prices to Euro and add a price_euro column
    """
    data["price_euro"] = data["price"] / data["currency"].map(exchange_rates.set_index("Currency")["Exchange Rate"])
    return data
    



