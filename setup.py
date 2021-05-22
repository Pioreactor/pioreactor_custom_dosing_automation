# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()


setup(
    name="pioreactor_custom_dosing_automation",
    version="0.0.1",
    license="MIT",
    install_requires=REQUIREMENTS,
    long_description=open("README.md").read(),
    author_email="cam@pioreactor.com",
    packages=find_packages(),
    include_package_data=True,
    entry_points={'pioreactor.plugins': 'pioreactor_custom_dosing_automation = pioreactor_custom_dosing_automation'},
)
