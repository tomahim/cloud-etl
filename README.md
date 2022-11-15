# cloud-etl


## TODO

- [X] Setup a dynamoDB with terraform
- [X] Setup ORM to persist data to dynamoDB
- [X] Check unicity in DynamoDB before insert
- [ ] Chalice: Schedule one function with CRON to retrieve some data frequently
- [ ] Zappa: Schedule one function with CRON to retrieve some data frequently (no django, flask)
- [ ] How to unit test a lambda function ?
- [ ] Check ways to monitor lambda (performance, cost, fails, successful executions etc.)
- [ ] Monitoring alerts when a lambda is not working anymore
- [ ] Can we pause temporarly a lambda easily ?

## Show log lambda 

aws logs tail /aws/lambda/etl-functions-dev --follow