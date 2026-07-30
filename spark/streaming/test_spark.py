from spark.streaming.kafka_reader import read_kafka_stream
from spark.streaming.spark_session import create_spark_session


def main():
    spark = create_spark_session()

    kafka_df = read_kafka_stream(spark)

    kafka_df.printSchema()

    spark.stop()


if __name__ == "__main__":
    main()