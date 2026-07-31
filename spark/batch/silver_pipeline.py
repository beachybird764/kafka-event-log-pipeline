from configs.storage_config import SILVER_PATH
from spark.streaming.spark_session import create_spark_session
from spark.batch.bronze_reader import read_bronze, write_silver
from spark.batch.silver_transformations import apply_silver_transformations

def main():

    spark = create_spark_session()

    bronze_df = read_bronze(spark)
    silver_df = apply_silver_transformations(bronze_df)

    print(f"Bronze Rows : {bronze_df.count()}")
    print(f"Silver Rows : {silver_df.count()}")

    write_silver(silver_df)

    df = (
        spark.read
        .format("delta")
        .load(SILVER_PATH)
    )

    df.printSchema()
    df.show(10, truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()