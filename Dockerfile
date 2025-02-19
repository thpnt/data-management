# Dockerfile

FROM python:3.10-slim

# Create and set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code into the image
COPY . .
COPY gcp_service_account.json /app/gcp_service_account.json

# Expose port 8080 (Cloud Run's default)
EXPOSE 8080

# Run the app with uvicorn (or use CMD if you like)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]