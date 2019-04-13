# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='kdl',
    version='0.0.1',
    description=(
        'kuaidaili sdk for api, site: https://www.kuaidaili.com'
    ),
    long_description=open('README.rst').read(),
    author='<kuaidaili-dev>',
    author_email='<service@kuaidaili.com>',
    license='BSD License',
    packages= [
        'kdl',
    ],
    platforms='any',
    install_requires=[
        'requests'
    ],
    url='<https://github.com/kuaidaili-dev>',
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