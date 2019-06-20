    
import os
import csv

def to_usd(my_price):
  # return "${0:,.2f}".format(my_price)
  return f"${my_price:,.2f}"

#
# INFO INPUTS
#

CSV_FILENAME = "sales-201710.csv"

csv_filepath = os.path.join("data", CSV_FILENAME)

rows = []

with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for items in reader:
        rows.append(dict(items)) # ideally we would transform all the prices from strings to floats here

print(rows[0])


# float(rows[0]["sales price"])
#> 130.10

sales_prices = [float(row["sales price"]) for row in rows] # list comprehension for mapping purposes!

total_sales = sum(sales_prices)

month = "MARCH" # TODO: get from file name or date values
year = 2018 # TODO: get from file name or date values

#
# INFO OUTPUTS
#

print("-------------------------")
print(f"SALES REPORT!")
print("-------------------------")
print(f"MONTH: {month} {year}")
print(f"TOTAL SALES: {to_usd(total_sales)}")