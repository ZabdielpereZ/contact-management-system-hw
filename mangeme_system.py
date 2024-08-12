from helper import clear
contacts = {}

def add_contact():
    name = input('Enter contact name :)\n')
    phone_num = input('Enter contact number :3\n')
    email = input('Enter contact email! :D\n')
    if phone_num in contacts:
        print('Contact already exists!')
    else:
        contacts[phone_num] = {
            'name': name,
            'email': email
        }
        print(f'{name} {email} and {phone_num} added to contacts! ^_^')

def edit_contact():
    phone = input("Enter phone number of the contact to edit: ")
    if phone in contacts:
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        contacts[phone]['name'] = name
        contacts[phone]['email'] = email
        print("Contact updated successfully! :D")
    else:
        print("Contact not found!")

def remove_contact():
    phone = input("Enter phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def search_contact():
    phone = input("Enter phone number to search: ")
    if phone in contacts:
        details = contacts[phone]
        print(f"Phone: {phone}, Name: {details['name']}, Email: {details['email']}")
    else:
        print("Contact not found!")

def display_contacts():
    print('Phone Book\n')
    for phone, details in contacts.items():
        print(f'Phone: {phone}, Name: {details["name"]}, Email: {details["email"]}')

def export_contacts(filename):
    with open(filename, 'w') as file:
        for phone, details in contacts.items():
            file.write(f"{phone},{details['name']},{details['email']}\n")
    print("Contacts exported successfully!")

def import_contacts(filename):
    with open(filename, 'r') as file:
        for line in file:
            phone, name, email = line.strip().split(',')
            contacts[phone] = {
                'name': name,
                'email': email
            }
    print("Contacts imported successfully!")

def main():
    while True:
        ans = input('''
CONTACT MANAGEMENT SYSTEM:                                                         

Enter the corresponding number for the action you'd like to take:
    1 - Add a new contact
    2 - Edit an existing contact
    3 - Delete a contact
    4 - Search for a contact
    5 - Display all contacts
    6 - Export contacts to a text file
    7 - Import contacts from a text file
    8 - Quit
''')
        if ans == '1':
            clear()
            add_contact() 
        elif ans == '2':
            clear()
            edit_contact() 
        elif ans == '3':
            clear()
            remove_contact()
        elif ans == '4':
            clear()
            search_contact() 
        elif ans == '5':
            clear()
            display_contacts()
        elif ans == '6':
            clear()
            filename = input("Enter filename to export contacts: ")
            export_contacts(filename)
        elif ans == '7':
            clear()
            filename = input("Enter filename to import contacts: ")
            import_contacts(filename)
        elif ans == '8':
            clear()
            print("THANKS FOR MANAGING!")
            break

if __name__ == "__main__":
    main()

