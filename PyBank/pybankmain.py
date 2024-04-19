import os
import csv

#set variables
total_months = 0
total_net_profit= 0 # total
prior_profit_loss = 0
profit_change = 0  #net change
greatest_increase = ["", 0]
greatest_decrease = ["", 0]  
change_list = []



csvpath = os.path.join("python-challenge\PyBank\Resources","budget_data.csv")

with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile,delimiter=",")
   headers = next(csvreader) 


   for row in csvreader:

#calculate total months  
        total_months += 1
        # print(f"total months: {total_months}")
        
# calculate total profit/loss       
        total_net_profit += int(row[1]) #+ profit_loss  # Total Profit loss
        print (total_net_profit)

# #Calculate greatest increase, greatest decrease and prior profit loss
        
        if prior_profit_loss != 0:
            profit_change = int(row[1]) - prior_profit_loss
            change_list.append(profit_change)
    
        prior_profit_loss = int(row[1])
            
        if profit_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase [1] = profit_change
            
        elif profit_change < greatest_decrease[1]:
            greatest_decrease [0] = row[0]
            greatest_decrease [1] = profit_change

            prior_profit_loss = int(row[1])
            profit_change = profit_change + prior_profit_loss    

#Calculate average change
avg_change = (sum(change_list) / len(change_list))
print(change_list)


print(f"Financial Analysis\n")

#Print dashes
print("----------------\n")

# Print total months
print(f"Total Months: {total_months}\n")

# Print total net profit
print (f"Total: ${total_net_profit}\n")

#print greatest change
print(f"Greatest Change: ${round(avg_change,2)}\n")

#Print greatedst increase
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")

#print greatest decrease
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#Print to output file
output_file_path_2 = os.path.join("python-challenge\PyBank\Analysis","pybankoutput.txt")

#open to file as a writeable and write the output into thefile
with open(output_file_path_2,"w") as output_file:
    output_file.write(f"Financial Analysis\n")
    output_file.write("----------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_net_profit}\n")
    output_file.write(f"Greatest Change: ${round(avg_change,2)}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")