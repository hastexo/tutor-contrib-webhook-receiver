Tutor plugin for [Open edX Webhook Receiver](https://github.com/hastexo/webhook-receiver)
===================================

This is an **experimental** plugin for
[Tutor](https://docs.tutor.overhang.io) that deploys the
[Open edX Webhook Receiver](https://github.com/hastexo/webhook-receiver) 
application alongside Open edX.

Installation
------------

    pip install git+https://github.com/hastexo/tutor-contrib-webhook-receiver

Then, to enable this plugin, run:

    tutor plugins enable webhook_receiver

Before starting Tutor, build the docker image for the 
`webhook_receiver` service:

    tutor images build webhook_receiver


Configuration
-------------

* `WEBHOOK_RECEIVER_HOST` (default `"webhooks.{{ LMS_HOST }}"`)
* `WEBHOOK_RECEIVER_DB_NAME` (default `"webhook_receiver"`)
* `WEBHOOK_RECEIVER_DB_USER` (default `"webhook_receiver01"`)
* `WEBHOOK_RECEIVER_DB_MIGRATION_OPTIONS` (default `{}`)
* `WEBHOOK_RECEIVER_DJANGO_LOG_LEVEL` (default `"DEBUG"`)
* `WEBHOOK_RECEIVER_EDX_OAUTH2_KEY` (default `"webhook_receiver"`)
* `WEBHOOK_RECEIVER_SHOPIFY_SHOP_DOMAIN` (default `""`)
* `WEBHOOK_RECEIVER_SHOPIFY_API_KEY` (default `""`)
* `WEBHOOK_RECEIVER_WOOCOMMERCE_SOURCE` (default `""`)
* `WEBHOOK_RECEIVER_WOOCOMMERCE_SECRET` (default `""`)

These values can be modified with `tutor config save --set
PARAM_NAME=VALUE` commands.
