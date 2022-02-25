Tutor plugin for [Open edX Webhook Receiver](https://github.com/hastexo/webhook-receiver)
===================================

This is an **experimental** plugin for
[Tutor](https://docs.tutor.overhang.io) that deploys the
[Open edX Webhook Receiver](https://github.com/hastexo/webhook-receiver) 
application alongside Open edX.

Installation
------------

    pip install git+https://github.com/hastexo/tutor-contrib-webhook-receiver@v0.0.0

Then, to enable this plugin, run:

    tutor plugins enable webhookreceiver

Before starting Tutor, build the docker image for the 
`webhookreceiver` service:

    tutor images build webhookreceiver


Configuration
-------------

* `WEBHOOKRECEIVER_HOST` (default `"webhooks.{{ LMS_HOST }}"`)
* `WEBHOOKRECEIVER_DB_NAME` (default `"webhook_receiver"`)
* `WEBHOOKRECEIVER_DB_USER` (default `"webhook_receiver01"`)
* `WEBHOOKRECEIVER_DB_MIGRATION_OPTIONS` (default `{}`)
* `WEBHOOKRECEIVER_DJANGO_LOG_LEVEL` (default `"DEBUG"`)
* `WEBHOOKRECEIVER_EDX_OAUTH2_KEY` (default `"webhook_receiver"`)
* `WEBHOOKRECEIVER_SHOPIFY_SHOP_DOMAIN` (default `""`)
* `WEBHOOKRECEIVER_SHOPIFY_API_KEY` (default `""`)
* `WEBHOOKRECEIVER_WOOCOMMERCE_SOURCE` (default `""`)
* `WEBHOOKRECEIVER_WOOCOMMERCE_SECRET` (default `""`)

These values can be modified with `tutor config save --set
PARAM_NAME=VALUE` commands.
