# Import dependencies for file i/o and csv files and use of nan in mean, min and max functions
import os
import csv
import numpy as np

# Set up lists to store data
# Lists for months collected, profit/loss amount, change in profit/loss
# Create path to budget data file in Resources folder
months = []
pl_amount = []
pl_change = []

# Set up index for keeping track of place in data
# Initialised to -1 as it is incremented with eah new row from csv file
# Hence first row of file sets index to 0
index = -1

# Initialise total months to 0
total_months = 0

# Initialise net total amount of profit/loss to 0
net_total = 0

# Create path to CSV input file
csvpath = os.path.join("Resources", "budget_data.csv")

# Read CSV file in using with open
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first of Date and Profit/Losses
    csv_header = next(csvreader)

    # Read each row of budget data after the header
    # Each row is a two element list
    # row[0] is the month
    # row[1] is the amount of profit/loss in that month
    for row in csvreader:
        
        # Increment data index by 1
        index = index + 1
        
        # Increment total months by 1
        # Assumes there are no gaps or errors in data!
        # Would need to be checked for and validated in more strict, real world scenarios
        total_months = total_months + 1
        
        # Append the month in row[0] to the list of months
        months.append(row[0])
        
        # Cast current amount of profit/loss to the integer value of row[1]
        current_amount = int(row[1])
        
        # Append the current amount to the list of profit/loss amounts
        pl_amount.append(current_amount)
            
        # Update net total mount of profit/loss with current amount
        # Net total equals its current value plus the current amount of profift/loss
        # A loss will be a negative number added to the current total i.e. subtraction
        net_total = net_total + current_amount
             
        # If this is the first row of the file the net change has no data to compare with
        # Hence no real meaning
        # Set to nan aka not a number using numpy module
        if (index == 0):
            net_change = np.nan
            
        # Otherwise in all other rows
        # Net change equals the current amount minus the value of the last amount stored
        # Stored in index-1 of current place in list
        else:
            net_change = current_amount - pl_amount[index-1]
            
        # Append the net change to its list
        pl_change.append(net_change)
        
# Print financial analysis to screen
# Print out text labels and dashes
print("Financial Analysis")
print("------------------------------------------")

# Print out total months
print(f"Total Months: {total_months}")

# Print out the net total of all profit/loss values
print(f"Total: ${net_total}")

# Print out the average change in profit/loss using pl_change list
# Need to use numpy's nanmean to avoid first value in list i.e. pl_change[0] being nan
# nanmean discards this value from the calculation of the mean
# Will be a floating point value
# Round to two decimal places as is referencing money
print(f"Average Change: ${round(np.nanmean(pl_change),2)}")

# Find index of where greatest increase in profits occurs in pl_change list i.e. maximum value
# Must use numpy's nanargmax to avoid nan value in pl_change[0]
index_of_max = np.nanargmax(pl_change)

# Find index of where greatest increase in profits occurs in pl_change list i.e. minimum value
# Must use numpy's nanargmin to avoid nan value in pl_change[0]
index_of_min = np.nanargmin(pl_change)

# Use index to find month in which maximum and minimum values occur from the list months
# Print these out to screen along with the values of the maximum and minimum
# Cast to integer to avoid decimal point
# All values are whole dollar in profit/loss so no need for decimal point
print(f"Greatest Increase in Profits: {months[index_of_max]} (${int(np.nanmax(pl_change))})")
print(f"Greatest Decrease in Profits: {months[index_of_min]} (${int(np.nanmin(pl_change))})")       

# Set variable for text output file named "analysis.txt" in folder analysis
output_file = os.path.join("analysis","analysis.txt")

# Open the output file
# Need to append newlines to each line to have correctly formatted output
with open(output_file, "w") as outfile:

    # Print out text labels and dashes to output file
    outfile.write("Financial Analysis\n")
    outfile.write("------------------------------------------\n")

    # Print out total months to output file
    outfile.write(f"Total Months: {total_months}\n")

    # Print out the net total of all profit/loss values to output file
    outfile.write(f"Total: ${net_total}\n")

    # Print out the average change in profit/loss using pl_change list
    outfile.write(f"Average Change: ${round(np.nanmean(pl_change),2)}\n")

    # Already found indexes of maxiumum and minimum values and stored in variables
    # Hence no need to repeat code from above

    # Print out months of maximum and minium change in in proft/loss and their values to output file
    outfile.write(f"Greatest Increase in Profits: {months[index_of_max]} (${int(np.nanmax(pl_change))})\n")
    outfile.write(f"Greatest Decrease in Profits: {months[index_of_min]} (${int(np.nanmin(pl_change))})\n")

