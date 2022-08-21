from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as arr:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "--n":
        n = int(a)
    elif o == "--f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + " "*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                 address="", home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="", homepage="",
                 bday="20", bmonth="July", byear="2020", aday="10", amonth="August", ayear="2010", address2="", second_phone="", notes="")] + [
        Contact(firstname=random_string("firstname", 5), middlename=random_string("middlename", 5), lastname=random_string("lastname", 5), nickname=random_string("nickname", 5),
                title=random_string("title", 5), address=random_string("address", 5), home_phone=random_string("home_phone", 5), mobile_phone=random_string("mobile_phone", 5),
                work_phone=random_string("work_phone", 5), fax=random_string("fax", 5), email=random_string("email", 5), email2=random_string("email2", 5), email3=random_string("email3", 5),
                homepage=random_string("homepage", 5), bday="20", bmonth="July", byear="2020", aday="10", amonth="August", ayear="2010", address2=random_string("address2", 5),
                second_phone=random_string("second_phone", 5), notes=random_string("notes", 5))
        for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))