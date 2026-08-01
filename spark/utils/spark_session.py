import os
import sys
from pyspark.sql import SparkSession

from configs.spark_config import MASTER, APP_NAME, SHUFFLE_PARTITIONS, AQE_ENABLED

JAVA_HOME = r"C:\Users\HP\.jdks\ms-17.0.19"
HADOOP_HOME = r"C:\Users\HP\IdeaProjects\event-log-pipeline\hadoop"

python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ["JAVA_HOME"] = JAVA_HOME
os.environ["HADOOP_HOME"] = HADOOP_HOME
os.environ["PATH"] = (
        JAVA_HOME + r"\bin;" +
        HADOOP_HOME + r"\bin;" +
        os.environ["PATH"]
)

def create_spark_session() -> SparkSession:
    builder = (
        SparkSession.builder
        .appName(APP_NAME)
        .master(MASTER)

        # Delta
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

        # Kafka package
        .config("spark.jars.packages",
            ",".join([
                "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.6",
                "io.delta:delta-spark_2.12:3.3.2"
            ])
        )

        # Performance
        .config("spark.sql.shuffle.partitions", SHUFFLE_PARTITIONS)
        .config("spark.sql.adaptive.enabled", AQE_ENABLED)
    )

    spark = builder.getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    return spark