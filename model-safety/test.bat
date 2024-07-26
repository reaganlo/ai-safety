@echo off
REM Use curl to send a POST request to the API endpoint
curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d "{\"model\": \"llama3\", \"prompt\": \"Why is the sky blue?\"}"

pause
