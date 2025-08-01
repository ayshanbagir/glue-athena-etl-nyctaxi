import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from awsglue.transforms import Join


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load source data
dyf_yellow = glueContext.create_dynamic_frame.from_catalog(
    database="nyc_taxi_db",
    table_name="raw_yellow_tripdata"
)

dyf_zones = glueContext.create_dynamic_frame.from_catalog(
    database="nyc_taxi_db",
    table_name="raw_taxi_zone"
)
# Convert them to dataframe
df_yellow = dyf_yellow.toDF()
df_zones = dyf_zones.toDF()

# Pickup time should be lower than dropoff time
df_yellow = df_yellow.filter(df_yellow["tpep_pickup_datetime"] < df_yellow["tpep_dropoff_datetime"])

# Passenger count should be between 1 and 6 for a typical yellow cab
df_yellow = df_yellow.filter(df_yellow["passenger_count"].between(1, 6))

# Rename columns
df_yellow = df_yellow.withColumnRenamed("tpep_pickup_datetime", "pickup_datetime") \
                     .withColumnRenamed("tpep_dropoff_datetime", "dropoff_datetime")

# Join and Transform
df_joined = df_yellow.join(df_zones, df_yellow["PULocationID"] == df_zones["LocationID"], "left")

from pyspark.sql import Row
# Define vendor data
vendor_data = [
    Row(ID=1, VendorName="Creative Mobile Technologies, LLC"),
    Row(ID=2, VendorName="Curb Mobility, LLC"),
    Row(ID=6, VendorName="Myle Technologies Inc"),
    Row(ID=7, VendorName="Helix")
]

# Create DataFrame
df_vendor = spark.createDataFrame(vendor_data)

# Join and get final data
df_final = df_joined.join(df_vendor, df_joined["VendorID"] == df_vendor["ID"], "left")

from pyspark.sql.functions import col

df_final = df_final.select("VendorID", "VendorName", "pickup_datetime", "dropoff_datetime", "passenger_count",
         "trip_distance", "PULocationID", "Borough", "Zone", "payment_type", "fare_amount", "tip_amount", 
         "tolls_amount", \
        (col("extra") + col("mta_tax") + col("improvement_surcharge") + col("congestion_surcharge")).alias("other_amounts"))
         
dyf_final = DynamicFrame.fromDF(df_final, glueContext, "dyf_final")

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame=dyf_final,
    connection_type="s3",
    connection_options={"path": "s3://nyc-taxi-etl-ayshan/transformed/"},
    format="parquet"
)

job.commit()