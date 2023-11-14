FROM alpine
ENTRYPOINT /usr/bin/python /tmp/spacemenu.py
COPY spacemenu.py /tmp
COPY functions.py /tmp
COPY requirements.txt /tmp
RUN chmod 777 /tmp/spacemenu.py
RUN apk add py3-pip
RUN pip install -r /tmp/requirements.txt