# Build the C sieve (option 2) in a separate stage so gcc stays out of the final image
FROM python:3.13-slim AS c-build
RUN apt-get update && apt-get install -y --no-install-recommends gcc libc6-dev \
    && rm -rf /var/lib/apt/lists/*
COPY amicable_pairs/amicable.c .
RUN gcc -O2 -shared -fPIC amicable.c -o libamicable.so

FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY --from=c-build /libamicable.so amicable_pairs/libamicable.so
RUN python manage.py collectstatic --noinput

RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

CMD ["sh", "-c", "exec gunicorn amicable_numbers.wsgi:application --bind 0.0.0.0:${PORT} --workers 2 --timeout 120"]
