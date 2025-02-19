# app.py
from fastapi import FastAPI
import uvicorn

# Import the ETL main() function
from etl import etl

app = FastAPI()

@app.get("/")
async def trigger_etl():
    """
    Endpoint to trigger the ETL job.
    Calls the main() function in script.py and
    returns a JSON response with status info.
    """
    try:
        result = etl()  # main() returns 0 if successful
        if result == 0:
            return {"message": "ETL job completed successfully.", "status_code": 0}
        else:
            return {"message": "ETL job encountered an issue.", "status_code": result}
    except Exception as e:
        return {"message": f"ETL job failed with error: {str(e)}", "status_code": 1}

# Only needed if you want to run locally: "python app.py"
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080)
