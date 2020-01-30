FROM python:3
ENV PYTHONNUNBEFFERED 1
RUN mkdir /code
WORKDIR /code
ADD local_requirements.txt /code/
RUN pip3 install -r local_requirements.txt
ADD . /code/


