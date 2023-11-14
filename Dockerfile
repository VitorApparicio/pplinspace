FROM alpine
ENTRYPOINT /usr/bin/python /tmp/pplinspace.py
COPY pplinspace.py /tmp
COPY requirements.txt /tmp
RUN chmod 777 /tmp/pplinspace.py
RUN apk add py3-pip
RUN pip install -r /tmp/requirements.txt