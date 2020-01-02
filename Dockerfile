FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt /app

RUN apk update && \
    apk --no-cache add postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libpq

RUN pip --no-cache-dir install -r requirements.txt

COPY . /app
CMD ["python", "run.py"]
