#FROM --platform=linux/amd64 python:latest
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#RUN pip install gunicorn gevent
#COPY . .
#CMD  ["gunicorn","gettingstarted.wsqi"]
#CMD ["python","Salesforce.py"]
FROM python:3.11-slim-bullseye as databuilder
WORKDIR /SalesforceCnnect
COPY requirements.txt .
RUN apt-get update && apt-get -y install gcc patchelf scons
RUN pip install gunicorn gevent
RUN pip install -r requirements.txt

