# Install

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# Run

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
