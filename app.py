from flask import Flask, jsonify, request
import logging
import random
import time

app = Flask(__name__)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/api/data")
def get_data():
    if random.random() < 0.2:
        app.logger.error("Random internal server error occurred.")
        return jsonify(error="Internal Server Error"), 500

    app.logger.info("Returning dummy data")
    return jsonify(data=[random.randint(0, 100) for _ in range(5)])

@app.route("/api/delay")
def delayed_response():
    delay = request.args.get("seconds", default=0.5, type=float)
    time.sleep(delay)
    app.logger.info(f"Responding after {delay} seconds delay.")
    return jsonify(message="Response delayed", delay=delay)

@app.route("/api/log")
def log_test():
    level = random.choice(["debug", "info", "warning", "error", "critical"])
    msg = f"Generated a {level.upper()} log"
    getattr(app.logger, level)(msg)
    return jsonify(message=msg, level=level)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
