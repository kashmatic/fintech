FROM python:3.6-alpine

RUN apk update && apk upgrade && apk add git gcc libxslt libxml2 libxml2-dev libxslt-dev musl-dev
# RUN git clone -b master https://github.com/kashmatic/stockmarket.git

COPY code /code

WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "005_database.py", "-t", "iex"]
