import csv

# Sample data
new_cars = {"year": 2025, "color": "Green", "make": "Kia"}

# Open the CSV file in write mode (use 'newline='' to ensure proper line endings)
with open("cars.csv", "a", newline='') as f:
    fieldnames = ["year", "color", "make"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # If the file is empty, write the header row
    if f.tell() == 0:
        writer.writeheader()

    # Write the new car data to the CSV file
    writer.writerow(new_cars)

print("New car data has been saved to cars.csv.")
print(new_cars)