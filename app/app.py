import os
import socket
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "dev")


@app.get("/")
def index():
    return jsonify(
        message="Hello from the CI/CD demo service",
        version=VERSION,
        host=socket.gethostname(),
    )


@app.get("/health")
def health():
    return jsonify(status="ok", time=datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
