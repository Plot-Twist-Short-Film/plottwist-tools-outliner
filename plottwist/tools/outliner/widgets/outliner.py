#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Custom outliner for Plot Twist
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtWidgets import *

import tpDcc as tp

import artellapipe


class OutlinerToolWidget(artellapipe.ToolWidget, object):

    def __init__(self, project, config, settings, parent):
        super(OutlinerToolWidget, self).__init__(project=project, config=config, settings=settings, parent=parent)

    def ui(self):
        super(OutlinerToolWidget, self).ui()
