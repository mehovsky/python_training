# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
        if len(db.get_group_list()) == 0:
                app.group.create(Group(name=""))
        old_groups = db.get_group_list()
        group = Group(name="update")
        group_ = random.choice(old_groups)
        app.group.edit_group_by_id(group, group_.id)
        new_groups = db.get_group_list()
        old_groups = app.group.change_old_groups_list(old_groups, group_.id, new_data=Group(name="update"))
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_edit_group_header(app):
#        if app.group.count() == 0:
#                app.group.create(Group(header=""))
#        old_groups = app.group.get_group_list()
#        group = Group(header="update")
#        group.id = old_groups[0].id
#        app.group.edit_first_group(group)
#        new_groups = app.group.get_group_list()
#        assert len(old_groups) == len(new_groups)
#        old_groups[0] = group
#        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)