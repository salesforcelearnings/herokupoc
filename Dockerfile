FROM python:3.6-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn gevent
COPY . /app
WORKDIR /app
CMD  ["gunicorn","gettingstarted.wsqi"]
CMD  ["Python","Salesforce.py"]



