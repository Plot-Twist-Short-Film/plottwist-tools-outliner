#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for plottwist-tools-outliner
"""

import pytest

from plottwist.tools.outliner import __version__


def test_version():
    assert __version__.get_version()
