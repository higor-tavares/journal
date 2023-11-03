# Simple flask rest application crud
This is a sample prof of concept from a rest api using python and flask with in memory crud operations

## Requirements
* Python3
* Pip3
* Make

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