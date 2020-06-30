FROM alpine:3.8

RUN apk add --no-cache \
    gcc musl-dev python3 python3-dev libffi-dev tzdata && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

WORKDIR /app/
COPY . /app/

ENV TZ=CST-8

RUN pip install --no-cache-dir -r ./requirements.txt

# ENTRYPOINT /bin/bash
EXPOSE 5000

ENTRYPOINT python ./manage.py run
