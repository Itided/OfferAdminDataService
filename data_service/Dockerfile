FROM python:3.12-alpine

RUN adduser --disabled-password --gecos '' DataServiceUser

WORKDIR /opt/

COPY ./data_service/requirements.txt .
COPY ./data_service/app ./app

RUN chown -R DataServiceUser:DataServiceUser .
USER DataServiceUser
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



USER DataServiceUser

EXPOSE 5000
