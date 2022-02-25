from .__about__ import __version__
from glob import glob
import os
import pkg_resources


templates = pkg_resources.resource_filename(
    "tutorwebhookreceiver", "templates"
)

config = {
    "add": {
        "DB_PASSWORD": "{{ 32|random_string }}",
        "DJANGO_SECRET_KEY": "{{ 50|random_string }}",
        "EDX_OAUTH2_SECRET": "{{ 32|random_string }}",
    },
    "defaults": {
        "VERSION": __version__,
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}webhookreceiver:{{ WEBHOOKRECEIVER_VERSION }}",  # noqa: E501
        "HOST": "webhooks.{{ LMS_HOST }}",
        "DB_NAME": "webhook_receiver",
        "DB_USER": "webhook_receiver01",
        "DB_MIGRATION_OPTIONS": {},
        "DJANGO_LOG_LEVEL": "WARN",
        "LMS_ROOT_URL":
            "{{ 'https' if ENABLE_HTTPS else 'http' }}://{{ LMS_HOST }}",
        "EDX_OAUTH2_KEY": "webhook_receiver",
        "SHOPIFY_SHOP_DOMAIN": "",
        "SHOPIFY_API_KEY": "",
        "WOOCOMMERCE_SOURCE": "",
        "WOOCOMMERCE_SECRET": "",
    },
}

hooks = {
    "build-image": {
        "webhookreceiver": "{{ WEBHOOKRECEIVER_DOCKER_IMAGE }}",
    },
    "remote-image": {
        "webhookreceiver": "{{ WEBHOOKRECEIVER_DOCKER_IMAGE }}",
    },
    "init": ["mysql", "lms", "webhookreceiver"]
}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutorwebhookreceiver", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
