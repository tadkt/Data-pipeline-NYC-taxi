# Data-pipeline-NYC-taxi
1.  **Clone the repository**:

    ```bash
    git clone https://github.com/tadkt/Data-pipeline-NYC-taxi
    ```

2.  **Start all infrastructures**:

    ```bash
    make run_all
    ```

    This command will download the necessary Docker images, create containers, and start the services in detached mode.

3.  **Setup environment**:

    ```bash
    conda create -n bigdata python==3.9
    y
    conda activate bigdata
    pip install -r requirements.txt
    ```

    Activate your conda environment and install required packages

4.  **Access the Services**:

    - Postgres is accessible on the default port `5432`.
    - Kafka Control Center is accessible at `http://localhost:9021`.
    - Debezium is accessible at `http://localhost:8085`.
    - MinIO is accessible at `http://localhost:9001`.
    - Airflow is accessible at `http://localhost:8080`.

5.  **Download Dataset**:
    You can download and use this dataset in here: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

6.  **Download JAR files for Spark**:

    ```bash
    mkdir jars
    cd jars
    curl -O https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
    curl -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
    curl -O https://repo1.maven.org/maven2/org/postgresql/postgresql/42.4.3/postgresql-42.4.3.jar
    curl -O https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.2.1/spark-sql-kafka-0-10_2.12-3.2.1.jar
    ```

# 🔍 How to Guide

## I. Batch Processing

1.  **Push the data (parquet format) from local to `raw` bucket - Datalake (MinIO)**:

```bash
    python src/local_to_raw.py
```


    Pushed the data to MinIO successfully
</p>

2. **Process the data from `raw` to `processed` bucket (MinIO)**:

```bash
    python src/raw_to_processed.py
```

<p align="center">
<img src="./imgs/batch_2.png" width=100% height=100%>

<p align="center">
    Processed the data successfully
</p>

3. **Convert the data into Delta Lake format**:

```bash
    python src/processed_to_delta.py
```

<p align="center">
<img src="./imgs/batch_3.png" width=100% height=100%>

<p align="center">
    Converted the data successfully
</p>

4. **Create schema `staging`, `production` and table `staging.nyc_taxi` in PostgreSQL**

```bash
   python utils/create_schema.py
   python utils/create_table.py
```

5. **Execute Spark to read, process the data from Datalake (MinIO) and write to Staging Area**

```bash
   python batch_processing/datalake_to_dw.py
```

This command may take a little time to process.

<p align="center">
<img src="./imgs/batch_5.png" width=100% height=100%>

<p align="center">
    Queried the data after executing Spark
</p>

6. **Validate data in Staging Area**

```bash
   cd data_validation
   great_expectations init
   Y
```

Then, run the file `full_flow.ipynb`

<p align="center">
<img src="./imgs/batch_6.png" width=100% height=100%>

<p align="center">
    Validated the data using Great Expectations
</p>

7. **Use DBT to transform the data and create a star schema in the data warehouse**

```bash
   cd dbt_nyc
```

Allocation of tasks:

Data streaming: Lam & Dũng
- Our tasks contains creating a datastreaming pipeline to add new data to the datalake, using various tools like debezium and kafka

Data Batch:

Datalake: Hà
- Make a pipeline which manages the flow of raw data to usable datasets within a structured data lake, with Airflow automating each stage.
- The data is ingested, stored in raw format, processed, and then made available in an accessible form for data scientists to read and analyze.
- The system also leverages MinIO for scalable storage, Hive for metadata management, and Delta Lake for data reliability.

Data Warehouse: Kiên
- My task contains batch processing (writing from Datalake to Data Warehouse) and Data validation using Great Expectation

Link report:https://docs.google.com/document/d/1x_OtN-g_M4uhVbFck3hIFCr4fa2ndIRzgw0WtD4yFFg/edit?tab=t.0#heading=h.xv8dmjsbqpy0

Link slide: https://www.canva.com/design/DAGU3Y4J1QU/1a4I3R-MRD1obWPC-2SudQ/edit?utm_content=DAGU3Y4J1QU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Link Q&A prep: https://docs.google.com/document/d/1hUUOvRXj5vxNwpdOK65ZR_2w3_ta6X8DcOl9u1Xho70/edit?usp=sharing
