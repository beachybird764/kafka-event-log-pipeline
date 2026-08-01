Write-Host "Starting Kafka Console Consumer..."

docker exec -it kafka `
    /opt/kafka/bin/kafka-console-consumer.sh `
    --bootstrap-server localhost:9092 `
    --topic event_logs `
    --group event-log-consumer `
    --formatter org.apache.kafka.tools.consumer.DefaultMessageFormatter `
    --formatter-property print.timestamp=true `
    --formatter-property print.offset=true `
    --formatter-property print.key=true `
    --formatter-property print.value=true