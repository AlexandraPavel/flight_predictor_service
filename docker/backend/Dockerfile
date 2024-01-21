FROM alpine:3.16.0

WORKDIR /app

RUN set -xe;

COPY . .
# --no-cache
RUN apk add python3 py3-pip tini; \
    pip install --upgrade pip3 setuptools-scm; \
    apk add build-base python3-dev libffi-dev openssl-dev zlib-dev libgcc gfortran; \
    apk add bash; \
    apk add py3-scikit-learn;
    # addgroup -g 1000 appuser; \
    # adduser -u 1000 -G appuser -D -h /app appuser; \
    # chown -R appuser:appuser /app

COPY requirements.txt requirements.txt
RUN pip3 install  -r requirements.txt
RUN pip3 install scikit-learn
# --no-cache-dir

ADD ./backend /app/backend
ADD ./docker /app/docker
ADD ./research /app/research

#RUN mkdir -p /app/backend/server/staticfiles
RUN mkdir -p /app/backend/server/static
