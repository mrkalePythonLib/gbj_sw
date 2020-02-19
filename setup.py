#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup function for the package."""

from setuptools import setup, find_namespace_packages

setup(
  name='gbj_sw',
  version='1.0.1',
  description='Python libraries for software support.',
  long_description='Sub-packages suitable for whatever python console application.',
  classifiers=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Topic :: System :: Monitoring',
  ],
  keywords='configuration, mqtt, trigger, timer, statistics, filter, utils',
  url='http://github.com/mrkalePythonLib/gbj_sw',
  author='Libor Gabaj',
  author_email='libor.gabaj@gmail.com',
  license='MIT',
  packages=find_namespace_packages(),
  install_requires=[],
  include_package_data=True,
  zip_safe=False
)
