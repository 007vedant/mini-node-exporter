import os
import time
from flask import Flask
from urllib.parse import urlparse
from flask import jsonify, request
from prometheus_client import Gauge, generate_latest, REGISTRY, PROCESS_COLLECTOR, PLATFORM_COLLECTOR

# mini-node-exporter

app = Flask(__name__)

start = time.time()

load_metric = Gauge('node_load', 'Load Avg', ['duration'])  # metric for load avg with 'duration' label
uptime_metric = Gauge('node_uptime', 'Node Uptime') # metric for uptime


@app.route("/")
def home():
    return jsonify("Mini Exporter Node")

@app.route("/info")
def info():
    return jsonify("Task for Project Chaos Mesh - LFX Mentorship")

@app.route("/info/load")
def load():
    load1, load5, load15 = os.getloadavg()  # calculating load avg metric
    load_metric.labels(duration="1m").set(load1)
    load_metric.labels(duration="5m").set(load5)
    load_metric.labels(duration="15m").set(load15)

    return jsonify({"1m": load1, "5m": load5, "15m": load15})

@app.route("/info/hostname")
def hostname():
    hostinfo = urlparse(request.base_url)
    return jsonify(hostinfo.hostname)

@app.route("/info/uptime")
def uptime():
    now = time.time()
    uptime = now - start    # calculating uptime metric
    uptime_metric.set(uptime)
    return jsonify(str(uptime))

@app.route("/metrics")
def metrics():
    return generate_latest() # collecting metrics and exposing to /metrics endpoint
    

if __name__ == '__main__':
    app.run('0.0.0.0', port=23333)
