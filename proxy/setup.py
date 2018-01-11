# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='proxy',
    version='0.0.1',
    description='Script to get proxy.',
    long_description=readme,
    author='Mervyn Zhang',
    author_email='zmy@foreverz.cn',
    url='https://github.com/foreverzmy/PythonDemo',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')))
