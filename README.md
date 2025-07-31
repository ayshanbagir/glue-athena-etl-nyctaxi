# NYC Taxi Data ETL with AWS Glue and Athena

This project demonstrates an end-to-end data engineering workflow using publicly available NYC Yellow Taxi data. The pipeline ingests raw CSV files from S3, catalogs them with AWS Glue Crawlers, transforms them using AWS Glue Jobs, and enables querying with Amazon Athena.

## 📁 Folder Structure 

  
``` 

glue-athena-etl-nyctaxi/  
├── glue_job_script.py           
├── data/ 
│   ├── yellow_tripdata_2023-01.csv
│   └── taxi_zone_lookup.csv 
├── README.md                     
└── architecture.jpeg             

```

---

## 🧪 AWS Services Used
- **Amazon S3** – Storage for raw and processed data 
- **AWS Glue Crawler** - Scans and catalogs S3 data into Glue Data Catalog
- **AWS Glue (PySpark)** - Transforms the raw taxi trip data
- **Amazon Athena** - Queries processed data using SQL 
- **IAM Roles & Policies** - Permissions for Athena and Glue

---

## ✅ Summary of Steps

### 1. Created an S3 Bucket
Created a bucket `nyc-taxi-etl-ayshan` with folders `raw_data/` and `processed_data/` to simulate raw and processed data zones.

### 2. Created a Glue Crawler for Raw Data

### 3. Created a Glue ETL Job

### 4. Athena...

## 📷 Architecture Diagram

![Architecture Diagram](architecture.jpeg)
