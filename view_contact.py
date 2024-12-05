import csv

def view_contacts():
    try:
        with open('contact_infos.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)

            if len(rows) == 0:
                print("Contact list is empty.")
            else:
                print(f"Name | Email | Phone | Address")
                for row in rows:
                    print(f"{row[0]} | {row[1]} | 0{row[2]} | {row[3]}")
    except FileNotFoundError:
        print("The file 'contact_infos.csv' does not exist.")





