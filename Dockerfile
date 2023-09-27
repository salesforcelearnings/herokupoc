FROM --platform=linux/amd64 python:latest
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn gevent
COPY . .
WORKDIR /
CMD  ["gunicorn","gettingstarted.wsqi"]



