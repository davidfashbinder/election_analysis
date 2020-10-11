# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources

- Data Source: election_results.csv
- Software: Python 3.9, Visual Studio Code 1.5.0

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
 - The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
  - Diana DeGette received 73.8% of the vote and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
- The winner of the election was:
  - Diana Degette who received 73.8% of the vote and 272,892 votes
  
 ## Challenge Overview
 The challenge asked me to audit the data and provide further insight into the voting results from the election.  Specifically:
 
 1. Votes by County.
 2. Percentage of Votes by County.
 3. County with the largest number of votes.
 
 There are 3 counties in this precinct: Arapahoe, Denver, and Jefferson.
 
 This data was added to the Python script from the project, in order to produce a more robust election analysis.
 
 ## Election Audit Results
 - Total votes cast in this congressional election: 369,711
 
 ![Total Votes Code](https://github.com/davidfashbinder/election_analysis/blob/main/total_votes.png?raw=true)
 
 - Votes and Vote Percentage by County in the Precinct
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
  
 ![Votes by County](https://github.com/davidfashbinder/election_analysis/blob/main/county_votes_code.png?raw=true)
 ![Votes by County Percentage](https://github.com/davidfashbinder/election_analysis/blob/main/county_votes_percent_code.png?raw=true)
 
 - County with the largest number of votes: Denver (306,055)
 
 ![Largest_County](https://github.com/davidfashbinder/election_analysis/blob/main/largest_county_code.png?raw=true)
 
 - The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
  - Diana DeGette received 73.8% of the vote and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
  
 ![Votes_by_Candidate](https://github.com/davidfashbinder/election_analysis/blob/main/candidate_votes_code.png?raw=true)
 ![Votes by Candidate Percentage](https://github.com/davidfashbinder/election_analysis/blob/main/candidate_votes_percent_code.png?raw=true)
  
- The winner of the election was:
  - Diana Degette who received 73.8% of the vote and 272,892 votes
  
 ![Winning Candidate Summary](https://github.com/davidfashbinder/election_analysis/blob/main/winning_candidate_code.png?raw=true)
 
 ## Challenge Summary 
This code can be used by your election commission for any election - of any type.  Since we are sourcing our data from a CSV file of the results, we can create lists for any candidates.  We can also create dictionaries that deep-dive into any breakdown of the voting district in question:
  - States
  - Cities
  - School Districts
  - And more
You can also print data not related to the winning candidate, if you wish to explore a specific candidate and how they fared in a specific part of the voting district.  
