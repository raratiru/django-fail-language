#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : setup.py
#
#       Creation Date : Mon 08 Apr 2019 07:00:40 PM EEST (19:00)
#
#       Last Modified : Wed 19 Aug 2020 10:54:15 PM EEST (22:54)
#
# ==============================================================================

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-fail-language",
    version="0.1",
    python_requires=">=3",
    description=(
        "A failing application with Django-3.1 only when ./manage.py migrate"
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/raratiru/django-fail-language",
    author="George Tantiras",
    license="BSD 3-Clause License",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["Django>=2.2"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)
