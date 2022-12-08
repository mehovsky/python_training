import random
from model.contact import Contact
from model.group import Group
from model.contact_in_group import ContactInGroup


def test_add_contact_to_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    old_contacts = orm.get_contacts_in_groups(group)
    contacts = [contact for contact in orm.get_contacts_not_in_groups(group)
                if contact not in old_contacts]
    if len(db.get_contact_list()) == 0 or len(contacts) == 0:
        app.contact.create(Contact(firstname="Sergey"))
    contacts = orm.get_contacts_not_in_groups(group)
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact.id, group)
    new_contacts = orm.get_contacts_in_groups(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactInGroup.id_max) == sorted(new_contacts, key=ContactInGroup.id_max)