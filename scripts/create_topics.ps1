Write-Host "Creating Kafka topic: event_logs..."

docker exec kafka `
/opt/kafka/bin/kafka-topics.sh `
    --create `
    --topic event_logs `
    --bootstrap-server localhost:9092 `
    --partitions 3 `
    --replication-factor 1

Write-Host "Topic creation completed."

# run:  .\scripts\create_topics.ps1