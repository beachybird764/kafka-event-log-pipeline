from datetime import datetime
from pyspark.sql import Row
from spark.audit.audit_writer import write_audit
from spark.audit.audit_schema import AUDIT_SCHEMA

def log_pipeline_run(
        spark,
        pipeline_name,
        layer,
        batch_id,
        status,
        start_time,
        end_time,
        input_rows,
        output_rows,
        error_message=None
):

    audit_df = spark.createDataFrame(
        [
            (
                pipeline_name,
                layer,
                batch_id,
                status,
                start_time,
                end_time,
                input_rows,
                output_rows,
                error_message
            )
        ],
        schema=AUDIT_SCHEMA
    )

    audit_df.printSchema()
    audit_df.show(truncate=False)

    write_audit(audit_df)