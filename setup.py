#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='youneedtosleep',
    version='0.1.0',
    description='Time Tracker',
    long_description=readme + '\n\n' + history,
    author='Christopher Grebs',
    author_email='cg@webshox.org',
    url='https://github.com/YouNeedToSleep/youneedtosleep',
    packages=[
        'youneedtosleep',
    ],
    package_dir={'youneedtosleep':
                 'youneedtosleep'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='youneedtosleep',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)