Write-Host "Stopping Kafka cluster..."

docker compose -f docker/docker-compose.yml down

Write-Host "Kafka cluster stopped."

# run script:  .\scripts\stop_kafka.ps1