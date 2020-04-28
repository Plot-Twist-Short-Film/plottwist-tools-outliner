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

import artellapipe

# Defines ID of the tool
TOOL_ID = 'plottwist-tools-outliner'

# We skip the reloading of this module when launching the tool
no_reload = True


class {cookiecutter.tool_class}Tool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super({cookiecutter.tool_class}Tool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Outliner',
            'id': TOOL_ID,
            'logo': 'outliner_logo',
            'icon': 'outliner',
            'help_url': 'https://plot-twist-short-film.github.io/plottwist-docs/pipeline/pipeline/tools/outliner/',
            'kitsu_login': False,
            'tooltip': 'Custom outliner for Plot Twist',
            'tags': ['plottwist', 'outliner'],
            'sentry_id': '',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Outliner', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'TD',
                 'type': 'menu', 'children': [{'id': 'plottwist-tools-outliner', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'TD',
                 'children': [{'id': 'plottwist-tools-outliner', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class OutlinerToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(OutlinerToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from plottwist.tools.outliner.widgets import outliner

        tool_inst = outliner.OutlinerToolWidget(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [tool_inst]
