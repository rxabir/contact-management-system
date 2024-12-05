import csv

all_contacts = []

def add_contacts():
    name = str(input("Enter contact's Name: "))
    email = str(input("Enter contact's Email: "))
    while True:
        try:
            phone = int(input("Enter contact's Phone: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid phone number (numbers only).")
            add_contacts()

    address = str(input("Enter contact's Address: "))

    try:
        mylist = []
        with open('contact_infos.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                mylist.append({"name": row[0], "email": row[1], "phone": row[2], "address": row[3]})

        for contact in mylist:
            if contact["phone"] == str(phone):
                print("This phone number already exists in the contact list.")
                print("Try again using a different number.")
                return add_contacts()
    except IndexError:
        pass
    except FileNotFoundError:
        pass

    contact = {"name": name,
               "email": email,
               "phone": phone,
               "address": address}
    all_contacts.append(contact)
    save_contact(all_contacts)
    print("Contact added successfully.")
    all_contacts.clear()
    return all_contacts

def save_contact(all_contacts):
    try:
        with open("contact_infos.csv", 'a', newline='') as fp:
            for contact in all_contacts:
                line = f"{contact["name"]},{contact["email"]},{contact["phone"]},{contact["address"]}\n"
                fp.write(line)
    except FileNotFoundError:
        with open("contact_infos.csv", 'w', newline='') as fp:
            for contact in all_contacts:
                line = f"{contact["name"]},{contact["email"]},{contact["phone"]},{contact["address"]}\n"
                fp.write(line)




