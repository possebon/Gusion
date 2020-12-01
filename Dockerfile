FROM python:3.7.9-slim

LABEL maintainer="Fernando Possebon jose.possebon@edu.pucrs.br"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TIMEZONE            America/Sao_Paulo

# Change the timezone

RUN mkdir /app
COPY . /app
COPY ./images /app/images
COPY ./system /app/system

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN [ "python", "-c", "import nltk; nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger')" ]

ENTRYPOINT ["tail", "-f", "/dev/null"]