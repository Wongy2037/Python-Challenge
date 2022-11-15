#Create a Python script that analyzes the PyBank records to calculate the result

#Import dependencies
import csv
import os

# collect data from the Resources
file = os.path.join( "Resources", "budget_data.csv")
# Open and read the data from the CSV file
with open(file, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',') 
    #create a hearder 
    header=next(csvreader)
   # Define variables
    month = []
    profit = []
    profit_change = []
                    
    #search through the values and add them to the empty list 
    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])
                      
#evaluate the max and min from the list
gain = max(profit_change)
loss = min(profit_change)

#using the index
highest_Month_Profit = profit_change.index(max(profit_change))+1
lowest_Month_Profit = profit_change.index(min(profit_change))+1

#Print the outcome 
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {month[highest_Month_Profit]} (${(str(gain))})")
print(f"Greatest Decrease in Profits: {month[lowest_Month_Profit]} (${(str(loss))})")      

#Export a text file with the results
output = os.path.join("analysis", "output.txt")
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month[highest_Month_Profit]} (${(str(gain))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month[lowest_Month_Profit]} (${(str(loss))})")