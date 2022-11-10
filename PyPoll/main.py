
#Import the os module
import os
#Import module to read csv files
import collections as ct

#Clear terminal screen
os.system('cls')

#Indicates file to open
vote_csv = os.path.join('C:/Users/vosta/OneDrive/Documents/GitHub/python-challenge/PyPoll/election_data.csv')

totvote = []

#Read the file as text
with open(vote_csv) as f:

    votes = ct.Counter()

    header = next(f)
    
    for row in f:
        candidate = row.split(",")[-1].strip()
        votes[candidate] +=1
        totvote.append(row[0])

    

    #print header of analysis
    print("Election Results")
    print("-------------------------")

    #Len(fecha) counts the # of items in dictionary
    print("Total Votes: ", len(totvote))
    print("-------------------------")
    print("Diana DeGette            ", votes['Diana DeGette'], "   ", round(float(votes['Diana DeGette']/len(totvote)*100),2), "%" )
    print('Charles Casper Stockham  ', votes['Charles Casper Stockham'], "    ", round(float(votes['Charles Casper Stockham']/len(totvote)*100),2), "%" )
    print('Raymon Anthony Doane     ', votes['Raymon Anthony Doane'], "     ", round(float(votes['Raymon Anthony Doane']/len(totvote)*100),2), "%")
    print("-------------------------")
    print("Winner:  ", votes.most_common(1))

    #Export a text file with the results
    output_path = os.path.join('analysis.txt')

    #Write to the txt file line by line the results. \n it's use to write a blank line
    #Converting numeric data to string is required
    with open(output_path, 'w') as f:
        f.write("Election Results")
        f.write('\n')
        f.write("-------------------------")
        f.write('\n')
        f.writelines("Total Votes: " + str(len(totvote)))
        f.write('\n')
        f.writelines("-------------------------")
        f.write('\n')
        f.writelines("Diana DeGette            " + str(votes['Diana DeGette']) + "   " + str(round(float(votes['Diana DeGette']/len(totvote)*100),2)) + "%" )
        f.write('\n')
        f.writelines('Charles Casper Stockham  ' + str(votes['Charles Casper Stockham']) + "    " + str(round(float(votes['Charles Casper Stockham']/len(totvote)*100),2)) + "%" )
        f.write('\n')
        f.writelines('Raymon Anthony Doane     ' + str(votes['Raymon Anthony Doane']) + "     " + str(round(float(votes['Raymon Anthony Doane']/len(totvote)*100),2)) + "%")
        f.write('\n')
        f.writelines("-------------------------")
        f.write('\n')
        f.writelines("Winner:  " + str(votes.most_common(1)))
        
              
  
    