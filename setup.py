#!/usr/bin/python3
from setuptools import setup

setup(
    name='ManFuzzer',
    version='1.01',
    packages=['manparser', 'arguments', 'values', 'legacymanfuzzer'],
    include_package_data=True,
    license='Apache2.0',
    description='A tool to create fuzzing inputs for command line programs using help options and man pages',
    long_description="",
    url='https://github.com/CIFASIS/ManFuzzer/',
    author='G.Grieco',
    author_email='gg@cifasis-conicet.gov.ar',
    scripts=['manfuzzer'],
    install_requires=[
    ],
)

