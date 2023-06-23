# Python Contact Book

This repository contains a simple implementation of a contact book in Python. It uses three main files:

1. `main.py` - Where the program is run.
2. `contactbook.py` - The Contactlist class and its methods are defined here.
3. `contact.py` - The Contact class is defined here.

## Class Descriptions

### Contact Class

This class is defined in `contact.py`. It represents a contact, having `contact_name` and `phone_numbers` as its attributes.

### Contactlist Class

This class is defined in `contactbook.py`. It represents a contact list (or contact book), providing the following methods:

- `add_contact(name, number)`: Adds a contact with a specified name and number to the contact book.

- `remove_contact(name)`: Removes a contact with the specified name from the contact book.

- `search_contact_by_name(name)`: Searches for a contact by its name and prints its details.

- `search_contact_by_phone_number(phone_number)`: Searches for a contact by its phone number and prints its details.

- `display_contactbook()`: Displays all the contacts in the contact book.

## Usage

The `main.py` file contains the program execution. Here is an excerpt:

```python
from contact import Contact
from contactbook import Contactlist

my_contacts = Contactlist()

my_contacts.add_contact("Hans Meier", '0145799765')
my_contacts.add_contact("Elon Musk", "+13458256")
my_contacts.add_contact("Bill Gates", "+134298356")
my_contacts.add_contact("Jeff Bezos", "+19654985")
my_contacts.add_contact("Shakira", "+34679243")
my_contacts.add_contact("Pique", "+34679244")

my_contacts.search_contact_by_name("Pique")
my_contacts.display_contactbook()

my_contacts.remove_contact("Pique")
my_contacts.display_contactbook()

my_contacts.search_contact_by_phone_number("+34679243")
```
In this sample, contacts are added to the contact list, then a contact is searched by name and the entire contact book is displayed. After that, a contact is removed and the updated contact book is displayed. Finally, a contact is searched by its phone number.

## Created by
Sebastian Viehhofer
