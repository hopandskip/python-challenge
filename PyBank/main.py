#Establish dependencies
import os
import csv

#Import the file
pybank_path = os.path.join("Resources","budget_data.csv")

#create the variables
date = []
profit_loss = []
change_in_profit_loss = []

with open (pybank_path, newline ="") as pybank_data:
    pybank_reader =csv.reader(pybank_data, delimiter=",")
    next(pybank_reader) #skip the header row
    for row in pybank_reader:
        #Put the data into a list 
        date.append(row[0])
        profit_loss.append(int(row[1]))

    for i in range(1,len(profit_loss)):
        #Find the change in profit/loss between consecutive months and store in a list
        change_in_profit_loss.append(int(profit_loss[i]) - int(profit_loss[i-1]))
        #Get the max profit
        max_profit = max(change_in_profit_loss)
        #Get the max loss
        max_loss = min(change_in_profit_loss)
        #Get the month with the max profit
        max_profit_loss_date = str(date[change_in_profit_loss.index(max(change_in_profit_loss))+1])
        #Get the month with the max loss
        min_profit_loss_date = str(date[change_in_profit_loss.index(min(change_in_profit_loss))+1])


print ("Financial Analysis")
print ("----------------------------")
#Get the total number of months
print (f"Total Months: {len(date)}")
#Get the sum of the profit and losses
print (f"Total: ${sum(profit_loss)}")
#Get average of the changes in "Profit/Losses" over the entire period
average_change = sum(change_in_profit_loss) / (len(date) -1)
print (f"Average change: ${average_change:.2f}")
print (f"Greatest Increase in Profits: {max_profit_loss_date} ${max_profit}")
print (f"Greatest Decrease in Profits: {min_profit_loss_date} ${max_loss}")

print ("Financial Analysis", file=open("PyBank.txt", "a"))
print ("----------------------------", file=open("PyBank.txt", "a"))
#Get the total number of months
print (f"Total Months: {len(date)}", file=open("PyBank.txt", "a"))
#Get the sum of the profit and losses
print (f"Total: ${sum(profit_loss)}", file=open("PyBank.txt", "a"))
#Get average of the changes in "Profit/Losses" over the entire period
average_change = sum(change_in_profit_loss) / (len(date) -1)
print (f"Average change: ${average_change:.2f}", file=open("PyBank.txt", "a"))
print (f"Greatest Increase in Profits: {max_profit_loss_date} ${max_profit}", file=open("PyBank.txt", "a"))
print (f"Greatest Decrease in Profits: {min_profit_loss_date} ${max_loss}", file=open("PyBank.txt", "a"))


