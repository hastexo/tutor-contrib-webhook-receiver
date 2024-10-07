Tutor plugin for [Open edX Webhook Receiver](https://github.com/hastexo/webhook-receiver)
===================================

This is an **experimental** plugin for
[Tutor](https://docs.tutor.overhang.io) that deploys the
[Open edX Webhook Receiver](https://github.com/hastexo/webhook-receiver) 
application alongside Open edX.

Version compatibility matrix
----------------------------

You must install a supported release of this plugin to match the Open
edX and Tutor version you are deploying. If you are installing this
plugin from a branch in this Git repository, you must select the
appropriate one:

| Open edX release | Tutor version     | Plugin branch | Plugin release |
|------------------|-------------------|---------------|----------------|
| Lilac            | `>=12.0, <13`     | Not supported | Not supported  |
| Maple            | `>=13.2, <14`[^1] | `maple`       | 0.1.x          |
| Nutmeg           | `>=14.0, <15`     | `nutmeg`      | 1.0.x          |
| Olive            | `>=15.0, <16`     | `olive`       | 2.2.x          |
| Palm             | `>=16.0, <17`     | `palm`        | 2.3.x          |
| Quince           | `>=17.0, <18`     | `quince`      | `>=2.4.0, <3`  |
| Redwood          | `>=18.0, <19`     | `main`        | `>=3`          |


[^1]: For Open edX Maple and Tutor 13, you must run version 13.2.0 or
    later. That is because this plugin uses the Tutor v1 plugin API,
    [which was introduced with that
    release](https://github.com/overhangio/tutor/blob/master/CHANGELOG.md#v1320-2022-04-24).

Installation
------------

    pip install git+https://github.com/hastexo/tutor-contrib-webhook-receiver@v3.0.0

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
* `WEBHOOKRECEIVER_REPOSITORY` (default `"https://github.com/hastexo/webhook-receiver.git"`)
* `WEBHOOKRECEIVER_REVISION` (default `"main"`)
* `WEBHOOKRECEIVER_SHOPIFY_SHOP_DOMAIN` (default `""`)
* `WEBHOOKRECEIVER_SHOPIFY_API_KEY` (default `""`)
* `WEBHOOKRECEIVER_WOOCOMMERCE_SOURCE` (default `""`)
* `WEBHOOKRECEIVER_WOOCOMMERCE_SECRET` (default `""`)

These values can be modified with `tutor config save --set
PARAM_NAME=VALUE` commands.
