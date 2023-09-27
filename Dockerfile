FROM --platform=linux/amd64 python:3.6-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn gevent
COPY . .
CMD  ["gunicorn","gettingstarted.wsqi"]
CMD ["python","Salesforce.py"]



