FROM python:3.12-alpine
LABEL authors="ZKWolf"
LABEL description="Sinking Yacht Adguard Converter API"
ENV TZ="Europe/Vienna" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

WORKDIR /app

COPY requirements.txt /app/

RUN apk add --no-cache curl
RUN apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk del .build-deps

COPY app /app
EXPOSE 5000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1