import os
from dotenv import load_dotenv
from postgresql_client import PostgresSQLClient

load_dotenv(".env")

def main():
    pc = PostgresSQLClient(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

    schemas = ["CREATE SCHEMA IF NOT EXISTS iot;","CREATE SCHEMA IF NOT EXISTS staging;","CREATE SCHEMA IF NOT EXISTS production;"]

    for schema in schemas:
        try:
            pc.execute_query(schema)
            print(f"Schema created or already exists.")
        except Exception as e:
            print(f"Failed to create schema with error: {e}")

if __name__ == "__main__":
    main()