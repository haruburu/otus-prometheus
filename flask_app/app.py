#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return 'Hello, OTUS!'

if __name__ == '__main__':
    app.run()