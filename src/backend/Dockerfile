FROM python:3.9.2-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "Server.py"]