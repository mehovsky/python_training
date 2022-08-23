from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.contact_cache = None

    def edit_contact(self, new_contact_data, index):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_to_edit(index)
        self.fill_contact_form(new_contact_data)
        # Submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def edit_contact_by_id(self, new_contact_data, id):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(new_contact_data)
        # Submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def open_contact_to_edit(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[3]/ul/li[1]/a").click()
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            cell_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            if cell_id == id:
                cells[7].click()
                break

    def open_contact_view(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def delete_contact(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def select_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                td = element.find_elements_by_tag_name("td")
                lastname = td[1].text
                firstname = td[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = td[5].text
                address = td[3].text
                all_mails = td[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_mails_from_home_page=all_mails))
        return list(self.contact_cache)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        second_phone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        mail1 = wd.find_element_by_name("email").get_attribute("value")
        mail2 = wd.find_element_by_name("email2").get_attribute("value")
        mail3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, second_phone=second_phone,
                       address=address, email=mail1, email2=mail2, email3=mail3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        second_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, second_phone=second_phone)

    def change_old_contact_list(self, old_contacts, id, new_data):
        for item in old_contacts:
            if item.id == id:
                item.firstname = new_data.firstname
                item.lastname = new_data.lastname
                break
        return old_contacts

    def get_info_from_contacts_list(self, contacts, key):
        data_list = []
        for item in contacts:
            if key == 'emails':
                data_list.append(item.all_mails_from_home_page)
            elif key == 'phones':
                data_list.append(item.all_phones_from_home_page)
            elif key == 'lastname':
                data_list.append(item.lastname)
            elif key == 'firstname':
                data_list.append(item.firstname)
            elif key == 'address':
                data_list.append(item.address)
        return data_list

    @staticmethod
    def clear(s: str):
        return re.sub("[() -]", "", s)

    def merge_emails(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))

    def merge_emails_from_db(self, contacts):
        merged_users_email_list = []
        for item in contacts:
            merged_users_email_list.append(self.merge_emails(item))
        return merged_users_email_list

    def merge_phones_from_db(self, contacts):
        merged_users_phone_list = []
        for item in contacts:
            merged_users_phone_list.append(self.merge_phones(item))
        return merged_users_phone_list

    def merge_phones(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: ContactHelper.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone_number, contact.mobile_phone_number,
                                            contact.work_phone_number, contact.phone2]))))