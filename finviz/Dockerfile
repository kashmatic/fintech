FROM python:3.6-alpine

RUN apk update && apk upgrade && apk add git gcc libxslt libxml2 libxml2-dev libxslt-dev musl-dev
RUN git clone https://github.com/kashmatic/Finance-Data-Scraper-API.git

WORKDIR /Finance-Data-Scraper-API

RUN python setup.py install

# ENTRYPOINT ["python", "finance_data_scraper/webserver.py"]
