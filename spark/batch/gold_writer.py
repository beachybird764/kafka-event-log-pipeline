from pyspark.sql import DataFrame
from configs.storage_config import (
    DIM_APPLICATION_PATH,
    DIM_DEVICE_PATH,
    DIM_PRODUCT_PATH,
    DIM_LOCATION_PATH,
    DIM_DATE_PATH,
    DIM_USER_PATH,
    DIM_SESSION_PATH,
    FACT_EVENTS_PATH,
    SILVER_PATH
)

def write_dim_application(df: DataFrame) -> None:
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(DIM_APPLICATION_PATH)
    )


def write_dim_device(df: DataFrame) -> None:
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(DIM_DEVICE_PATH)
    )


def write_dim_product(df: DataFrame) -> None:
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(DIM_PRODUCT_PATH)
    )


def write_dim_location(df: DataFrame) -> None:
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(DIM_LOCATION_PATH)
    )


def write_dim_date(df: DataFrame) -> None:
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(DIM_DATE_PATH)
    )

def write_dim_user(df: DataFrame) -> None:
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(DIM_USER_PATH)
    )


def write_dim_session(df: DataFrame) -> None:
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(DIM_SESSION_PATH)
    )

def write_fact_events(df: DataFrame) -> None:
    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .partitionBy("event_date")
        .save(FACT_EVENTS_PATH)
    )

def read_silver(spark) -> DataFrame:
    return (
        spark.read
        .format("delta")
        .load(SILVER_PATH)
    )

def read_dim_application(spark) -> DataFrame:
    return spark.read.format("delta").load(DIM_APPLICATION_PATH)


def read_dim_device(spark) -> DataFrame:
    return spark.read.format("delta").load(DIM_DEVICE_PATH)


def read_dim_product(spark) -> DataFrame:
    return spark.read.format("delta").load(DIM_PRODUCT_PATH)


def read_dim_location(spark) -> DataFrame:
    return spark.read.format("delta").load(DIM_LOCATION_PATH)


def read_dim_date(spark) -> DataFrame:
    return spark.read.format("delta").load(DIM_DATE_PATH)


def read_dim_user(spark) -> DataFrame:
    return spark.read.format("delta").load(DIM_USER_PATH)


def read_dim_session(spark) -> DataFrame:
    return spark.read.format("delta").load(DIM_SESSION_PATH)