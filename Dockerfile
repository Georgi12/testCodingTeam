FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /restaurant
COPY requirements.txt /restaurant/
RUN pip install -r requirements.txt
COPY . /restaurant/