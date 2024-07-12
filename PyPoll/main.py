# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 00:47:50 2024

"""

#initialize the votes
total_votes = 0

first_line = True

#make a dictionary to store election results for each candidate
candidate_data = {
    'Charles Casper Stockham' : 0 ,
    'Diana DeGette' : 0,
    'Raymon Anthony Doane' : 0}

file = open('election_data.csv' , 'r')

for line in file:
    if first_line:
        first_line = False
        
    else:
        #print(line)
        total_votes += 1
        
        #locate the candidate name
        first = line.find(',')
        second = line.find(',', first + 1)
        
        candidate = line[(second +1):]
        #print(candidate)
        
        if ("\n") in candidate:
            candidate = candidate[:-1]
        
        candidate_data[candidate] += 1


file.close()



#Determine the election winner

highest_ballots = 0
winner_candidate = None

for candidate in candidate_data:
    ballots = candidate_data[candidate]
    
    if ballots > highest_ballots:
        highest_ballots = ballots
        winner_candidate = candidate
        
    

#make another dictionary to obtain the percentages

candidate_data_percent = {
    'Charles Casper Stockham' : 0 ,
    'Diana DeGette' : 0,
    'Raymon Anthony Doane' : 0}


for candidate in candidate_data:
    ballots = candidate_data[candidate]
    
    ballots_percent = 100*(ballots / total_votes)
    ballots_percent = round(ballots_percent , 3)
    
    candidate_data_percent[candidate] = ballots_percent
    
    

print('Election Results')
print('-----------------------------')
print(('Total Votes: ') + str(total_votes))
print('-----------------------------')
print(('Charles Casper Stockham: ') + str(candidate_data_percent['Charles Casper Stockham']) + '% ' + '(' + str(candidate_data['Charles Casper Stockham']) + ')')
print(('Diana DeGette: ') + str(candidate_data_percent['Diana DeGette']) + '% ' + '(' + str(candidate_data['Diana DeGette']) + ')')
print(('Raymon Anthony Doane: ') + str(candidate_data_percent['Raymon Anthony Doane']) + '% ' + '(' + str(candidate_data['Raymon Anthony Doane']) + ')')
print('-----------------------------')
print(('Winner: ') + str(winner_candidate))
print('-----------------------------')



#Now type it on a txt file

with open('election_results.txt' , 'w') as file:
    file.write('Election Results' + '\n')
    file.write('-----------------------------' + '\n')
    file.write(('Total Votes: ') + str(total_votes) + '\n')
    file.write('-----------------------------' + '\n')
    file.write(('Charles Casper Stockham: ') + str(candidate_data_percent['Charles Casper Stockham']) + '% ' + '(' + str(candidate_data['Charles Casper Stockham']) + ')' + '\n')
    file.write(('Diana DeGette: ') + str(candidate_data_percent['Diana DeGette']) + '% ' + '(' + str(candidate_data['Diana DeGette']) + ')' + '\n')
    file.write(('Raymon Anthony Doane: ') + str(candidate_data_percent['Raymon Anthony Doane']) + '% ' + '(' + str(candidate_data['Raymon Anthony Doane']) + ')' + '\n')
    file.write('-----------------------------' + '\n')
    file.write(('Winner: ') + str(winner_candidate) + '\n')
    file.write('-----------------------------' + '\n')
    
