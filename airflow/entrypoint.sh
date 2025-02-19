# Initialize the Airflow database
airflow db init

# Create the admin user if it doesn't exist
if ! airflow users list | grep -q 'admin'; then
    airflow users create \
        --username admin \
        --firstname Admin \
        --lastname User \
        --role Admin \
        --email admin@example.com \
        --password admin
fi

# Execute the original entrypoint command
exec "$@"