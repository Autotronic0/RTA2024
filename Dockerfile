
FROM python:3.11-slim-buster as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY perceptron_model.pkl .

FROM python:3.11-slim-buster

WORKDIR /app

COPY --from=builder /app .

COPY app.py .

ENV FLASK_APP=app

EXPOSE 8000

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
