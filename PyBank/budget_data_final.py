# import csv module
import csv

# set path for file
csvpath_in = "PyBank/Resources/budget_data.csv"

# set variables
header = []
total_months = 0
current_month_profit_loss = 0
previous_month_profit_loss = 0
total_profit_losses = 0
total_change = 0
changes = []
average_change = 0

# set variables for calc greatest increase in profits
greatest_increase = 0
greatest_increase_month = str()

# set variables for calc greatest decrease in profits
greatest_decrease = 0
greatest_decrease_month = str()

# open csv file and read it
with open(csvpath_in, 'r') as csvfile:
    
    # store contents of the csv file into csvreader
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header row
    header = next(csvreader)

    # loop through each row
    for row in csvreader:

        # count the number of rows
        total_months += 1

        # store current month value
        current_month_profit_loss = int(row[1])
        
        # add up each month to calculate total profit loss
        total_profit_losses += current_month_profit_loss

        # store month for greatest increase in profits
        month = row[0]
        
        # initiate IF on second run
        if total_months > 1:

            # calculate change from month to month
            change = current_month_profit_loss - previous_month_profit_loss

            # add change calc from above to changes list
            changes.append(change)

            # sum all changes and stores in total change
            total_change += change

            # checking for greatest increase in profits
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = month

            # checking for greatest increase in profits
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = month

        # overwrite previous month profit loss
        previous_month_profit_loss = current_month_profit_loss

# test print total_months and total_profit_losses to terminal
print(total_months)
print(total_profit_losses)

# calc avg change
average_change = total_change / len(changes)
# test print average_average to terminal
print(f'${average_change:.2f}')

# test print greatest inc and dec month and values to terminal
print((greatest_increase_month),(f'${greatest_increase}'))
print((greatest_decrease_month),(f'${greatest_decrease}'))

out_file_path = "PyBank/Analysis/budget_data_analysis.txt"

with open(out_file_path, 'w') as analysis:
    analysis.write('Financial Analysis\n'
                    '-----------------------------------\n'
                    f'Total Months: {total_months}\n'
                    f'Total: ${total_profit_losses}\n'
                    f'Average Change: ${average_change:.2f}\n'
                    f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n'
                    f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')