import csv
all_contacts = []
def remove_contacts():
    try:
        index_number = int(input("Enter the number of contact which you want to remove: ")) - 1

        try:
            with open('contact_infos.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    all_contacts.append({"name": row[0], "email": row[1], "phone": row[2], "address": row[3]})

            if index_number < len(all_contacts):
                contact = all_contacts.pop(index_number)
                del_save_contact(all_contacts)
                all_contacts.clear()
                print("Contact removed successfully")
                return all_contacts
        except IndexError:
            print("Contact list is empty.")

    except FileNotFoundError:
        print("The file 'contact_infos.csv' does not exist.")



def del_save_contact(all_contacts):
    with open("contact_infos.csv",'w',newline='') as fp:
        for contact in all_contacts:
            line = f"{contact["name"]},{contact["email"]},{contact["phone"]},{contact["address"]}\n"
            fp.write(line)
