FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN python3 -m venv /webhook_receiver/venv/
ENV PATH "/webhook_receiver/venv/bin:$PATH"
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev && \
    git clone {{ WEBHOOKRECEIVER_REPOSITORY }} ./webhooks
WORKDIR ./webhooks
RUN git checkout {{ WEBHOOKRECEIVER_REVISION }}
RUN pip install --upgrade pip && \
    pip install -r requirements/production.txt --exists-action w
EXPOSE 8090
CMD gunicorn --env DJANGO_SETTINGS_MODULE=webhook_receiver.settings.production webhook_receiver.wsgi:application --bind 0.0.0.0:8090
