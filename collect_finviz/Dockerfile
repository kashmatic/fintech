FROM python:3.6-alpine

RUN apk update && apk upgrade && apk add git gcc libxslt libxml2 libxml2-dev libxslt-dev musl-dev
RUN git clone -b master https://github.com/kashmatic/stockmarket.git

WORKDIR /stockmarket

RUN cat requirements.txt
RUN pip install -r requirements.txt

WORKDIR /stockmarket/stockprice

EXPOSE 5000

ENTRYPOINT ["python", "005_database.py", "-t", "finviz"]
