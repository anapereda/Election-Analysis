#Pseudo-code
#Obtain data to retrieve
#Calculate the total number of voters cast (group by cast and sum)
#complete a list of candidates who received votes
#percetage of votes each candidate won
#total number of votes each candidate won
#winner of the election based on pupular vote
import csv
import os

#create file to load
file_to_load= '/Users/anitapereda/Documents/Data Analytics boot camp/Election-Analysis/Resources/election_results.csv'
#create file to read
file_to_save= os.path.join("Analysis", "election_analysis.txt")

#open the election resuts and read the file 
with open(file_to_load) as election_data:
    #to do: reand and analyze the data hear
    #read the file object with the reader function
    file_reader= csv.reader(election_data)
    #print each row n the CSV file
    
    #read and print the headers row the 'next()' method will skip the first row
    headers= next(file_reader)
    print(headers)
    
    
    for row in file_reader:
        print(next(row))
#create a file to write your results





