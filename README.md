[![Build Status](https://travis-ci.com/laerteallan/challange.svg?branch=master)](https://travis-ci.com/laerteallan/challange)
[![Coverage Status](https://coveralls.io/repos/github/laerteallan/challange/badge.svg?branch=master)](https://coveralls.io/github/laerteallan/challange?branch=master)

# Test Challenge

This project was written in **Python** language using a version **3.7.2**, with the framework **Tornado**, the of default **REST**, design pattern **Factory**, **PostgreSql** to database, **Sqlalchemy Object Relational*** and was used an **object oriented programming** with a great **organization** and **traceability** of it. The **Tornado** was chosen as an **asynchronous framework** and independent. The Tornado is one the best python frameworks on the market for **performance** . 
The test has also been developed on a **docker** platform, so it is scalable horizontally with **high performance** and **portability**. The test has a in your structure the default  **python community** and is using the main static analysis tools (sonar, PEP8, PEP247, radron and etc.) that are most commonly used for quality code. This test was added **CI Travis** disponibled by **Github**, with a configuration YAML file, where **any changes of the branch master,  the tests will be running that has a 100% coverage**, giving tranquility to any future change, without fear of error. The test has logs and are displayed in the **stdout** of the machine as in the defaults for deploys in **CLOUD**.

# Install

For the local installation, you must have Python language 3.7.2 the package manager PIP and execute the following command:
```sh
pip install -r requiriments.txt # For production 
pip install -r requiriments-dev.txt # For developer 
```

Case have the docker-compose installed exeucte the command:
```sh
docker-compose up
```
This will create one container ready for use.

## Environment Variable
The test was developed to more types of environments as, Homol, Testing and Production, enough change the variable APPLICATION_ENV to the options disponible that same will be ready whatever environment. The disponible variables:
```sh
export LOG_LEVEL=INFO
export AMOUNT_PROCESS=1
export PORT_SERVER=8889
export APPLICATION_ENV=Homol
```
# Runnig Tests
Execute the following command:

```sh
make tests
```

# Execution System:

Create Database

```sh
 psql -U postgres -c 'create database challenge;'
```

It add the Environment of according with choices and execute:

```sh

python manager.py create # for create tables the of database postgree
python manager.py start # start application
```

# API


# Executions of Endpoints:

Create Payment Boleto using curl:

```sh
curl -X POST \
  http://localhost:8889/v1/api/payments/type/boleto \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 023ab60d-8de3-49e2-89e0-b07bd1126ca8' \
  -d '{"client_id": 10,
"name_buyer": "name buyer",
"email_buyer": "name@wirecard.com",
"cpf_buyer": "09170085610",
"amount": 10.989
}
'


{"status": "success", "message": {"number": "287821407897617007356961452738819332273288776689", "id": 136}}
```


```sh
curl -X POST \
  http://localhost:8889/v1/api/payments/type/card \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 023ab60d-8de3-49e2-89e0-b07bd1126ca8' \
  -d '{"client_id": 10,
"name_buyer": "Name buyer",
"email_buyer": "buyer@wirecard.com",
"cpf_buyer": "09170085610",
"amount": 10.989,
"card_name": "Laerte Allan",
"card_number": "4984423484992298",
"card_expiration_date": "0125122",
"card_cvv": "232"
}
'

{"status": "success", "message": {"card_flag": "Visa", "id": 138}}
```
For list of payments, execute curl to endpoint http://localhost:8889/v1/api/payments?value=name&amount_item=40&page=0&search_by=name&type=card. Changed type to card, boleto or remove type
for show all payments.

```sh
curl -X GET \
  'http://localhost:8889/v1/api/payments?value=lae&amount_item=40&page=0&search_by=name&type=card' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: e45bfa6b-b90f-4dfe-b062-22fff6b6ae22'
  
  {
    "status": "success",
    "message": [
        {
            "card_name": "Laerte Allan",
            "type": "Credit Card",
            "card_number": "4984423484992298",
            "card_flag": "Visa",
            "card_expiration_date": "12/20",
            "card_cvv": 232,
            "client_id": 10,
            "id": 1,
            "name_buyer": "Laerte Allan",
            "email_buyer": "laerte.allan@fs.com",
            "status": "SUCCESS",
            "cpf_buyer": "09170085617",
            "amount": "10.99"
        },
        {
            "card_name": "Laerte Allan",
            "type": "Credit Card",
            "card_number": "4984423484992298",
            "card_flag": "Visa",
            "card_expiration_date": "0125122",
            "card_cvv": 232,
            "client_id": 10,
            "id": 2,
            "name_buyer": "Laerte Allan",
            "email_buyer": "laerte.allan@fs.com",
            "status": "SUCCESS",
            "cpf_buyer": "09170085617",
            "amount": "10.99"
        }
]
  
```
