from memo import *
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def add_email(self):
        email = input("Enter the email: ")
        self.email = email

class Contacts:
    def __init__(self):
        self.contacts = []

    @staticmethod
    def show_menu(self):
        print("""
    === Contacts Book ===
    1. Add contact
    2. Show all contacts
    3. Search contact
    4. Delete contact
    5. Edit contact
    6. Exit
    """)

    def add_contact(self):
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email(to skip press Enter): ") or None
        self.contacts.append(Contact(name, phone_number, email))

    def show_all_contacts(self):
        print(*self.contacts.__dict__)

    def search_contact(self, target):
        for contact in self.contacts:
            if contact.name == target:
                return contact.__dict__
        return f"{target} not exists"

    def delete_contact(self, target):
        for contact in self.contacts:
            if contact.name == target:
                delete(contact)
        else:
            print(f"{target} not exists")

    def edit_contact(self, target):
        for contact in self.contacts:
            if contact.name == target:
                edit(contact)
        else:
            print(f"{target} not exists")

