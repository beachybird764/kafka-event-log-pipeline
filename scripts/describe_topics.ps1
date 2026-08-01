Write-Host "Topic Details: event_logs"

docker exec kafka `
    /opt/kafka/bin/kafka-topics.sh `
    --describe `
    --topic event_logs `
    --bootstrap-server localhost:9092

# run: .\scripts\describe_topics.ps1