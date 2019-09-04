FROM alpine:latest

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.4/main" >> /etc/apk/repositories && \
	echo "http://dl-4.alpinelinux.org/alpine/v3.4/community" >> /etc/apk/repositories

RUN apk update && \
	apk add --no-cache chromium chromium-chromedriver

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel 

ADD . /

RUN pip3 install -r requirements.txt

CMD [ "python3", "-u", "./app.py" ]
