# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
        app.group.edit_first_group(Group(name="update"))


def test_edit_group_header(app):
        app.group.edit_first_group(Group(header="update"))