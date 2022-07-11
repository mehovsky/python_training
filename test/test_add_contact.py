# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Sergey", middlename="Anatolevich", lastname="Mekhovsky", nickname="mehovsky",
                               title="title", company="company", address="SPB", home_phone_number="home", mobile_phone_number="123", work_phone_number="work",
                               fax="fax", email="1@mail.ru", email2="2@mail.ru", email3="3@mail.ru", homepage="homepage",
                               bday="20", bmonth="February", byear="1996", aday="5", amonth="March", ayear="2000",
                               address2="SPB", phone2="123", notes="notes"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home_phone_number="", mobile_phone_number="", work_phone_number="",
                               fax="", email="", email2="", email3="", homepage="",
                               bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",
                               address2="", phone2="", notes=""))
    app.session.logout()