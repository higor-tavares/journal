# Simple Flask REST Application CRUD
This project is a proof of concept for a REST API built with Python, Flask, and DynamoDB to perform CRUD operations

## Prerequisites
Ensure you have the following installed on your local machine:

* Python3
* Pip3
* Make
* Docker and Docker-Compose
* AWS CLI

## Getting Started
To set up a local development environment:

Configure your virtual environment by running the command: `make configure`
Install all the necessary dependencies with: `make install`
Start the application with: `make run`
You can now access the application at http://localhost:5000?username=your_user. Initially, you will see an empty journal.

## Database Configuration
To set up the local instance of DynamoDB:

Run `docker-compose up -d`. This starts the database running on port 8000.
Create the journal table by running the following command:

```bash
aws dynamodb --endpoint-url http://localhost:8000 create-table --table-name journal \
--attribute-definitions '[{"AttributeName":"username", "AttributeType":"S"}, {"AttributeName":"id", "AttributeType":"S"}]' \
--key-schema '[{"AttributeName":"username", "KeyType":"HASH"}, {"AttributeName":"id", "KeyType":"RANGE"}]' \
--provisioned-throughput '{"ReadCapacityUnits":5,"WriteCapacityUnits":5}'
```

## Usage

### Adding a Journal Entry
To create a new journal entry, run the following command:
```bash
curl -X POST http://localhost:5000/ \
 -H "Content-Type:application/json" \
-d '{ "username":"your_user", "description":"Salary", "type":"CREDIT", "amount":264200 }'
```
### Deleting a Journal Entry
To delete a journal entry, use the id from the list of entries and run the following command:
`curl -X DELETE 'http://localhost:5000?username=your_user&id=id_from_line_you_want_delete'`
