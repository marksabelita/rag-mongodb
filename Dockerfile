FROM python:3-slim-buster

RUN mkdir /app

WORKDIR /app


COPY requirements.txt .

RUN python3 -m venv venv
RUN . ./venv/bin/activate
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]
