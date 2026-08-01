from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    row_number,
    quarter,
    weekofyear
)
from pyspark.sql.window import Window
from pyspark.sql.functions import broadcast, date_format


# ==========================================================
# APPLICATION DIMENSION
# ==========================================================

def create_dim_application(df: DataFrame) -> DataFrame:

    window = Window.orderBy("application_id")

    return (
        df
        .select(
            "application_id",
            "application_version"
        )
        .distinct()
        .withColumn(
            "application_key",
            row_number().over(window)
        )
        .select(
            "application_key",
            "application_id",
            "application_version"
        )
    )


# ==========================================================
# DEVICE DIMENSION
# ==========================================================

def create_dim_device(df: DataFrame) -> DataFrame:

    window = Window.orderBy("device_id")

    return (
        df
        .select(
            "device_id",
            "device_type",
            "device_model",
            "os_version"
        )
        .distinct()
        .withColumn(
            "device_key",
            row_number().over(window)
        )
        .select(
            "device_key",
            "device_id",
            "device_type",
            "device_model",
            "os_version"
        )
    )


# ==========================================================
# PRODUCT DIMENSION
# ==========================================================

def create_dim_product(df: DataFrame) -> DataFrame:

    window = Window.orderBy("product_id")

    return (
        df
        .filter(col("product_id").isNotNull())
        .filter(col("product_name").isNotNull())
        .select(
            "product_id",
            "product_name",
            "category",
            "brand"
        )
        .distinct()
        .withColumn("product_key", row_number().over(window))
        .select(
            "product_key",
            "product_id",
            "product_name",
            "category",
            "brand"
        )
    )


# ==========================================================
# LOCATION DIMENSION
# ==========================================================

def create_dim_location(df: DataFrame) -> DataFrame:

    window = Window.orderBy(
        "country",
        "state",
        "city"
    )

    return (
        df
        .select(
            "country",
            "state",
            "city"
        )
        .distinct()
        .withColumn(
            "location_key",
            row_number().over(window)
        )
        .select(
            "location_key",
            "country",
            "state",
            "city"
        )
    )


# ==========================================================
# USER DIMENSION
# ==========================================================

def create_dim_user(df: DataFrame) -> DataFrame:

    window = Window.orderBy("user_id")

    return (
        df
        .select("user_id")
        .distinct()
        .withColumn(
            "user_key",
            row_number().over(window)
        )
        .select(
            "user_key",
            "user_id"
        )
    )


# ==========================================================
# SESSION DIMENSION
# ==========================================================

def create_dim_session(df: DataFrame) -> DataFrame:

    window = Window.orderBy("session_id")

    return (
        df
        .select("session_id")
        .distinct()
        .withColumn("session_key", row_number().over(window))
        .select(
            "session_key",
            "session_id"
        )
    )


# ==========================================================
# DATE DIMENSION
# ==========================================================

def create_dim_date(df: DataFrame) -> DataFrame:

    window = Window.orderBy("date")

    return (
        df
        .select(
            col("event_date").alias("date"),
            "event_year",
            "event_month",
            "event_day",
            "event_weekday"
        )
        .distinct()
        .withColumn("quarter", quarter("date"))
        .withColumn("week_of_year", weekofyear("date"))
        .withColumn("date_key", date_format(col("date"), "yyyyMMdd").cast("int"))
        .select(
            "date_key",
            "date",
            "event_year",
            "event_month",
            "event_day",
            "event_weekday",
            "quarter",
            "week_of_year"
        )
    )

def lookup_application_key(fact_df: DataFrame, dim_application_df: DataFrame) -> DataFrame:

    return (
        fact_df.join(
            broadcast(
                dim_application_df.select(
                    "application_key",
                    "application_id",
                    "application_version"
                )
            ),
            on=[
                "application_id",
                "application_version"
            ],
            how="left"
        )
    )

def lookup_device_key(fact_df: DataFrame, dim_device_df: DataFrame) -> DataFrame:

    return (
        fact_df.join(
            broadcast(
                dim_device_df.select(
                    "device_key",
                    "device_id"
                )
            ),
            on="device_id",
            how="left"
        )
    )

def lookup_product_key(fact_df: DataFrame, dim_product_df: DataFrame) -> DataFrame:

    return (
        fact_df.join(
            broadcast(
                dim_product_df.select(
                    "product_key",
                    "product_id"
            )
        ),
            on="product_id",
            how="left"
        )
    )

def lookup_location_key(fact_df: DataFrame, dim_location_df: DataFrame) -> DataFrame:

    return (
        fact_df.join(
            broadcast(
                dim_location_df.select(
                    "country",
                    "state",
                    "city",
                    "location_key"
                )
            ),
            on=[
                "country",
                "state",
                "city"
            ],
            how="left"
        )
    )

def lookup_user_key(fact_df: DataFrame, dim_user_df: DataFrame) -> DataFrame:

    return (
        fact_df.join(
            broadcast(
                dim_user_df.select(
                    "user_id",
                    "user_key"
                )
            ),
                on="user_id",
                how="left"
        )
    )

def lookup_session_key(fact_df: DataFrame, dim_session_df: DataFrame) -> DataFrame:

    return (
        fact_df.join(
            broadcast(
                dim_session_df.select(
                    "session_id",
                    "session_key"
                )
            ),
            on="session_id",
            how="left"
        )
    )

def lookup_date_key(fact_df: DataFrame, dim_date_df: DataFrame) -> DataFrame:

    return (
        fact_df.join(
            broadcast(
                dim_date_df.select(
                    "date_key",
                    col("date").alias("event_date")
                )
            ),
            on="event_date",
            how="left"
        )
    )



def create_fact_events(df: DataFrame) -> DataFrame:

    return (
        df
        # Remove natural keys
        .drop(
            "application_id",
            "application_version",

            "device_id",
            "device_type",
            "device_model",
            "os_version",

            "product_id",
            "product_name",
            "category",
            "brand",

            "country",
            "state",
            "city",

            "user_id",
            "session_id"
        )

        # Arrange columns
        .select(
            "event_id",
            "event_timestamp",
            "event_date",
            "date_key",
            "application_key",
            "device_key",
            "product_key",
            "location_key",
            "user_key",
            "session_key",
            "event_type",
            "event_category",
            "purchase_amount",
            "payment_success",
            "response_time_ms",
            "response_bucket",
            "batch_id",
            "ingestion_timestamp"
        )

    )