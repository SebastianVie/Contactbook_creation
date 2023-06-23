
from contact import Contact
class Contactlist:
    def __init__(self):
        self.phonebook = []

    def add_contact(self, contact):
        self.phonebook.append(contact)

    def add_contact(self, name, number):
        self.phonebook.append(Contact(name, number))
        print("Your contact " + name + " has beenn added.")

    def remove_contact(self, name):
        for contact in self.phonebook:
          if name == contact.contact_name:
            self.phonebook.remove(contact)
            print("Your contact " + contact.contact_name + " has been removed.")

    def search_contact_by_name(self, name):
        for contact in self.phonebook:
            if name == contact.contact_name:
                print("Name: " + contact.contact_name + "; Phone Number: " + contact.phone_numbers)


    def search_contact_by_phone_number(self, phone_number):
        for contact in self.phonebook:
            if phone_number == contact.phone_numbers:
                print("Name: " + contact.contact_name + "; Phone Number: " + contact.phone_numbers)
            
    def display_contactbook(self):
        for contact in self.phonebook:
            print("Name " + contact.contact_name + "; Phone Number: " + contact.phone_numbers)
