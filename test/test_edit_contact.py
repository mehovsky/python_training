# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Sergey"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="update")
    app.contact.edit_contact(contact, index)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)