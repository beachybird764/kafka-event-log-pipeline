Write-Host "Starting Kafka cluster..."

docker compose -f docker/docker-compose.yml up -d

Write-Host "Kafka cluster started."

# run script:  .\scripts\start_kafka.ps1