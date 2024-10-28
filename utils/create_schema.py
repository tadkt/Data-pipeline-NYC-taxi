import os
import logging
from dotenv import load_dotenv
from postgresql_client import PostgresSQLClient

# Load environment variables from .env file
load_dotenv(".env")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_tables(pc):
    """
    Create the necessary tables in the PostgreSQL database.
    """
    create_table_iot = """
        CREATE TABLE IF NOT EXISTS iot.taxi_nyc_time_series( 
            VendorID                INT, 
            tpep_pickup_datetime    TIMESTAMP WITHOUT TIME ZONE, 
            tpep_dropoff_datetime   TIMESTAMP WITHOUT TIME ZONE, 
            passenger_count         FLOAT, 
            trip_distance           FLOAT, 
            RatecodeID              FLOAT, 
            store_and_fwd_flag      VARCHAR, 
            PULocationID            INT, 
            DOLocationID            INT, 
            payment_type            INT, 
            fare_amount             FLOAT, 
            extra                   FLOAT, 
            mta_tax                 FLOAT, 
            tip_amount              FLOAT, 
            tolls_amount            FLOAT, 
            improvement_surcharge   FLOAT, 
            total_amount            FLOAT, 
            congestion_surcharge    FLOAT, 
            Airport_fee             FLOAT
        );
    """

    create_table_staging = """
        CREATE TABLE IF NOT EXISTS staging.nyc_taxi (
            year                    VARCHAR,
            month                   VARCHAR,
            dow                     VARCHAR,
            vendor_id               INT, 
            rate_code_id            FLOAT, 
            pickup_location_id      INT, 
            dropoff_location_id     INT, 
            payment_type_id         INT, 
            service_type            INT,
            pickup_datetime         TIMESTAMP WITHOUT TIME ZONE, 
            dropoff_datetime        TIMESTAMP WITHOUT TIME ZONE, 
            pickup_latitude         FLOAT,
            pickup_longitude        FLOAT,
            dropoff_latitude       FLOAT,
            dropoff_longitude       FLOAT,
            passenger_count         FLOAT, 
            trip_distance           FLOAT,
            extra                   FLOAT, 
            mta_tax                 FLOAT, 
            fare_amount             FLOAT, 
            tip_amount              FLOAT, 
            tolls_amount            FLOAT, 
            total_amount            FLOAT, 
            improvement_surcharge   FLOAT, 
            congestion_surcharge    FLOAT
        );
    """

    try:
        logging.info("Creating tables in the database")
        pc.execute_query(create_table_iot)
        pc.execute_query(create_table_staging)
        logging.info("Tables created successfully.")
    except Exception as e:
        logging.error(f"Failed to create tables: {e}")

def main():
    # Initialize the PostgreSQL client
    pc = PostgresSQLClient(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

    # Create the tables
    create_tables(pc)

if __name__ == "__main__":
    main()