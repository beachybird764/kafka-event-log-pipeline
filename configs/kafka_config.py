# Kafka Broker Configuration
BOOTSTRAP_SERVERS = "localhost:9092"

# Topic Configuration
TOPIC_NAME = "event_logs"

# Topic Properties
PARTITIONS = 3
REPLICATION_FACTOR = 1

# Producer Configuration
ACKS = "all"
RETRIES = 5
LINGER_MS = 5
BATCH_SIZE = 16384

LANDING_PATH = "data/landing/event_logs"
BRONZE_PATH = "data/bronze/event_logs"

LANDING_CHECKPOINT = "data/checkpoints/landing"
BRONZE_CHECKPOINT = "data/checkpoints/bronze"

# Now, every python module in the project will import these values instead of hardcoding them.
# python module (producer, Spark, consumer, Airflow)