import csv
def search_name():
    name = input("Enter the contact name: ")

    try:
        with open('contact_infos.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) == 0:
                print("Contact list is empty.")
            else:
                found = False
                for row in rows:
                    if row[0].lower() == name.lower():
                        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
                        found = True
                        break
                if not found:
                    print("Contact named", name, "is not present contact list")

    except FileNotFoundError:
        print("The file 'contact_infos.csv' does not exist.")






