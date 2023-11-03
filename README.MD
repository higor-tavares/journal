# Simple flask rest application crud
This is a sample prof of concept from a rest api using python and flask with in memory crud operations

## Requirements

* Python3
* Pip3
* Make
* Docker and Docker-Compose
* AWS Cli

## Running this application
First, configure your virtual enviroment with the command bellow
`make configure`
and then install all the requirements with the command `make install`
finaly run the application with `make run`.
access http://localhost:5000 and see an empty journal
## Adding the first journal entry
run the command bellow to create a simple journal
```
curl -X POST http://localhost:5000/salary \
 -H "Content-Type:application/json" \
-d '{ "description":"Salary", "type":"CREDIT", "amount":264200 }'
```
## Create Journal table
run `docker-compose up -d` to create the local DynamoDB database
then run the command `python3 database/create_journal_table.py` to create the table journal.
then see the table list with the command `aws dynamodb --endpoint-url http://localhost:8000 list-tables`

## Project Status

In progress