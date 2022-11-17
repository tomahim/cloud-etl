# cloud-etl

Toy project to experiment mainly with lambda on AWS using both Zappa and AWS Chalice as frameworks.
Integration with Terraform is also in the scope of the project.

## How it works

#### /infrastructure

It contains a simple DynamoDB to experiment communicating to a database from a lambda.

It can be setup with terraform: `terraform apply`

#### /chalice-functions 

It contains very simple examples of lambdas deployable with AWS Chalice (endpoint and scheduled function).

Just run `chalice deploy` and you are good to go

#### /zappa-functions


It contains a very simple example of scheduled function with Zappa. It can be further extended with endpoints provided by a Django app for example.

Just run `zappa deploy dev` 


## Show logs of a lambda 


From Cloudwatch (the lambda needs to have policies to write on CloudWatch)

aws logs tail /aws/lambda/etl-functions-dev --follow


## How to make Serverless/Zappa and Terraform live together with outputs


https://medium.com/johnveldboom/deploy-terraform-serverless-framework-in-perfect-harmony-948ab6dcbc78


## How to unit test an AWS lambda


https://medium.com/@pekelny/how-to-unit-test-an-aws-lambda-524069d4fe06


## Invoke a lambda locally


https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-lambda.html


## Invoke Django manage command on a lambda with Zappa

https://oreilly.com/library/view/building-serverless-python/9781788837613/61e3689d-3ebe-4285-a45c-9c272d5ff460.xhtml


## Lambda monitoring

#### With CloudWatch like any other services, possibility to define alerts (errors, number of invocations etc.).

https://docs.aws.amazon.com/lambda/latest/operatorguide/monitoring-observability.html
https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html

#### Also Datadog

https://www.datadoghq.com/dg/monitor/lambda/?utm_source=advertisement&utm_medium=search&utm_campaign=dg-google-infra-emea-lambda&utm_keyword=monitor%20aws%20lambda&utm_matchtype=p&utm_campaignid=15832880531&utm_adgroupid=134218764878&gclid=Cj0KCQiA1NebBhDDARIsAANiDD2bjU--D1b_iNoffL5NSKU41QRk3dy_yihUe1gKRmFe8sLd1EDXuvEaAggpEALw_wcB


#### Monitor cost of a lambda


Since cost per function is not available under billing, the best way would be to monitor the Invocation and Duration metrics for that specific Lambda function as you can Sum these and capture the total invocations and durations for period of time.


#### Pause a lambda


Need to disable the rule triggering the lambda, in case of an event in EventBridge


List the rules : `aws events list-rules`

Disable the rule : `aws events disable-rule --name zappa-functions-dev-app.lambda_fn`


It would be possible to monitor too which rule is enabled/disabled at anytime.


## What to do next : Things to learn in Django

- [ ] Use the ORM and the migrations
- [ ] Add manage commands
- [ ] View system
- [ ] Graphql and REST Api with Django
- [ ] Use of a validator with Django (Marshmallow ?)
- [ ] How to do async tasks with Django ? (Celery ?)
- [ ] Use Zappa to deploy REST endpoint in lambdas
- [ ] Toy project: Zappa + Django + Terraform (database, redis, async tasks etc.) ?

