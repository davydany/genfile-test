FROM python:3.8

WORKDIR /code

COPY . /code

VOLUME /output

RUN pip install -r requirements.txt

CMD python genfile.py