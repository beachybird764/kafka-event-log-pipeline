from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    year,
    month,
    dayofmonth,
    hour,
    date_format,
    when,
    col
)

def apply_silver_transformations(df: DataFrame) -> DataFrame:

    df = (
        df
        .dropDuplicates(["event_id"])
        .dropna(subset=["event_id", "event_timestamp", "application_id", "user_id", "session_id", "event_type"])
        .filter("response_time_ms >= 0")
        .filter("(price IS NULL) OR (price >= 0)")
        .filter("(quantity IS NULL) OR (quantity > 0)")
    )

    df = (
        df
        .withColumn("event_year", year("event_timestamp"))
        .withColumn("event_month", month("event_timestamp"))
        .withColumn("event_day", dayofmonth("event_timestamp"))
        .withColumn("event_hour", hour("event_timestamp"))
        .withColumn("event_weekday", date_format("event_timestamp", "EEEE"))
    )

    df = (
        df
        .withColumn("event_category",
            when(col("event_type").isin("LOGIN", "LOGOUT"),"Authentication")
            .when(col("event_type").isin("APP_OPEN"),"Application")
            .when(col("event_type").isin("SEARCH", "PRODUCT_VIEW", "ADD_TO_CART", "CHECKOUT"),"Shopping")
            .when(col("event_type").isin("PAYMENT_SUCCESS", "PAYMENT_FAILED"),"Payment")
            .otherwise("Other")
        )
    )

    df = (
        df
        .withColumn("purchase_amount",
            when(
                col("price").isNotNull() & col("quantity").isNotNull(),
                col("price") * col("quantity")
            ).otherwise(None)
        )
        .withColumn("payment_success", (col("payment_status") == "SUCCESS"))
        .withColumn("response_bucket",
            when(col("response_time_ms") < 200,"Fast")
            .when(col("response_time_ms") < 500,"Medium")
            .otherwise("Slow")
        )
    )

    return df