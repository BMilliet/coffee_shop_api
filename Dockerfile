FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip --no-cache-dir install -r requirements.txt

RUN apk --no-cache add libpq

COPY . /app
CMD ["python", "run.py"]
