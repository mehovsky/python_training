# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Sergey"))
    app.contact.delete_first_contact()