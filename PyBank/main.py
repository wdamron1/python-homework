'''''
Your task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset.
    Seems like a += loop counter with count.

The net total amount of Profit/Losses over the entire period.
    Sum up an entier column.

The average of the changes in Profit/Losses over the entire period.
    Told in class that this is the sum of the changes.
    Calculate the change. Add up all the changes. Probably a loop.
    
The greatest increase in profits (date and amount) over the entire period.
    The greatest increase will be the greatest change (delta). Calculated from above. 
    Use the change to identify the date and amount.
    
The greatest decrease in losses (date and amount) over the entire period.
    Same as above. 
    
Your resulting analysis should look similar to the following:

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
Your final script should print the analysis to the terminal and export a text file with the results.

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: ")
print(f"Total: $")
print(f"Average Change: $")
print(f"Greatest Increase in Profits:")
print(f"Greatest Decrease in Profits:")
'''''

from pathlib import Path
import csv

budget_csv = Path("../Resources/PyBank/PyBank.ipynb")

profitloss = []

line_num = 0

with open(budget_csv, 'r') as csvfile:
    
    print(type(csvfile))
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    print(type(csvreader))
    
    # header = next(csv_reader)
    # print(f"{header} <---- HEADER")

    for row in csv_reader:
        if line_num == 0:
            print(f'Column names are {", ".join(row)}')
            line_num += 1 
        else:
            print(f'\t{row[0]} the Profit/Loss was {row[1]}')
            line_num += 1
    print('Processed {line_num} lines.')
    
#         print(row)
#         profitloss = int(row[2])
#         profitloss.append(profitloss)