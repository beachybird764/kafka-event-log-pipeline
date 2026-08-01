from pyspark.sql import DataFrame
from pyspark.sql.functions import col, from_json

from spark.streaming.schemas import EVENT_SCHEMA


def parse_event_stream(kafka_df: DataFrame) -> DataFrame:

    return (
        kafka_df
        .select(
            from_json(
                col("value").cast("string"),
                EVENT_SCHEMA
            ).alias("event")
        )
        .select("event.*")
    )

from spark.streaming.kafka_reader import read_kafka_stream
from spark.utils.spark_session import create_spark_session


def main():

    spark = create_spark_session()

    kafka_df = read_kafka_stream(spark)

    parsed_df = parse_event_stream(kafka_df)

    query = (
        parsed_df.writeStream
        .format("console")
        .outputMode("append")
        .option("truncate", False)
        .start()
    )

    query.awaitTermination()


if __name__ == "__main__":
    main()