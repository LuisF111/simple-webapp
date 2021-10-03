FROM python:3.6

RUN pip install flask

COPY app.py /opt/

CMD [ "python", "/opt/app.py" ]
