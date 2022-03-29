
FROM debian:bullseye

RUN apt-get update \
  && apt-get install -y --no-install-recommends g++ make cmake python3 python3-pip python3-dev python3-setuptools git-lfs \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy python sources.
COPY ./ ./

# Instance dependencies.
RUN pip3 install --no-cache-dir -r requirements.txt

# Load initial trade db from git LFS (https://git-lfs.github.com/).
RUN git lfs pull -I lpbook/cost/traded_data.pickled

# Start server.
CMD python3 -m lpbook.server.server