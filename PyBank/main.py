import csv
import os
 # Assignt our variables
budget_data = os.path.join("Resources","budget_data.csv")
total_months = 0
change_in_months = []
net_change_list = []
total_net = 0
greatest_increase = ["", 0]
greatest_decrease = ["", float(9999999999999999999)]
with open (budget_data) as py_bank:
    reader= csv.reader(py_bank)
    header = next(reader)
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    for financial_analysis in reader:
       total_months +=1
       total_net += int(financial_analysis[1])
       net_change = int(financial_analysis[1]) - previous_net
       net_change_list += [net_change]
       if net_change > greatest_increase[1]:
           greatest_increase[0] = financial_analysis[0]
           greatest_increase[1] = net_change
       if net_change < greatest_decrease[1]:
           greatest_decrease[0] = financial_analysis[0]
           greatest_increase[1] = net_change
       if len(net_change_list) > 0 :
          average_change = sum(net_change_list) / len(net_change_list)
       else:
           average_change = 0
print("Financial Analysis")
print("-------------------------------------------------------------------------")
# Calculate total months
print(f"Total Months: {total_months}")
# Calculate total profit loss
print(f"Total: ${total_net}")
# Calculate the changes
print(f"Average Change: ${average_change:.2f}")
# Calculate the greatest increase in profits
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
# Calculate the greatest increase in profits
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
