# Simple Flask Reste Aplication CRUD
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
access http://localhost:5000/products and see an empty product list
## Adding the first product
run the command bellow to create a simple product with a name and a price in cents
`curl -X POST http://localhost:5000/products/myProductName -d '{"price":8990}'`