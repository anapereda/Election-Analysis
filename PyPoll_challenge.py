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
file_to_load= '/Users/anitapereda/Documents/dataAnalytics/Election-Analysis/Resources/election_results.csv'
#create file to read
file_to_save= os.path.join("Analysis","election_analysis_challenge.txt")
#initialize the counter (total number of rows)
total_votes= 0

#crete a list of counties 
candidate_options= []
county_options= []

#create a dictionary where the county is the key and the votes cast for each county election
county_votes = {}
candidate_votes= { }
#create an empty list 

vote_percentage_ca= []
vote_percentage_co=[]

#variable declaration for the winning candidate
winning_candidate= ""
winning_count = 0 
winning_percentage= 0 

winning_county= ""
county_winning_count= 0
#open the election resuts and read the file 
with open(file_to_load) as election_data:
    #to do: reand and analyze the data hear
    #read the file object with the reader function
    file_reader= csv.reader(election_data)
    #print each row n the CSV file
    
    #read and print the headers row the 'next()' method will skip the first row
    headers= next(file_reader)
    
    for row in file_reader:
        total_votes += 1

       #check if the candidate does not match any existing candidate 
        county_name= row[1]
        #county count
        if county_name not in county_options:
            #Add the candidate name to the candidate list
            county_options.append(county_name)
            #begin tracking that candidate's vote count 
            county_votes[county_name]=0
        
        #add a vote to that candidate's count
        county_votes[county_name] += 1
        
        #candidate count
        candidate_name= row[2]
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count 
            candidate_votes[candidate_name]=0
        
        candidate_votes[candidate_name] += 1

    
    #open text file
    with open (file_to_save, "w") as txt_file:
        
        election_results= (f"Election Results\n" f"-----------------------\n" f"Total Votes: {total_votes:,}\n" f"-----------------------\n")
        txt_file.write(election_results)
        
        #county votes calculation and print statements 
        for county in county_votes: 
        #retrieve vote count of a candidate
            votes= county_votes[county]
                #calculate the percentage of votes
            vote_percentage_co= float(votes)/ float(total_votes) *100
    
            county_results= (f"{county}: {vote_percentage_co: .1f}% ({votes:,})\n" )
            txt_file.write(county_results)
        #print the candidate name and percentage of votes 
            if (votes > county_winning_count):
                winning_county= county

        winning_county_summary= (f"-----------------------\n" f"Largest County Turnout: {winning_county}\n" f"-----------------------\n")
        txt_file.write(winning_county_summary)

        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            vote_percentage= float(votes)/ float(total_votes)*100

            candidate_results= (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n" )
            txt_file.write(candidate_results)

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage= vote_percentage
                winning_candidate= candidate


        winning_candidate_summary= (f"----------------------\n"f"Winner: {winning_candidate}\n" 
            f"Winning Vote Count: {winning_count:,} \n" f"Winning Percentage: {winning_percentage: .1f}%\n"
            f"----------------------\n")

        txt_file.write(winning_candidate_summary)