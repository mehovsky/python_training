import random
from model.contact import Contact
from model.group import Group
from model.contact_in_group import ContactInGroup


def test_del_contact_to_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Sergey"))
        #old_list_contacts = db.get_contact_in_group_list()
        #groups_list = db.get_group_list()
        #group = random.choice(groups_list)
        #contacts_list = orm.get_contacts_not_in_groups(group)
        #user = random.choice(contacts_list)
        #app.contact.add_contact_to_group(user.id, group)
        #old_list_contacts.append(ContactInGroup(id=user.id))
    old_list_user = orm.get_groups_with_users()
    group = random.choice(old_list_user)
    user_in_group = orm.get_contacts_in_groups(group)
    user = random.choice(user_in_group)
    app.contact.delete_contact_from_group(user.id, group)
    new_list_user_in_group = orm.get_contacts_in_groups(group)
    user_in_group.remove(user)
    assert user_in_group == new_list_user_in_group