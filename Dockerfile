FROM --platform=linux/amd64 python:latest
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install pendulum
RUN pip install gunicorn gevent
COPY . .
CMD  ["gunicorn","gettingstarted.wsqi"]
CMD ["python","Salesforce.py"]



