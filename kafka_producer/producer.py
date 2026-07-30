import json
import time

from kafka import KafkaProducer
from kafka.errors import KafkaError

from configs.kafka_config import (
    BOOTSTRAP_SERVERS,
    TOPIC_NAME,
    ACKS,
    RETRIES,
    LINGER_MS,
    BATCH_SIZE
)

from configs.logging_config import get_logger

from kafka_producer.event_generator import generate_event

logger = get_logger(__name__)


def create_kafka_producer():

    return KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        client_id="event-log-producer",
        acks=ACKS,
        retries=RETRIES,
        linger_ms=LINGER_MS,
        batch_size=BATCH_SIZE,
        value_serializer=lambda value: json.dumps(value).encode("utf-8")
    )

def main():

    logger.info("Kafka Producer Started")

    producer = None

    try:
        producer = create_kafka_producer()
        logger.info("Connected to Kafka Broker")

        while True:

            event = generate_event()

            future = producer.send(
                TOPIC_NAME,
                value=event.to_dict()
            )

            metadata = future.get(timeout=10)

            logger.info(
                "Produced Event | event_id=%s | application=%s | event_type=%s | Topic=%s | partition=%d | offset=%d",
                event.event_id,
                event.application_id,
                event.event_type,
                "event_logs",
                metadata.partition,
                metadata.offset,
            )

            time.sleep(1)

    except KafkaError as e:
        logger.exception(f"Kafka Error: {e}")

    except Exception as e:
        logger.exception(e)

    except KeyboardInterrupt:
        logger.info("Stopping Kafka Producer...")

    finally:

        if producer is not None:
            producer.flush()
            producer.close()

        logger.info("Kafka Producer Stopped")

if __name__ == "__main__":
    main()