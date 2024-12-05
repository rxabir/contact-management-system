import add_contact
import view_contact
import remove_contact
import search
while True:
    print("\n")
    print("Welcome to the contact book Management system")
    print("---------------------------------------------")
    print("1. Add a new contact")
    print("2. View all the contacts")
    print("3. Remove contact")
    print("4. Search contact")
    print("5. Exit")
    print("---------------------------------------------")

    menu = input("Select the operation you want to perform: ")
    print("\n")

    if menu == "1":
        add_contact.add_contacts()
    elif menu == "2":
        view_contact.view_contacts()
    elif menu == "3":
        remove_contact.remove_contacts()
    elif menu == "4":
        search.search_name()
    elif menu == "5":
        break
    else:
        print("Please choose a valid number to perform the operation.")
