
FROM debian:buster

RUN apt-get update \
  && apt-get install -y --no-install-recommends g++ make cmake python python-venv python-pip python-dev \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# RUN python3 -m venv /app/venv

COPY ./ ./
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /app

CMD python3 -m lpbook.server.server