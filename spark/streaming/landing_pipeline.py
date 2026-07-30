from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    current_timestamp,
    to_date
)

from spark.streaming.kafka_reader import read_kafka_stream
from spark.streaming.spark_session import create_spark_session
from configs.storage_config import *

def write_landing(batch_df: DataFrame, batch_id: int):

    (
        batch_df.write
        .mode("append")
        .partitionBy("ingestion_date")
        .json(LANDING_PATH)
    )

def process_batch(batch_df, batch_id):

    landing_df = (
        batch_df.select(
            col("key").cast("string").alias("kafka_key"),
            col("value").cast("string").alias("raw_json"),
            col("topic"),
            col("partition"),
            col("offset"),
            col("timestamp").alias("kafka_timestamp")
        )
        .withColumn(
            "ingestion_timestamp",
            current_timestamp()
        )
        .withColumn(
            "ingestion_date",
            to_date(current_timestamp())
        )
    )

    write_landing(
        landing_df,
        batch_id
    )


def main():

    spark = create_spark_session()
    kafka_df = read_kafka_stream(spark)

    query = (
        kafka_df.writeStream
        .foreachBatch(process_batch)
        .option("checkpointLocation", LANDING_CHECKPOINT)
        .start()
    )

    query.awaitTermination()


if __name__ == "__main__":
    main()