# logging-system

This repository is a basic distributed logging system that operates using RabbitMQ.

## Installation

```sh
python3 -m pip install -r requirements.txt
```

Create a file `.env` which defines the necessary environment variables.

- `PIKA_HOST`
- `PIKA_PORT`
- `PIKA_VIRTUAL_HOST`
- `PIKA_USERNAME`
- `PIKA_PASSWORD`
