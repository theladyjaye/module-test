#!/usr/bin/env python
import os
from setuptools import setup

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

packages = [
    'module2'
]

requires = ['pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'simplejson',
    'validictory',
    'webtest',
    'celery']

setup(
    name='module2',
    version='0.1',
    description='Duh, Module2',
    long_description=readme,
    author='Adam Venturella',
    author_email='aventurella@gmail.com',
    url='http://github.com/aventurella',
    license=license,
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    package_dir={'moduel2': 'module2'},
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ),
)

del os.environ['PYTHONDONTWRITEBYTECODE']
