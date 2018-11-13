FROM python:3.6

RUN pip install flask
COPY code /code

WORKDIR /code

ENTRYPOINT ["python", "run.py"]
