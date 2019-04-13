[![Build Status](https://travis-ci.com/laerteallan/challange.svg?branch=master)](https://travis-ci.com/laerteallan/challange)
[![Coverage Status](https://coveralls.io/repos/github/laerteallan/challange/badge.svg?branch=master)](https://coveralls.io/github/laerteallan/challange?branch=master)
# Test Challenge
This project was written in **Python** language using a version **3.7.2**, with the framework of the **Tornado**, **REST**, and was used an **object oriented programming** with a great **organization** and **traceability** of it. The **Tornado** was chosen as an **asynchronous framework** and independent. The Tornado is one the best python frameworks on the market for **performance** . 
The test has also been developed on a **docker** platform, so it is scalable horizontally with **high performance** and **portability**. The test has a **python community** structure and using the main static analysis tools (sonar, PEP8, PEP247, radron and etc.) that are most commonly used for quality code. This test was added **CI Travis** disponibled by **Github**, with a configuration YAML file, where **any changes of the branch master,  the tests will be running that has a 100% coverage**, giving tranquility to any future change, without fear of error. The test has logs and are displayed in the **stdout** of the machine as in the defaults for deploys in **CLOUD**.

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

It add the Environment of according with choices and execute:

```sh
python manager.py start
```

# API


# Executions of Endpoints:


