#!/usr/bin/env python
"""
    setup.py - script for building MyApplication
    
    Usage:
    % python setup.py py2app
    """
from distutils.core import setup
import py2app

setup(
      app=['__main__.py'],
      data_files=[('resources/datetime_defaults.csv')],
      )
