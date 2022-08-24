import random
from model.contact import Contact
from model.group import Group
from model.contact_in_group import ContactInGroup


def test_add_contact_to_group(app, db, orm):
    #app.contact.choose_filter_on_home_page(key='[none]')
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Sergey"))
        #app.contact.choose_filter_on_home_page(key='[none]')
    old_list_contacts = db.get_contact_in_group_list()
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    contacts_list = orm.get_contacts_not_in_groups(group)
    user = random.choice(contacts_list)
    app.contact.add_contact_to_group(user.id, group)
    new_list_user_in_group = db.get_contact_in_group_list()
    old_list_contacts.append(ContactInGroup(id=user.id))
    assert sorted(old_list_contacts, key=ContactInGroup.id_max) == sorted(new_list_user_in_group, key=ContactInGroup.id_max)