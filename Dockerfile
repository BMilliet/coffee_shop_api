FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN apt update \
	&& apt install gcc -y \
	&& pip --no-cache-dir install -r requirements.txt

COPY . /app
CMD ["python", "app.py"]
