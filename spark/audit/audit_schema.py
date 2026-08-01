from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    TimestampType
)

AUDIT_SCHEMA = StructType([
    StructField("pipeline_name", StringType(), False),
    StructField("layer", StringType(), False),
    StructField("batch_id", IntegerType(), True),
    StructField("status", StringType(), False),
    StructField("start_time", TimestampType(), False),
    StructField("end_time", TimestampType(), False),
    StructField("input_rows", IntegerType(), False),
    StructField("output_rows", IntegerType(), False),
    StructField("error_message", StringType(), True)
])