"""
Package install information
"""

import ast
import os
import re

from setuptools import find_packages, setup

# Cannot use "from cloudbridge import get_version" because that would try to
# import the six package which may not be installed yet.
reg = re.compile(r'__version__\s*=\s*(.+)')
with open(os.path.join('cloudbridge', '__init__.py')) as f:
    for line in f:
        m = reg.match(line)
        if m:
            version = ast.literal_eval(m.group(1))
            break

REQS_BASE = [
    'bunch>=1.0.1',
    'six>=1.10.0',
    'retrying>=1.3.3'
]
REQS_AWS = ['boto3']
REQS_AZURE = ['msrest>=0.4.7',
              'msrestazure>=0.4.7',
              'azure-common>=1.1.5',
              'azure-mgmt-resource>=1.0.0rc1',
              'azure-mgmt-compute>=1.0.0rc1',
              'azure-mgmt-network>=1.0.0rc1',
              'azure-mgmt-storage>=1.0.0rc1',
              'azure-storage>=0.34.0',
              'pysftp>=0.2.9']
REQS_OPENSTACK = [
    'openstacksdk>=0.12.0',
    'python-novaclient>=7.0.0',
    'python-glanceclient>=2.5.0',
    'python-cinderclient>=1.9.0',
    'python-swiftclient>=3.2.0',
    'python-neutronclient>=6.0.0',
    'python-keystoneclient>=3.13.0'
]
REQS_FULL = REQS_BASE + REQS_AWS + REQS_AZURE + REQS_OPENSTACK
# httpretty is required with/for moto 1.0.0 or AWS tests fail
REQS_DEV = ([
    'tox>=2.1.1',
    'nose',
    # 'moto>=1.1.11',  # until https://github.com/spulec/moto/issues/1396
    'sphinx>=1.3.1',
    'pydevd',
    'flake8>=3.3.0',
    'flake8-import-order>=0.12'] + REQS_FULL
)

setup(
    name='cloudbridge',
    version=version,
    description='A simple layer of abstraction over multiple cloud providers.',
    author='Galaxy and GVL Projects',
    author_email='help@genome.edu.au',
    url='http://cloudbridge.cloudve.org/',
    install_requires=REQS_FULL,
    extras_require={
        ':python_version<"3.3"': ['ipaddress'],
        'full': REQS_FULL,
        'dev': REQS_DEV
    },
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'],
    test_suite="test"
)
