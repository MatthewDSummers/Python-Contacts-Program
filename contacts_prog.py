import re

RED =  "\033[91m"
GREEN =  "\033[92m"
BLUE =  "\033[94m"
YELLOW =  "\033[93m"
MAGENTA =  "\033[95m"
CYAN =  "\033[96m"

RESET = "\033[0m"

class ContactBook:
    contacts = {}

    @classmethod
    def add_contact(cls, contact):
        contact_key = contact.full_name
        ContactBook.contacts[contact_key] = contact
        print("\n" + GREEN + f"New contact {contact.full_name} added." + RESET)

    @classmethod 
    def get(cls, full_name):
        if cls.contacts.get(full_name):
            contact = cls.contacts[full_name]
            print("\n" + CYAN + f"Contact found: {contact.full_name}, Phone number: {contact.phone_number}" + RESET)
            return cls.contacts[full_name]
        else:
            print("\n" + YELLOW + "Contact not found." + RESET)

    @classmethod
    def get_all(cls):
        if cls.contacts:
            print("\n")
            for i, contact in enumerate(cls.contacts.values()):
                print(CYAN + f"{i+1}: {contact.first_name} {contact.last_name}, Phone Number: {contact.phone_number}")
            print(RESET)
        else:
            print("\n" + YELLOW + "There are no contacts." + RESET)
        return cls.contacts

    @classmethod
    def delete(cls, full_name):
        if cls.contacts:
            if cls.contacts.get(full_name):
                del cls.contacts[full_name]
                print("\n" + RED + f"Contact {full_name} has been deleted." + RESET)
            else:
                print("\n" + YELLOW + "Contact not found." + RESET)
        else:
            print("\n" + YELLOW + "There are no contacts." + RESET)

class Contact:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name.rstrip()
        self.last_name = last_name.rstrip()
        self.full_name = self.first_name + " " + self.last_name
        self.phone_number = phone_number
        self.validate_data()

    def validate_data(self):
        errors = 0

        # FIRST NAME
        if not self.first_name.isalpha():
            errors += 1
            print("\n" + RED + "First name must only contain letters--not numbers or symbols." + RESET)

        if not isinstance(self.first_name, str):
            errors += 1
            print("\n" + RED + "First name must be a string." + RESET)

        elif len(self.first_name) < 2:
            errors += 1
            print("\n" + RED + "First name must have at least 2 characters." + RESET)

        # LAST NAME 
        if not self.last_name.isalpha():
            errors += 1
            print("\n" + RED + "Last name must only contain letters--not numbers or symbols." + RESET)

        if not isinstance(self.last_name, str):
            errors += 1
            print("\n" + RED + "First name must be a string." + RESET)

        elif len(self.last_name) < 2:
            errors += 1
            print("\n" + RED + "Last name must have at least 2 characters." + RESET)

        # PHONE NUMBER
        pattern = r'^\d{3}-\d{3}-\d{4}$'
        if not re.match(pattern, self.phone_number):
            errors += 1
            print("\n" + RED + "Phone number must be in ###-###-#### format." + RESET)

        if errors < 1:
            ContactBook.add_contact(self)

def contacts_program():
    while True:
        choice = input("\nMenu:\n a. Add a contact\n b. Lookup a contact\n c. Delete a contact\n d. View all contacts\n e. Quit \n\nEnter your choice: ").lower()

        responses = {
            "a": "Provide Contact's first name: ",
            "b": "Provide Contact's last name: ",
            "c": "Provide Contact's phone number in ###-###-#### format: ",
            "d": "Provide Contact's full name: ",
        }

        if choice == "a":
            first_name = input(responses["a"])
            last_name = input(responses["b"])
            phone_number = input(responses["c"])
            Contact(first_name=first_name, last_name=last_name, phone_number=phone_number)

        elif choice == "b":
            full_name = input(responses["d"])
            contact = ContactBook.get(full_name)

        elif choice == "c":
            full_name = input(responses["d"])
            ContactBook.delete(full_name)
        
        elif choice =="d":
            all_contacts = ContactBook.get_all()

        elif choice == "e":
            break
    return "Goodbye"

print(contacts_program())