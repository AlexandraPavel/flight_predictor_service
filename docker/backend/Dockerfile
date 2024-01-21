FROM alpine:3.16.0

WORKDIR /app

RUN set -xe;

COPY . .
# --no-cache
RUN apk add python3 py3-pip tini; \
    pip install --upgrade pip setuptools-scm; \
    apk add build-base python3-dev libffi-dev openssl-dev zlib-dev libgcc; \
    apk add bash; \
    addgroup -g 1000 appuser; \
    adduser -u 1000 -G appuser -D -h /app appuser; \
    chown -R appuser:appuser /app

COPY requirements.txt requirements.txt
RUN pip install  -r requirements.txt
# --no-cache-dir

ADD ./backend /app/backend
ADD ./docker /app/docker
ADD ./research /app/research

#RUN mkdir -p /app/backend/server/staticfiles
RUN mkdir -p /app/backend/server/static
