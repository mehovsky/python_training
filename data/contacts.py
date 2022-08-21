from model.contact import Contact


testdata = [
               Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                 address="", home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="", homepage="",
                 bday="20", bmonth="July", byear="2020", aday="10", amonth="August", ayear="2010", address2="", second_phone="", notes="")] + [
        Contact(firstname=("firstname", 5), middlename=("middlename", 5), lastname=("lastname", 5), nickname=("nickname", 5),
                title=("title", 5), address=("address", 5), home_phone=("home_phone", 5), mobile_phone=("mobile_phone", 5),
                work_phone=("work_phone", 5), fax=("fax", 5), email=("email", 5), email2=("email2", 5), email3=("email3", 5),
                homepage=("homepage", 5), bday="20", bmonth="July", byear="2020", aday="10", amonth="August", ayear="2010", address2=("address2", 5),
                second_phone=("second_phone", 5), notes=("notes", 5))
        for i in range(5)
]