from dotenv import load_dotenv
import os
load_dotenv()

BRAND = os.getenv("BRAND")
BRAND_LOWER = BRAND.lower()


def query_raw_data(brand=BRAND):
    return f"""
    SELECT * 
    FROM `edhec-business-manageme.luxurydata2502.price-monitoring-2022` 
    WHERE brand = "{brand}"
    """