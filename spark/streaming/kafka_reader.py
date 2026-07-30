from pyspark.sql import DataFrame, SparkSession

from configs.kafka_config import BOOTSTRAP_SERVERS, TOPIC_NAME


def read_kafka_stream(spark: SparkSession) -> DataFrame:
    """
    Reads streaming data from Kafka.

    Returns the raw Kafka DataFrame.
    """

    return (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", BOOTSTRAP_SERVERS)
        .option("subscribe", TOPIC_NAME)
        .option("startingOffsets", "latest")
        .option("failOnDataLoss", "false")
        .load()
    )