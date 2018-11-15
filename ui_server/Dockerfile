FROM python:3.6-alpine

RUN apk update && apk upgrade && apk add git gcc libxslt libxml2 libxml2-dev libxslt-dev musl-dev

COPY code /code

WORKDIR /code

RUN cat requirements.txt
RUN pip install -r requirements.txt

# WORKDIR /stockmarket/website

ENTRYPOINT ["python", "run.py"]
