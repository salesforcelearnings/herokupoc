FROM python:3.6-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
WORKDIR /
ENTRYPOINT ["python"]
CMD ["Salesforce.py"]



