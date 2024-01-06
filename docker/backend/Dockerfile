FROM ubuntu:xenial
# FROM python:latest
# FROM ubuntu:latest

# Set DEBIAN_FRONTEND to avoid debconf frontend errors
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y build-essential \
    libssl-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libdb5.3-dev \
    libbz2-dev \
    libexpat1-dev \
    liblzma-dev \
    tk-dev \
    wget \
    curl \
    && cd /tmp \
    && wget https://www.python.org/ftp/python/3.6.15/Python-3.6.15.tgz \
    && tar -xf Python-3.6.15.tgz \
    && cd Python-3.6.15 \
    && ./configure --enable-optimizations \
    && make -j$(nproc) \
    && make install \
    && cd /tmp \
    && rm -rf Python-3.6.15* \
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
    # python3.6 python3.6-dev python3-pip

WORKDIR /app
COPY requirements.txt .
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.6 /usr/bin/python
RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.6 /usr/bin/python3

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn==19.9.0

ADD ./backend /app/backend
ADD ./docker /app/docker
ADD ./research /app/research

#RUN mkdir -p /app/backend/server/staticfiles
RUN mkdir -p /app/backend/server/static
