# otus-prometheus
1. Запуск окружения:
source venv/bin/activate
2. Запуск Prometheus:
docker run -d -p 9090:9090 -v /<full_path>/otus-prometheus/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
3. Запуск приложения
python flask_app/app.py

Метрики доступны по адресу http://localhost:5000/metrics
