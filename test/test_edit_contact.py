# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Sergey"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="update")
    contact_ = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact, contact_.id)
    new_contacts = db.get_contact_list()
    old_contacts = app.contact.change_old_contact_list(old_contacts, contact_.id, new_data=Contact(firstname="update"))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)