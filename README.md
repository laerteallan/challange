[![Build Status](https://travis-ci.com/laerteallan/challange.svg?branch=master)](https://travis-ci.com/laerteallan/challange)
# Teste Challenge
Esse projeto foi escrito na linguagem **Python** usando a versão **3.7.2**, com o principal framework o **Tornado**, **REST**, e usado a **programação orientada a objetos**, tendo uma otima **organização** e **rastreabilidade** do mesmo. O **Tornado** foi escolhido por ser um framework **assíncrono** e independente para o uso e ser um dos melhores frameworks python do mercado  para **perfomance** desde que saiba realmente do que está fazendo. Também foi desenvolvido sobre a platarforma de **docker**, dessa forma ele é escalável horizontamente dando maior **performance** e **portabilidade**. O teste tem toda a estrutura da **comunidade python** usando as principais ferramentas de análise estática de mercado (sonnarqube, PEP8, PEP247, radon e etc..) que são mais utilizadas para dar maior qualidade ao código. Foi adicionado nesse teste **CI** diponibilizado pelo **GITLAB**, com uma configuração do arquivo YAML, onde **qualquer ateração commitada para a branch master, o mesmo começará a rodar os testes unitários* que possui uma cobertura de 100%**, dando tranquilidade para qualquer futura alteração, sem ter medo errar. O teste possui logs e são mostrado no **stdout** da máquina estando nos padrões para deploys em **CLOUD**.


# Instalação
Para a instalação local do teste deverá ter o python 3.7.2 e o gerenciador PIP ou uma versão mais próxima desta e rodar o seguinte comando.
```sh
pip install -r requiriments.txt para produção ou
pip install -r requiriments-dev.txt para desenvolvimento.
```
Caso possua o docker-compose instalado basta executar
```sh
docker-compose up
```
que o mesmo criarar um container pronto para uso.

## Variáveis de ambiente
O teste foi desenvolvido para vários tipos de ambientes como, homologação (Homol), teste(Testing) e produção (Production), basta alterar a váriavel APPLICATION_ENV para uma das opções disponiveis que o mesmo estará preparado para qualquer ambiente. As variaveis de ambientes disponiveis são.
```sh
export LOG_LEVEL=INFO
export AMOUNT_PROCESS=1
export PORT_SERVER=8889
export APPLICATION_ENV=Homol
export URL_S3_ZAP="http://grupozap-code-challenge.s3-website-us-east-1.amazonaws.com/sources/source-2.json"
```
# Rodar os testes
Basta executar os seguintes comando

```sh
make tests
```

# Execução do sistema:
adicionar as váriaveis de ambiente de acordo a escolha e executar:
```sh
python manager.py start
```

# API

Foi disponibilizada 2 endpoints um de healthcheck e outro para a pesquisa.
O que diferencia o zap do viva real é a opção **partner** onde os existentes são **zap** para "Zap Imóveis" e **viva** para  "Vivareal". Lembrando que é obrigatório passar o numero da págian coforme abaixo.
Nessa api de pesquisa foi disponibilizado um campo a mais de número de páginas (**Pois eu achei interessante ter.**) e temos 40 items por página.

```sh
http://localhost:8889/v1/api?partner=zap&pageNumber=100
http://localhost:8889/healthcheck
```

# Execução dos Endpoints


```sh
curl -X GET http://localhost:8889/healthcheck
{"status": "success", "message": {"status": "ok"}}
 
curl -X GET 'http://localhost:8889/v1/api?partner=zap&pageNumber=100'
 
```
