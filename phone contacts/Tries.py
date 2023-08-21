from enum import Enum
import json

class Actions(Enum):
  PRINT = 0
  ADD = 1 
  DELETE = 2
  SEARCH = 3
  EXIT = 5
  
contacts = []

def display_menu():
  for x in Actions:
    print(f'{x.value} - {x.name}')
  selection = input("Your Selection: ")
  return Actions(int(selection))

def print_contacts():
  print(contacts)

def add_contact():
  name = input("Enter name: ")
  phone = input("Enter phone: ")
  contacts.append({"name": name, "phone": phone})

def delete_contact():
  name = input("Name to delete: ")
  global contacts 
  contacts = [c for c in contacts if c["name"] != name]

def search_contacts():
  query = input("Search name: ")
  results = [c for c in contacts if query in c["name"]]
  print(f"Found: {results}" if results else f"No results found for '{query}'")

def menu():
  while True:
    option = display_menu()
    
    if option == Actions.PRINT:
      print_contacts()
    elif option == Actions.ADD:
      add_contact()
    elif option == Actions.DELETE:
      delete_contact()
    elif option == Actions.SEARCH:
      search_contacts()
    elif option == Actions.EXIT:
      break
    
def save_contacts():
  with open("contacts.json", "w") as f:
    json.dump(contacts, f)

def load_contacts():
  global contacts
  try: 
    with open("contacts.json") as f:
      contacts = json.load(f)
  except FileNotFoundError:
    print("No contacts file found, starting with empty list")
    contacts = []

if __name__ == "__main__":
  load_contacts()  
  menu()  
  save_contacts()