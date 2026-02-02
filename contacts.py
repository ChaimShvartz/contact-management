from memo import *

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return str(self.__dict__)

    def add_email(self):
        if not self.email:
            email = input("Enter the email: ")
            self.email = email
        else:
            print(f"{self.name} already has email")

class Contacts:
    def __init__(self):
        self.contacts = load_memo()

    def __getitem__(self, item):
        for contact in self.contacts:
            if contact.name == item:
                return contact
        raise ValueError

    def __setitem__(self, key, value):
        self[key].phone_number =  value

    def __delitem__(self, key):
        for contact in self.contacts:
            if contact.name == key:
                self.contacts.remove(contact)
                return
        raise ValueError

    @staticmethod
    def show_menu():
        print("""
    === Contacts Book ===
    1. Add contact
    2. Show all contacts
    3. Search contact
    4. Delete contact
    5. Edit contact
    6. Add email
    7. Exit
    """)

    def add_contact(self):
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email(to skip press Enter): ") or None
        self.contacts.append(Contact(name,phone_number,email))

    def show_all_contacts(self):
        print(*self.contacts, sep='\n')

    def search_contact(self, target):
        try:
            print(self[target])
        except ValueError:
            print(f"{target} not exists")

    def delete_contact(self, target):
        try:
            del self[target]
        except (ValueError, KeyError):
            print(f"{target} not exists")
        else:
            print(f"{target} deleted")
            update_memo(self.contacts)

    def edit_contact(self, target, new_phone_number):
        try:
            self[target] = new_phone_number
        except ValueError:
            print(f"{target} not exists")
        else:
            update_memo(self.contacts)

    def add_email_to_contact(self, target):
        try:
            self[target].add_email()
        except ValueError:
            print(f"{target} not exists")

def main():
    contacts_list = Contacts()
    while True:
        contacts_list.show_menu()
        choice = input("Choose option: ")
        match choice:
            case '1':
                contacts_list.add_contact()
                update_memo(contacts_list.contacts)
            case '2':
                contacts_list.show_all_contacts()
            case '3':
                target = input("Enter the name you want searching for: ")
                contacts_list.search_contact(target)
            case '4':
                target = input("Enter the name you want delete: ")
                contacts_list.delete_contact(target)
                update_memo(contacts_list.contacts)
            case '5':
                target = input("Enter the name you want edit: ")
                new_phone_number = input("Enter the new phone number: ")
                contacts_list.edit_contact(target, new_phone_number)
                update_memo(contacts_list.contacts)
            case '6':
                target = input("Enter the name you want add email: ")
                contacts_list.add_email_to_contact(target)
            case '7':
                update_memo(contacts_list.contacts)
                break
            case _:
                continue
        input("Press Enter to continue: ")


if __name__ == "__main__":
    main()