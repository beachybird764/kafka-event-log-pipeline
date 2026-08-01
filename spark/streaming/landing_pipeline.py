from pyspark.sql import DataFrame
from pyspark.sql.functions import lit
from pyspark.sql.functions import (
    col,
    current_timestamp,
    to_date
)
from spark.streaming.kafka_reader import read_kafka_stream
from spark.utils.spark_session import create_spark_session
from spark.streaming.json_parser import parse_event_stream
from configs.storage_config import (
    LANDING_PATH,
    BRONZE_PATH,
    INGESTION_CHECKPOINT,
)

def write_landing(batch_df: DataFrame) -> None:

    (
        batch_df.write
        .mode("append")
        .partitionBy("ingestion_date")
        .json(LANDING_PATH)
    )

def write_bronze(bronze_df) -> None:

    (
        bronze_df.write
        .format("delta")
        .mode("append")
        .partitionBy("event_date")
        .option("mergeSchema", "true")
        .save(BRONZE_PATH)
    )

def prepare_bronze_df(batch_df, batch_id):

    bronze_df = parse_event_stream(batch_df)

    bronze_df = (
        bronze_df
        .withColumn("event_date", to_date("event_timestamp"))
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("batch_id", lit(batch_id))
    )

    return bronze_df

def process_batch(batch_df, batch_id) -> None:

    landing_df = (
        batch_df.select(
            col("key").cast("string").alias("kafka_key"),
            col("value").cast("string").alias("raw_json"),
            col("topic"),
            col("partition"),
            col("offset"),
            col("timestamp").alias("kafka_timestamp")
        )
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("ingestion_date", to_date(current_timestamp()))
        .withColumn("batch_id", lit(batch_id))
    )

    bronze_df = prepare_bronze_df(batch_df, batch_id)

    landing_df = landing_df.cache()
    bronze_df = bronze_df.cache()

    write_landing(landing_df)
    write_bronze(bronze_df)

    print("=" * 80)
    print(f"Batch ID : {batch_id}")
    print(f"Landing Rows : {landing_df.count()}")
    print(f"Bronze Rows  : {bronze_df.count()}")
    print("=" * 80)

    landing_df.unpersist()
    bronze_df.unpersist()


def main():

    spark = create_spark_session()
    kafka_df = read_kafka_stream(spark)

    query = (
        kafka_df.writeStream
        .foreachBatch(process_batch)
        .option("checkpointLocation", INGESTION_CHECKPOINT)
        .start()
    )

    query.awaitTermination()


if __name__ == "__main__":
    main()