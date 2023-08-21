import json

contacts=[]
def save_contacts(filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def load_contacts(filename):
    global contacts
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty contacts list
        contacts = []

def P_menu():
    while(True):
        print("P - print all contacts")
        print("A - add contect")
        print("D - delete contect")
        print("S - search contect")
        print("X - exit")
        result = input("Please choose")
        if result == "P" : print(contacts)
        if result == "A" : contacts.append({"name":input("please enter a name") , "tel":input("please enter a tel num")})
        if result == "D":name_to_delete = input("Enter a name to delete: ")
        contacts = [contact for contact in contacts if contact["name"] != name_to_delete]
        save_contacts('contacts.json')

        if result == "S" : 
            search_key = input("Enter a name to search for: ")
            found_contacts = [c for c in contacts if search_key in c["name"]]
            print(f"Found contacts: {found_contacts}" if found_contacts else f"No contacts found with '{search_key}'")
        if result == "X" : return
        print("Your selection is: ")
