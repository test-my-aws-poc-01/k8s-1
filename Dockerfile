FROM python:3.7-alpine

WORKDIR /service

RUN apk update && \
    apk add python3-dev libffi-dev openssl-dev gcc libc-dev make && \
    apk add bash less vim

COPY requirements.txt /service
RUN pip install --upgrade setuptools pip pip-tools && \
    pip install -r requirements.txt

COPY app /service/app
COPY manage.py /service
COPY setup.py /service

ENV FLASK_APP=manage.py
EXPOSE 8080
CMD gunicorn --reload -b :8080 -w 1 manage:app --log-level info --access-logfile - --error-logfile -
