# Start from a lightweight Python 3.10 base image
FROM python:3.10-slim

# Set Airflow home and working directory
ENV AIRFLOW_HOME=/opt/airflow
WORKDIR $AIRFLOW_HOME

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
   && apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Apache Airflow 2.10.5 (with celery extra) using constraints for Python 3.10
RUN pip install --upgrade pip && \
    pip install "apache-airflow[celery]==2.10.5" \
      --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.10.txt"

# Copy the requirements.txt from the project root (relative to the build context)
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the DAGs from the airflow folder
COPY airflow/dags $AIRFLOW_HOME/dags

# Copy your source code and modules
COPY src $AIRFLOW_HOME/src
COPY etl $AIRFLOW_HOME/etl

# Expose Airflow's default webserver port
EXPOSE 8080

# Run Airflow in standalone mode
CMD ["airflow", "standalone"]
