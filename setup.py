#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as fobj:
    readme = fobj.read()

with open('CHANGES.rst') as fobj:
    history = fobj.read()
    history.replace('.. :changelog:', '')


test_requires = [
    # General test libraries
    'tox>=1.8,<1.9',
    'py>=1.4.25,<1.5',
    'pytest>=2.6.3,<2.7',
    'pytest-django>=2.6.1,<2.7',

    # Pep8 and code quality checkers
    'pyflakes>=0.8.1,<0.9',
    'coverage>=3.7.1,<3.8',
    'pytest-cov>=1.8,<1.9',
    'pytest-flakes>=0.2,<1.0',
    'pytest-pep8>=1.0.5,<1.1',
    'pep8>=1.5.7,<1.6',
    'coverage>=3.7.1,<3.8',

    # Fixtures, test helpers
    'factory-boy>=2.4.1,<2.5',
    'mock>=1.0.1,<1.1',
    'httpretty>=0.8.0',
]


install_requires = [
    # General dependencies
    'django>=1.7,<1.8',

    # i18n/l10n,
    'babel>=1.3',
    'django-babel-underscore>=0.1.0',
    'django-statici18n>=1.1',
    'django-babel>=0.3.6',

    # For our REST Api
    'djangorestframework>=2.4.3,<2.5',
    'requests>=2.4.1,<2.5',

    'python-social-auth>=0.1.25',
    'requests>=2.3.0',
    'requests-oauthlib>=0.4.1',

    # Markdown support for browsable api
    'markdown',

    # Filtering support for the API
    'django-filter',
]


dev_requires = [
    'ipdb'
]


docs_requires = [
    'sphinx>=1.2.3',
    'sphinx_rtd_theme'
]


postgresql_requires = [
    'psycopg2>=2.5.4',
]

setup(
    name='sleepy',
    version='0.1.0',
    description='Simple and effective time tracking.',
    long_description=readme + '\n\n' + history,
    author='Christopher Grebs',
    author_email='cg@webshox.org',
    url='https://github.com/YouNeedToSleep/sleepy/',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    tests_require=test_requires,
    install_requires=install_requires,
    extras_require={
        'docs': docs_requires,
        'tests': test_requires,
        'dev': dev_requires,
        'postgresql': postgresql_requires,
    },
    zip_safe=False,
    license='BSD',
    classifiers=[
        '__DO NOT UPLOAD__',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
