import os
import csv
file_load = os.path.join("..","bowenya","python-challenge","PyBank","budget_data.csv")
file_output = os.path.join("..","bowenya","python-challenge","PyBank","financial_analysis.txt")

monthcount = 0
total = 0
prevdata = 0
change = 0
change_l = []
maxinc = ["",0]
maxdec = ["",999999999]
avgchange = 0

with open(csvpath, newline='') as budgetdata:
    reader = csv.reader(budgetdata, delimiter=",")
    header = next(budgetdata)
    for row in reader:
        monthcount += 1
        total += int(row[1])
        change = int(row[1]) - prevdata
        prevdata = int(row[1])
        change_l = change_l + [change]
        if change > int(maxinc[1]):
            maxinc = [row[0],row[1]]
        elif change < int(maxdec[1]):
            maxdec = [row[0],row[1]]

change_l.pop(0)
avgchange = round(sum(change_l)/len(change_l),2)

output = (
          "\nFinancial Analysis\n"
          "-------------------------------------\n"
          f"Total Months: {monthcount}\n"
          f"Total: ${total}\n"
          f"Average Change: ${avgchange}\n"
          f"Greatest Increase In Profits: {maxinc[0]} (${maxinc[1]})\n"
          f"Greatest Decrease in Profits: {maxdec[0]} (${maxdec[1]})\n")

print(output)

with open(file_output, 'w') as txt_file:
    txt_file.write(output)
