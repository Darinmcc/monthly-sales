import csv

csv_file_path = "data/sales-201710.csv"

file_date_year = csv_file_path[11:15]
file_date_month = csv_file_path[15:17]

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

print(f"GENERATING SALES REPORT FOR MONTH OF OCTOBER {file_date_year}...")

total_sales = 0

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    for items in reader:
        
        total_sales += float(items["sales price"] )
        total_sales_usd = to_usd(total_sales)
    #for row in reader:
        #print(row["date"], row["product"], row["unit price"], row["units sold"], row["sales price"] )
        #date,product,unit price,units sold,sales price
    

print(f"SALES REPORT (MARCH {file_date_year})")
print(f"TOTAL SALES: $ {total_sales_usd}")