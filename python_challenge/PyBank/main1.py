#this is a new file for the python_challenge for PyBank - main1a.py

import os
import csv

#path to collect data from the resources folder - may need to use an absolute path
budgetdata = os.path.join('..', "Resources" , 'budget_data.csv')


#read in the csv file
with open(budgetdata, 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    data = [] # set empty list
    month_count = 0 #set variable - ok
    profit = 0 #set variable
    loss = 0 #set variable
    
    #header = next(csvreader) #skips header row - don't use here
    for row in csvreader:
                
        data = [list(row) for row in csvreader]
        
        month_count = len(data) #determines number of months - ok
        #profit = max(data) #determines max profit
        #loss = min(data) #determines max loss
        #print(data)
        
with open(budgetdata, 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    total_amount = 0 #set variable - ok      
    header = next(csvreader) #skips header row
    for row in csvreader:
           total_amount += int(row[1]) #calculate total amount - ok
           profit = max(data) #determines max profit
           loss = min(data) #determines max loss
         
#average of changes in profit/losses
avg_change = (total_amount/month_count) #ok ?


print("Total Months: ", str(month_count)) #check print - ok
print("Total: ", str(total_amount)) #check print - ok
print("Average Change: $", str(avg_change)) #check print - ok?
print("Greatest Increase in profits :", str(profit)) #print check
print("Greatest Decrease in profits :", str(loss)) #print check



#specify the file to write to - may need to use an absolute path
#output_path = os.path.join("..","output", "new.csv")

#open the file using write mode
#with open(output_path, 'w', newline='') as csvfile:
    #initialize csv writer
    #csvwriter = csv.writer(csvfile, delimiter=',')
    #write the first row - column headers
    #csvwriter.writerow(['Total Months:','Total:','Average Change:','Greatest Increase in Profits','Greatest Decrease in Profits'])
    #write the second row
    #csvwriter.writerow([total_months, total_pl, total_change, great_totalp, great_totald])
