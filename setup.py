#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sonarqube_new_code",
    version_config=True,
    setup_requires=['setuptools-git-versioning'],
    author="Hector",
    author_email="hector@mrjeffapp.com",
    description="sonarqube_new_code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeff-labs/sonarqube-new-code",
    packages=find_packages(),
    install_requires=[],
    scripts=['bin/sonarqube_new_code']
)
