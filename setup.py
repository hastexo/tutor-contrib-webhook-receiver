import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


setup(
    name="tutor-contrib-webhook-receiver",
    use_scm_version=True,
    url="https://github.com/hastexo/tutor-contrib-webhook-receiver",
    project_urls={
        "Code": "https://github.com/hastexo/tutor-contrib-webhook-receiver",
        "Issue tracker":
            "https://github.com/hastexo/tutor-contrib-webhook-receiver/issues",
    },
    license="AGPLv3",
    author="hastexo",
    description="webhook-receiver plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor"],
    entry_points={
        "tutor.plugin.v0": [
            "webhook-receiver = tutor_webhook_receiver.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
