FROM python:3

ENV PYTHONNUNBUFFERED 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
# Run the pip install command
RUN pip install -r requirements.txt 

COPY . /code/