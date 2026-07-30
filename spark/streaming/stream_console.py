from pyspark.sql.functions import col

from spark.streaming.kafka_reader import read_kafka_stream
from spark.streaming.spark_session import create_spark_session


def main():
    spark = create_spark_session()

    kafka_df = read_kafka_stream(spark)

    stream_df = (
        kafka_df.select(
            col("topic"),
            col("partition"),
            col("offset"),
            col("timestamp"),
            col("value").cast("string").alias("message")
        )
    )

    query = (
        stream_df.writeStream
        .format("console")
        .outputMode("append")
        .option("truncate", False)
        .option("numRows", 20)
        .start()
    )

    query.awaitTermination()


if __name__ == "__main__":
    main()