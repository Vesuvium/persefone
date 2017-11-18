#!/usr/bin/env python
import io

from setuptools import find_packages, setup


readme = io.open('README.rst', 'r', encoding='utf-8').read()

setup(
    name='persefone',
    description='Encoder for the Siren hypermedia format',
    long_description=readme,
    url='https://github.com/Vesuvium/persefone',
    author='Jacopo Cascioli',
    author_email='jacopocascioli@gmail.com',
    license='MIT',
    version='0.0.0',
    packages=find_packages(),
    tests_require=[
        'pytest',
        'pytest-mock'
    ],
    setup_requires=['pytest-runner'],
    install_requires=[
        'ujson>=1.35'
    ],
    classifiers=[]
)
