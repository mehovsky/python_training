# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Sergey"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="update")
    app.contact.edit_first_contact(contact)
    contact.id = old_contacts[0].id
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)