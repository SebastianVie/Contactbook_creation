#%%
from contact import Contact
from contactbook import Contactlist

my_contacts = Contactlist()
#%%
my_contacts.add_contact("Hans Meier", '0145799765')
my_contacts.add_contact("Elon Musk", "+13458256")
my_contacts.add_contact("Bill Gates", "+134298356")
my_contacts.add_contact("Jeff Bezos", "+19654985")
my_contacts.add_contact("Shakira", "+34679243")
my_contacts.add_contact("Pique", "+34679244")
#%%
my_contacts.search_contact_by_name("Pique")
my_contacts.display_contactbook()
#%%
my_contacts.remove_contact("Pique")
my_contacts.display_contactbook()
#%%
my_contacts.search_contact_by_phone_number("+34679243")
# %%
