from spark.utils.spark_session import create_spark_session
from datetime import datetime
from spark.audit.audit_logger import log_pipeline_run
from spark.batch.gold_transformations import *
from spark.batch.gold_writer import *


def main():

    spark = create_spark_session()

    # start_time = datetime.now()


    silver_df = read_silver(spark).cache()

    input_rows = silver_df.count()
    print(f"Silver Rows : {input_rows}")

    dim_application_df = create_dim_application(silver_df)
    dim_device_df = create_dim_device(silver_df)
    dim_product_df = create_dim_product(silver_df)
    dim_location_df = create_dim_location(silver_df)
    dim_date_df = create_dim_date(silver_df)
    dim_user_df = create_dim_user(silver_df)
    dim_session_df = create_dim_session(silver_df)

    fact_df = silver_df
    fact_df = lookup_application_key(fact_df, dim_application_df)
    fact_df = lookup_device_key(fact_df, dim_device_df)
    fact_df = lookup_product_key(fact_df, dim_product_df)
    fact_df = lookup_location_key(fact_df, dim_location_df)
    fact_df = lookup_user_key(fact_df, dim_user_df)
    fact_df = lookup_session_key(fact_df, dim_session_df)
    fact_df = lookup_date_key(fact_df, dim_date_df)

    fact_events_df = create_fact_events(fact_df)

    write_dim_application(dim_application_df)
    write_dim_device(dim_device_df)
    write_dim_product(dim_product_df)
    write_dim_location(dim_location_df)
    write_dim_date(dim_date_df)
    write_dim_user(dim_user_df)
    write_dim_session(dim_session_df)

    assert fact_events_df.filter(col("application_key").isNull()).count() == 0
    assert fact_events_df.filter(col("device_key").isNull()).count() == 0
    assert fact_events_df.filter(col("date_key").isNull()).count() == 0

    write_fact_events(fact_events_df)

    output_rows = fact_events_df.count()
    fact_events_df.printSchema()

    print(f"Dim Application Rows : {dim_application_df.count()}")
    print(f"Dim Device Rows      : {dim_device_df.count()}")
    print(f"Dim Product Rows     : {dim_product_df.count()}")
    print(f"Dim Location Rows    : {dim_location_df.count()}")
    print(f"Dim Date Rows        : {dim_date_df.count()}")
    print(f"Dim User Rows        : {dim_user_df.count()}")
    print(f"Dim Session Rows     : {dim_session_df.count()}")
    print(f"Fact Event Rows      : {output_rows}")

    # print("Fact Schema")
    # fact_events_df.printSchema()

    print(f"Fact Rows : {output_rows}")
    # fact_events_df.select(
    #     "application_key",
    #     "device_key",
    #     "product_key",
    #     "location_key",
    #     "user_key",
    #     "session_key",
    #     "date_key"
    # ).show(10, False)

    print("Gold Pipeline Completed Successfully.")

    spark.stop()

if __name__ == "__main__":
    main()