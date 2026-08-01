from pyspark.sql.types import *

EVENT_SCHEMA = StructType([

    StructField("event_id", StringType(), False),
    StructField("event_timestamp", TimestampType(), False),

    StructField("application_id", StringType(), False),
    StructField("application_version", StringType(), False),

    StructField("device_id", StringType(), False),
    StructField("device_type", StringType(), False),
    StructField("device_model", StringType(), False),
    StructField("os_version", StringType(), False),

    StructField("user_id", StringType(), False),
    StructField("session_id", StringType(), False),

    StructField("event_type", StringType(), False),
    StructField("screen_name", StringType(), False),

    StructField("product_id", StringType(), True),
    StructField("product_name", StringType(), True),
    StructField("category", StringType(), True),
    StructField("brand", StringType(), True),

    StructField("price", DoubleType(), True),
    StructField("quantity", IntegerType(), True),

    StructField("payment_status", StringType(), True),

    StructField("country", StringType(), False),
    StructField("state", StringType(), False),
    StructField("city", StringType(), False),

    StructField("ip_address", StringType(), False),

    StructField("network_type", StringType(), False),
    StructField("browser", StringType(), True),

    StructField("response_time_ms", IntegerType(), False),

    StructField("status", StringType(), False),

    StructField("error_code", StringType(), True),
    StructField("error_message", StringType(), True),

    StructField("ingestion_source", StringType(), False),

    StructField("schema_version", StringType(), False)
])