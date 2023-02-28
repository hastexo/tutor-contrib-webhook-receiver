from .__about__ import __version__
from glob import glob
import os
import pkg_resources
from tutor import hooks


config = {
    "unique": {
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

for service in ["mysql", "lms", "webhookreceiver"]:
    path = pkg_resources.resource_filename(
        "tutorwebhookreceiver", os.path.join(
            "templates", "webhookreceiver", "tasks", service, "init")
    )
    with open(path, encoding="utf-8") as task_file:
        task = task_file.read()
    hooks.Filters.CLI_DO_INIT_TASKS.add_item((service, task))

hooks.Filters.IMAGES_BUILD.add_item((
    "webhookreceiver",
    ("plugins", "webhookreceiver", "build", "webhookreceiver"),
    "{{ WEBHOOKRECEIVER_DOCKER_IMAGE }}",
    (),
))

hooks.Filters.IMAGES_PULL.add_item((
    "webhookreceiver",
    "{{ WEBHOOKRECEIVER_DOCKER_IMAGE }}",
))
hooks.Filters.IMAGES_PUSH.add_item((
    "webhookreceiver",
    "{{ WEBHOOKRECEIVER_DOCKER_IMAGE }}",
))

# Add the "templates" folder as a template root
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutorwebhookreceiver", "templates")
)
# Render the "build" and "apps" folders
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("webhookreceiver/build", "plugins"),
        ("webhookreceiver/apps", "plugins"),
    ],
)
# Load patches from files
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutorwebhookreceiver", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item(
            (os.path.basename(path), patch_file.read())
        )
# Add configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"WEBHOOKRECEIVER_{key}", value)
        for key, value in config.get("defaults", {}).items()
    ]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"WEBHOOKRECEIVER_{key}", value)
        for key, value in config.get("unique", {}).items()
    ]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(
    list(config.get("overrides", {}).items())
)
