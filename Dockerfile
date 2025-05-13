FROM python:3.12

WORKDIR /app

RUN apt-get update \
 && apt-get install -y gcc libpq-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install celery gunicorn
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY="django-insecure-qw&5xfnqmd&79qhcq(d_twvpx@yu%q$k9&fluk=g06!6eea&b7"
ENV CELERY_BROKER_URL="redis://localhost:6379"
ENV CELERY_BACKEND="redis://localhost:6379"

RUN mkdir -p /app/staticfiles && chmod -R 755 /app/staticfiles
RUN python manage.py collectstatic --noinput || echo "Static files collection failed"

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]