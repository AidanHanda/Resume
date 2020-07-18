FROM python:3-alpine as code

RUN apk add --no-cache texlive-full

WORKDIR /resme/temp
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app/
COPY ./src ./src
COPY ./templates ./templates

USER root

ENTRYPOINT ["/bin/ash"]
#ENTRYPOINT ["python","src/resme.py"]

