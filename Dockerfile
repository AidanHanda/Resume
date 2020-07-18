FROM python:3

USER root

#RUN apt-get update && apt-get install -y texlive-latex-recommended

WORKDIR /resme/temp
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app/
COPY ./src ./src
COPY ./templates ./templates

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["python","src/resme.py"]

