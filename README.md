[![Build Status](https://travis-ci.com/laerteallan/challange.svg?branch=master)](https://travis-ci.com/laerteallan/challange)
# Test Challenge
Esse projeto foi escrito na linguagem **Python** usando a versão **3.7.2**, com o principal framework o **Tornado**, **REST**, e usado a **programação orientada a objetos**, tendo uma otima **organização** e **rastreabilidade** do mesmo. O **Tornado** foi escolhido por ser um framework **assíncrono** e independente para o uso e ser um dos melhores frameworks python do mercado  para **perfomance** desde que saiba realmente do que está fazendo. Também foi desenvolvido sobre a platarforma de **docker**, dessa forma ele é escalável horizontamente dando maior **performance** e **portabilidade**. O teste tem toda a estrutura da **comunidade python** usando as principais ferramentas de análise estática de mercado (sonnarqube, PEP8, PEP247, radon e etc..) que são mais utilizadas para dar maior qualidade ao código. Foi adicionado nesse teste **CI** diponibilizado pelo **GITLAB**, com uma configuração do arquivo YAML, onde **qualquer ateração commitada para a branch master, o mesmo começará a rodar os testes unitários* que possui uma cobertura de 100%**, dando tranquilidade para qualquer futura alteração, sem ter medo errar. O teste possui logs e são mostrado no **stdout** da máquina estando nos padrões para deploys em **CLOUD**.


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


