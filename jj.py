def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Display All Contacts")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input(f"Enter new phone number for '{name}': ")
        contacts[name] = phone
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def search_contact(contacts):
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def display_all_contacts(contacts):
    if contacts:
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            update_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            display_all_contacts(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
