# Importing cvs's for PyRamen. Calculate metrics and output a txt file.

# Import Libraries
import csv
from pathlib import Path

# Initalize paths
menu_filepath = Path('Resources/menu_data.csv') 
sales_filepath = Path('Resources/sales_data.csv')

# Initilize needed variables, dict or lists.
menu = []
sales = []
report = {}
row_count = 0

# read menu csv
with open(menu_filepath, 'r') as csvfile:
    # print(csvfile)
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    header = next(csv_reader)
    
    # print(f"{header} <- this is the header" )
    
    for row in csv_reader:
        menu.append(row)

# read sales csv
with open(sales_filepath, 'r') as csvfile:
    # print(csvfile)
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    header = next(csv_reader)
    
    # print(f"{header} <- this is the header" )
    
    for row in csv_reader:
        sales.append(row)

# create a metric dict for each new menu item
for sales_row in sales:
    
    sales_item = sales_row[4] 
    quantity = sales_row[3]

    if sales_item not in report:
        report[sales_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}
    else:
        continue

# extra quantites from sales to report
for sales_row in sales:
    
    sales_item = sales_row[4]
    quantity = sales_row[3]
    
    if sales_item in report:
        report[sales_item]["01-count"] += int(quantity)

# extra price and cost from menu and calculate revenue and cogs
for sales_row in sales:
    
    sales_item = sales_row[4]
    quantity = sales_row[3]
    
    for menu_row in menu:
        menu_item = menu_row[0]
        menu_price = menu_row[3]
        menu_cost = menu_row[4]
        
        if sales_item == menu_item:
            report[menu_item]["02-revenue"] += (int(menu_price) * int(quantity))
            report[menu_item]["03-cogs"] += (int(menu_cost) * int(quantity))
        elif sales_item != menu_item:
            continue

# calculate profit using revenue and cogs
for item, valuedict in report.items():
     
    for key in valuedict:
        
        cogs = report[item]["03-cogs"]
        revenue = report[item]["02-revenue"]
        
        if key == "04-profit":
            report[item][key] = revenue - cogs
        else:
            continue 

# output file with metrics
output_path = Path("PyRamen.txt")

with open(output_path, 'w') as file:
    file.write("This is the financial report for PyRamen.\n")
    for key in report:
        file.write(f"{key} {report[key]} \n")

            