#!/usr/bin/env python
import os
from setuptools import setup

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

packages = [
    'module1'
]

requires = ['pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'riak',
    'requests',
    'wsgi-intercept']

setup(
    name='module1',
    version='0.1',
    description='Duh, Module1',
    long_description=readme,
    author='Adam Venturella',
    author_email='aventurella@gmail.com',
    url='http://github.com/aventurella',
    license=license,
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    package_dir={'module1': 'module1'},
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ),

)

del os.environ['PYTHONDONTWRITEBYTECODE']
