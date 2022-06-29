# Install

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

then install git large file storage:

https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage 

and run

```bash
git lfs pull 
```

# Run

The environment variables HTTP_WEB3_URL and WS_WEB3_URL need to be set (an .env file is ok too). They should point to the http and websocket endpoint of an ethereum node, e.g.

```
HTTP_WEB3_URL=https://mainnet.infura.io/v3/{INFURA_KEY}
WS_WEB3_URL=wss://mainnet.infura.io/ws/v3/{INFURA_KEY}
```

Run the server with,

```bash
. venv/bin/activate
python -m lpbook.server.server
```

# Try it

Run

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/lps_trading_tokens' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  "0x6b175474e89094c44da98b954eedeac495271d0f",
  "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
]'
```

wait a few seconds (cache is initially empty), then rerun the above command again.

# Swagger interface

`http://127.0.0.1:8000/docs` 
