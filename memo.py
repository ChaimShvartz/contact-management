import json
from contacts import Contact

def load_memo():
    try:
        with open('contacts.json') as f:
            return [Contact(*(contact.values())) for contact in json.load(f)]
    except FileNotFoundError:
        with open('contacts.json', 'w') as f:
            pass
        return []


def update_memo(contacts):
    try:
        with open('contacts.json', 'w') as f:
            json.dump([contact.__dict__ for contact in contacts], f, indent=4)
    except Exception as e:
        print(e)