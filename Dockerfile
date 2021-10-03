FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip

RUN pip install flask

COPY app.py /opt/

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
