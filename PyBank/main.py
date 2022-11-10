
#Import the os module
import os
#Import module to read csv files
import csv

#Indicates file to open
budget_csv = os.path.join('PyBank/Resources/budget_data.csv')

#Read the csv
with open(budget_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #The file has column names. This skips this row 
    next(csvreader)
    
    #defining dictionaries
    fecha = []
    profit = []
    change = []

    #Separated csv data into dictionaries and change string value to float
    for row in csvreader:
        profit.append(float(row[1]))
        fecha.append(row[0])
    
    #print header of analysis
    print("Financial Analysis")
    print("-------------------------")

    #Len(fecha) counts the # of items in dictionary
    print("Total Months:         ", len(fecha))
    
    #sum(profit) totals the profit/revenue
    print("Total Profit/Loses:  $", round(sum(profit)))

    #for loop to go through the profit dictionary
    for x in range(1,len(profit)):

        #Calculates change in profit between current and previous value
        change.append(profit[x] - profit[x-1])
        #Calculates the average change in profit
        avg_change = sum(change) / len(change)
        #Calculates the greatest increase in profit
        max_change = max(change)
        #Calculates the greatest decrease in profit
        min_change = min(change)
        #Finds the date for the greates increase
        max_change_date = str(fecha[change.index(max(change))+1])
        #Finds the date for the greates decrease
        min_change_date = str(fecha[change.index(min(change))+1])

    #Prints the rest of the analysis
    print("Average Change:      $", round(avg_change))
    print("Greatest Increase in Profit:", max_change_date,"($", round(max_change),")")
    print("Greatest Decrease in Profit:", min_change_date,"($", round(min_change),")")

    #Export a text file with the results
    output_path = os.path.join('PyBank/analysis/analysis.txt')

    #Write to the txt file line by line the results. \n it's use to write a blank line
    #Converting numeric data to string is required
    with open(output_path, 'w') as f:
        f.write("Financial Analysis")
        f.write('\n')
        f.write("-------------------------")
        f.write('\n')
        f.write("Total Months:          ")
        f.write(str(len(fecha))) 
        f.write('\n')
        f.write("Total Profit/Loses:  $ ")
        f.write(str(round(sum(profit))))
        f.write('\n')
        f.write("Average Change:      $ ")
        f.write(str(round(avg_change,2)))
        f.write('\n')
        f.write("Greatest Increase in Profit: ") 
        f.write(max_change_date)
        f.write("  $ ")
        f.write(str(round(max_change)))
        f.write('\n')
        f.write("Greatest Decrease in Profit: ")
        f.write(min_change_date)
        f.write("  $ ")
        f.write(str(round(min_change)))
              
 