
## Test server
```shell script
curl -H "Content-Type: text/plain" --data  "This is sentence" http://0.0.0.0:5432/status
# json request
curl -d '{"sentence":"التعلم الرقمي من خلال التسجيل الرقمي افتتاح الموقع قري"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5432/analyse
```