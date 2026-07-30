Write-Host "Available Kafka Topics:"

docker exec kafka `
    /opt/kafka/bin/kafka-topics.sh `
    --list `
    --bootstrap-server localhost:9092

# run: .\scripts\list_topics.ps1