# NYC Taxi Data ETL with AWS Glue and Athena

This project demonstrates an end-to-end data engineering workflow using publicly available NYC Yellow Taxi data. The pipeline ingests raw CSV files from S3, catalogs them with AWS Glue Crawlers, transforms them using AWS Glue Jobs, and enables querying with Amazon Athena.

## 📁 Folder Structure 

  
``` 

glue-athena-etl-nyctaxi/  
├── glue_job_script.py           
├── data/ 
│   ├── yellow_tripdata.csv
│   └── taxi_zone_lookup.csv 
├── README.md                     
└── architecture.jpeg             

```

---

## 🧪 AWS Services Used
- **Amazon S3** – Storage for raw and processed data 
- **AWS Glue Crawler** - Scans and catalogs S3 data into Glue Data Catalog
- **AWS Glue** - Transforms the raw taxi trip data
- **Amazon Athena** - Queries processed data using SQL

---

## ✅ Summary of Steps

### 1. Created an S3 Bucket
Created a bucket `nyc-taxi-etl-ayshan` with folders `raw_data/` and `transformed/` to simulate raw and transformed data zones. 
Uploaded `yellow_tripdata.csv` and `taxi_zone_lookup.csv` to `nyc-taxi-etl-ayshan/raw_data/`

<img width="1492" height="405" alt="image" src="https://github.com/user-attachments/assets/fc71785c-564b-46bd-af59-8f7d10cadb6d" />


### 2. Created a Glue Crawler for Raw Data
 - **Source**: `s3://nyc-taxi-etl-ayshan/raw_data/`
 - **Target database**: `nyc_taxi_db`

<img width="1217" height="345" alt="image" src="https://github.com/user-attachments/assets/f32449fb-06cf-43e5-985b-4c43684d7cf4" />


### 3. Created a Glue ETL Job
**Transformations**: 
- Filter: pickup time < dropoff time
- Filter: passenger_count between 1 and 6
- Enriched the trip data with vendor names
- Renamed some columns, etc.

**Output**: `s3://nyc-taxi-etl-ayshan/transformed/`

<img width="1478" height="508" alt="image" src="https://github.com/user-attachments/assets/733e131a-3995-423b-97f8-ff2dc878ac9b" />

### 4. Created another crawler for transformed data

<img width="1223" height="338" alt="image" src="https://github.com/user-attachments/assets/83e6cac8-9d49-4b2d-8bcc-b920dd0e5fcf" />

### 5. Queried with Amazon Athena
- Use Athena to connect to Glue Catalog
- Example Query:

<img width="1488" height="559" alt="image" src="https://github.com/user-attachments/assets/e0c4604c-4cd2-45d8-a6e8-b340067beeab" />


## 📷 Architecture Diagram

![Architecture Diagram](architecture.jpeg)
