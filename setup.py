# -*- coding: utf-8 -*-
# flake8: noqa
from setuptools import find_packages, setup

entry_points = """
[console_scripts]
run_web=app.web:runserver
"""

setup(
    name='buildout',
    version='0.0.1',
    license='PRIVATE',
    author='',
    author_email='',
    url='https://github.com/mathbugua/buildout',
    description=u'buildout example',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=[
        'Flask'
    ],
    entry_points=entry_points,
)
