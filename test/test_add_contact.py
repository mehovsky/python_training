# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Sergey", middlename="Anatolevich", lastname="Mekhovsky", nickname="mehovsky",
                               title="title", company="company", address="SPB", home_phone_number="home", mobile_phone_number="123", work_phone_number="work",
                               fax="fax", email="1@mail.ru", email2="2@mail.ru", email3="3@mail.ru", homepage="homepage",
                               bday="20", bmonth="February", byear="1996", aday="5", amonth="March", ayear="2000",
                               address2="SPB", phone2="123", notes="notes"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
#                               title="", company="", address="", home_phone_number="", mobile_phone_number="", work_phone_number="",
#                               fax="", email="", email2="", email3="", homepage="",
#                               bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="",
#                               address2="", phone2="", notes=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)