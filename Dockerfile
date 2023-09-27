FROM python:3.6-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn gevent
COPY . .
WORKDIR /
CMD  ["gunicorn","gettingstarted.wsqi"]
CMD ["python","Salesforce.py"]



