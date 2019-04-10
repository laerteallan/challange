FROM python:3.7.2-alpine
RUN  apk add --no-cache --update bash libxslt libxslt-dev libffi-dev linux-headers alpine-sdk build-base gcc postgresql-dev bash
ARG DEPLOY_PATH='/home/deploy/challenge'
RUN mkdir -p $DEPLOY_PATH

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

COPY requirements.txt $DEPLOY_PATH/requirements.txt
COPY manager.py $DEPLOY_PATH/manager.py
COPY challenge $DEPLOY_PATH/challenge
RUN pip install -r $DEPLOY_PATH/requirements.txt
WORKDIR $DEPLOY_PATH
CMD ["python", "manager.py", "start"]