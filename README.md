# Data-pipeline-NYC-taxi
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

Link report: https://docs.google.com/document/d/1tgOSFVxPbTe6VVv3KJAw8KcMDtaScHIMLvDFwlwrHSM/edit?usp=sharing
