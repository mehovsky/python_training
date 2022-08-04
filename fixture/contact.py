from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # Init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # Submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_contact_page()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        # Init contact update
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # Submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_page()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_2(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone_number)
        self.change_field_value("mobile", contact.mobile_phone_number)
        self.change_field_value("work", contact.work_phone_number)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value_2("bday", contact.bday)
        self.change_field_value_2("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value_2("aday", contact.aday)
        self.change_field_value_2("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def open_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            td = element.find_elements_by_tag_name("td")
            lastname = td[1].text
            firstname = td[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return contacts

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))