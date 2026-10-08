FROM python:3.11-slim

WORKDIR /app

COPY log_analyzer.py /app

CMD ["python3", "log_analyzer.py"]
