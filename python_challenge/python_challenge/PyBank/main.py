#this is a file for the python_challenge for PyBank - main.py - Randy Dettmer

import os
import csv

#path to collect data from the resources folder - location on your computer may vary
budgetdata = os.path.join('..', "Resources" , 'budget_data.csv')

#read in the csv file     
with open(budgetdata, 'r') as csvfile:
    
    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    total_amount = 0 #set variable
    data = [] #raw profit/loss data
    adata = [] #raw profit/loss data to be used to calculate average change 
     
    header = next(csvreader) #skips header row
    for row in csvreader:
           total_amount += int(row[1]) #calculate total amount
           data.append(row[1]) #adding data to a new array
           adata.append(row[1])

#converting arrays from str to int
for i in range(0, len(data)): 
    data[i] = int(data[i])
for j in range(0, len(adata)): 
    adata[j] = int(adata[j])    
    
month_count = len(data) #determines number of months
profit = max(data) #determines maximum value of profit/loss
loss = min(data) #determines miniumn value of profit/loss

adata.insert(0,0) #adjust second array for moving average
adata.pop(-1) #adjust second array for moving average
avg_change = 0 #set variable

#source code from Stack Overflow "How to subtract two lists in python [duplicate]
for x in range(min(len(data), len(adata))):
    avg_change = data[x] - adata[x] + avg_change
    
#determine average changes over period, one is subtacted from month total to account adjusted to two decimal points   
total_var_avg = round((avg_change - data[0])/(month_count-1),2)  

#determine indicies for greatest profit and greatest loss
pindex = data.index(profit)
lindex = data.index(loss)

#run another loop to get the greatest values            
with open(budgetdata, 'r') as csvfile:
    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    counter = 0   
    header = next(csvreader) #skips header row
    for row in csvreader:
           if counter == pindex: #matching indexes for highest profit          
               pwin = row
           if counter == lindex: #matching indexes for highest loss
               ploss = row
           counter += 1    

print("Financial Analysis")
print("------------------------------------")
print("Total Months: ", str(month_count)) #check print - ok
print("Total: $", str(total_amount)) #check print - ok
print(f"Average Change: $ {total_var_avg}") #check print - ok?
print("Greatest Increase in profits :", str(pwin)) #print check
print("Greatest Decrease in profits :", str(ploss)) #print check

#specify the file to write to - may need to use an absolute path
output_path = os.path.join("new.csv") # - ok

#open the file using write mode - ok
with open(output_path, 'w', newline='') as csvfile:
    #initialize csv writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    #write the first row - column headers
    csvwriter.writerow(['Total Months:','Total:','Average Change:','Greatest Increase in Profits','Greatest Decrease in Profits'])
    #write the second row
    csvwriter.writerow([month_count, total_amount, total_var_avg, pwin, ploss])
