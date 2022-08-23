import re
from model.contact import Contact


def test_data_on_home_page(app, db):
    contact_list_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_list_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert app.contact.get_info_from_contacts_list(contact_list_from_home_page, key='emails') == app.contact.merge_emails_from_db(contact_list_from_db)
    assert app.contact.get_info_from_contacts_list(contact_list_from_home_page, key='phones') == app.contact.merge_phones_from_db(contact_list_from_db)
    assert app.contact.get_info_from_contacts_list(contact_list_from_home_page, key='lastname') == app.contact.get_info_from_contacts_list(contact_list_from_db, key='lastname')
    assert app.contact.get_info_from_contacts_list(contact_list_from_home_page, key='firstname') == app.contact.get_info_from_contacts_list(contact_list_from_db, key='firstname')
    assert app.contact.get_info_from_contacts_list(contact_list_from_home_page, key='address') == app.contact.get_info_from_contacts_list(contact_list_from_db, key='address')


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone_number == contact_from_edit_page.home_phone_number
    assert contact_from_view_page.work_phone_number == contact_from_edit_page.work_phone_number
    assert contact_from_view_page.mobile_phone_number == contact_from_edit_page.mobile_phone_number
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone_number, contact.mobile_phone_number,
                                        contact.work_phone_number, contact.phone2]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))