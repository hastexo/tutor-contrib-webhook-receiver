FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN python3 -m venv /webhook_receiver/venv/
ENV PATH "/webhook_receiver/venv/bin:$PATH"
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev && \
    git clone https://github.com/hastexo/webhook-receiver.git ./webhooks
WORKDIR ./webhooks
RUN pip install --upgrade pip && \
    pip install -r requirements/production.txt --exists-action w
