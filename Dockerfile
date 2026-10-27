FROM python:3.14-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    KERAS_BACKEND=tensorflow \
    CUDA_VISIBLE_DEVICES=-1

RUN apt update \
    && apt install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip check

COPY app.py .
COPY modele/reseau.keras modele/reseau.keras
COPY modele/tfidf.joblib modele/tfidf.joblib
COPY modele/metrics.json modele/metrics.json

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]