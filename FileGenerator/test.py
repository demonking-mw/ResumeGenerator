import csv

# Your 2D array
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
]

# Write to a CSV file
with open("output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
