## Unreleased

* [Enhancement] Support Tutor 19 and Open edX Sumac.

## Version 3.0.0 (2024-10-07)

* [Chore] Drop Python 3.8 support.

When updating your plugin to this version, you'll need to rebuild the image.

## Version 2.6.0 (2024-08-01)

* [Enhancement] Support Tutor 18 and Open edX Redwood.

## Version 2.5.0 (2024-04-05)

* [Enhancement] Support Python 3.12.

## Version 2.4.0 (2024-03-13)

* [Enhancement] Make the location and revision of the webhook-receiver application repository configurable.
* [Fix] Populate the webhook-receiver application's `ALLOWED_HOSTS` list from the value set for `WEBHOOKRECEIVER_HOST`.

## Version 2.3.0 (2024-02-07)

* [Enhancement] Add a new configuration variable, `WEBHOOKRECEIVER_WOOCOMMERCE_REQUIRE_PAYMENT`, for requiring completed payment on WooCommerce orders.

## Version 2.2.0 (2024-01-12)

* [Enhancement] Support Tutor 17 and Open edX Quince.

## Version 2.1.1 (2023-09-08)

* [fix] In the init job, ensure compatibility with MySQL 8.

## Version 2.1.0 (2023-08-22)

* [Enhancement] Support Tutor 16 and Open edX Palm, Python 3.10, and Python 3.11.

## Version 2.0.0 (2023-03-20)

* [BREAKING CHANGE] Add support for Tutor 15 and Open edX Olive.
  Tutor version 15.0.0 includes changes to the implementation of
  custom commands and thus requires changes in this plugin as well
  that are not backwards compatible.
  From version 2.0.0 this plugin only supports Tutor versions
  from 15.0.0 and Open edX Olive release.

## Version 1.0.1 (2022-08-30)

* [fix] Change lms-env-features patch to YAML format.

## Version 1.0.0 (2022-08-05)

* [BREAKING CHANGE] Support Tutor 14 and Open edX Nutmeg. This entails
  a configuration format change from JSON to YAML, meaning that from
  version 1.0.0 this plugin only supports Tutor versions from 14.0.0
  (and with that, only Open edX versions from Nutmeg).

## Version 0.1.0 (2022-06-29)

* [refactor] Use Tutor v1 plugin API

## Version 0.0.2 (2022-02-25)

* Fix version number as it appears in pip list (previously, all
  installations would show up as version 0.0.0, including
  installations from the 0.0.1 tag).


## Version 0.0.1 (2022-02-25)

**Experimental. Do not use in production.**

* Change plugin name to webhookreceiver
* Add webhook_receiver service
* Ensure Bulk Enrollment is activated
* Add basic testing via tox
* Initial Git import
