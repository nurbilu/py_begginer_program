from enum import Enum

class Actions(Enum):
    PRINT = 0
    ADD = 1 
    DELETE = 2
    SEARCH = 3
    EXIT = 5    

contacts=[]

def display_menu():
    for x in Actions: print(f'{x.value}' - {x.name})
    return Actions(int(input("Your Selection: ")))


def P_menu():
    while(True):
        result = display_menu()
        if result == Actions.PRINT : print(contacts)
        if result == Actions.ADD : contacts.append({"name":input("please enter a name") , "tel":input("please enter a tel num")})
        if result == Actions.DELETE: name_to_delete = input("Enter a name to delete: ")
        contacts = [contact for contact in contacts if contact["name"] != name_to_delete]

        if result == Actions.SEARCH : 
            search_key = input("Enter a name to search for: ")
            found_contacts = [c for c in contacts if search_key in c["name"]]
            print(f"Found contacts: {found_contacts}" if found_contacts else f"No contacts found with '{search_key}'")
        if result == Actions.EXIT : return
        print("Your selection is: ")