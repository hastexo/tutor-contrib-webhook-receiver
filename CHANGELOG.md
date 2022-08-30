## Unreleased

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
