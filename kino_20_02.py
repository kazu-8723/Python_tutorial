import csv

with open("test.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Yamada", 180, 70])

"""
with open("test.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerows([["Ochiai", 200, 100], ["Suzuki", 175, 65], ["Aoki", 190, 105], ["Minato", 150, 40]])
"""
"""
with open("test.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
"""
