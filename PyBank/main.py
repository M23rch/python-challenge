# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:55:15 2024

"""

#Open the file

file = open('budget_data.csv' , 'r')

#Initialize the profits and months count
total_profit = 0
months = 0
first_line = True

#initialize the greatest increase and decrease
greatest_increase = -99999999999
greatest_decrease = 9999999999

greatest_increase_month = None
greatest_decrease_month = None

previous_profit = 0

change_list = []

for line in file:
    #disregard the first line
    if first_line:
        first_line = False
        
    else:
        #add +1 month
        months += 1
        
        income = int(line[7:])
        
        change = (income - previous_profit)
        
        change_list.append(change)
      
        
        if change > greatest_increase:
            greatest_increase_month = str(line[0:6])
            greatest_increase = change
            
        if change < greatest_decrease:
            greatest_decrease_month = str(line[0:6])
            greatest_decrease = change
            
            
        #add the income to the total profit
        total_profit += income
        
        #update previous balance
        previous_profit = income
        
        
        
        
    
    
file.close()

change_list = change_list[1:]

#calculate the average change
average_change = sum(change_list) / len(change_list)
average_change = round(average_change, 2)



print('Financial Analysis')
print('----------------------------')
print(('Total Months: ') + str(months))
print(('Total: $') + str(total_profit))
print(('Average Change: $') + str(average_change))
print(('Greatest Increase in Profits: ') + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
print(('Greatest Decrease in Profits: ') + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")



#Now write it on a txt file

with open('financial_analysis.txt' , 'w') as file:
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write(('Total Months: ') + str(months) + "\n")
    file.write(('Total: $') + str(total_profit) + "\n")
    file.write(('Average Change: $') + str(average_change) + "\n")
    file.write(('Greatest Increase in Profits: ') + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")"  + "\n")
    file.write(('Greatest Decrease in Profits: ') + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")"  + "\n")

