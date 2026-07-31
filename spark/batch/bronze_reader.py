from pyspark.sql import SparkSession, DataFrame
from configs.storage_config import (
    BRONZE_PATH,
    SILVER_PATH
)

def write_silver(df: DataFrame) -> None:

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .partitionBy("event_date")
        .save(SILVER_PATH)
    )

def read_bronze(spark: SparkSession) -> DataFrame:

    return (
        spark.read
        .format("delta")
        .load(BRONZE_PATH)
    )