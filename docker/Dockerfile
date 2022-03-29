
FROM ubuntu:latest

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update \
  && apt-get install -y --no-install-recommends g++ make cmake python3.10 python3.10-venv python3.10-pip python3.10-dev \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# RUN python3 -m venv /app/venv

COPY ./ ./
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /app

CMD python3 -m lpbook.server.server