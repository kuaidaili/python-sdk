# -*- coding: utf-8 -*-

import sys
from setuptools import setup

if sys.version_info < (3,0):
    long_description_file = open('README.rst').read()
else:
    long_description_file=open('README.rst', encoding='UTF-8').read()

setup(
    name='kdl',
    version='0.2.18',
    description=(
        'kuaidaili api sdk python, site: https://www.kuaidaili.com'
    ),

    long_description=long_description_file,
    author='kuaidaili-dev',
    author_email='service@kuaidaili.com',
    license='BSD License',
    packages= [
        'kdl',
    ],
    platforms='any',
    install_requires=[
        'requests'
    ],
    url='https://github.com/kuaidaili/python-sdk/api-sdk',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
)
