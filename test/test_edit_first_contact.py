# -*- coding: utf-8 -*-
from model.contact import Contact


#def test_edit_first_contact(app):
#    app.contact.edit_first_contact(Contact(firstname="update", middlename="update", lastname="update", nickname="update",
#                               title="", company="", address="", home_phone_number="", mobile_phone_number="", work_phone_number="",
#                               fax="", email="", email2="", email3="", homepage="",
#                               bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="",
#                               address2="", phone2="", notes="update"))


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Sergey"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="update"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)