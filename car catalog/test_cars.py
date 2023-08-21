# import csv
# from enum import Enum

# class Commands_cars(Enum):
#     PRINT = 0
#     ADD = 1
#     DELETE = 2
#     SEARCH = 3
#     EXIT = 4  # Updated the EXIT value

# cars = []

# def display_menu():
#     for x in Commands_cars:
#         print(f'{x.value} - {x.name}')
#     selection = input("Your Selection: ")
#     return Commands_cars(int(selection))

# def print_cars():
#     print(cars)

# def add_car():
#     year = int(input("Enter year: "))
#     color = input("Enter color: ")
#     maker = input("Enter maker: ")
#     cars.append({"year": year, "color": color, "maker": maker})

# def delete_car():
#     maker = input("Car to delete: ")
#     global cars
#     cars = [c for c in cars if c["maker"] != maker]

# def search_cars():
#     maker_query = input("Search maker: ")
#     results = [c for c in cars if maker_query.lower() in c["maker"].lower()]
#     print(f"Found: {results}" if results else f"No results found for '{maker_query}'")

# def menu():
#     while True:
#         option = display_menu()

#         if option == Commands_cars.PRINT:
#             print_cars()
#         elif option == Commands_cars.ADD:
#             add_car()
#         elif option == Commands_cars.DELETE:
#             delete_car()
#         elif option == Commands_cars.SEARCH:
#             search_cars()
#         elif option == Commands_cars.EXIT:
#             break

# def save_cars():
#     with open("cars.csv", "w", newline='') as f:
#         fieldnames = ["year", "color", "maker"]
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(cars)

# def load_cars():
#     global cars
#     try:
#         with open("cars.csv", newline='') as f:
#             reader = csv.DictReader(f)
#             cars = [row for row in reader]
#     except FileNotFoundError:
#         print("No cars file found, starting with an empty list")
#         cars = []

# if __name__ == "__main__":
#     load_cars()
#     menu()
#     save_cars()
