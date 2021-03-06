# Election_Analysis
## Project Overview
The results of a local Colorado congressional election need to be audited, and the Board of Elections has asked you to deliver the following information:
1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

Later the election commision requested additional data to complete the audit:

6. Voter turnout for each county
7. Percentage of votes from each vounty out of the total count
8. County with the highest turnout

## Resources
- DataSource: election_results.csv (![Link](/Resources/election_results.csv))
- Software: Python 3.8.8, Visual Studio Code 1.61.2

## Results
The election audit with determined the following:
- A total of 369,711 votes were cast
- A break down of the counties who voted:
  - Jefferson County represented 10.5% of the vote with 38,855 voters
  - Denver County represented 82.8% of the vote with 306,055 voters
  - Arapahoe County represented 6.7% of the vote with 24,801 voters
- The county with largest number of votes was:
  -  Denver County with 306,055 voters representing 82.8% of votes cast
- A break down of the candidates who received votes:
  - Charles Casper Stockham, received 23.0% of the vote with 85,213 votes
  - Diana DeGette, received 73.8% of the vote with 272,892 votes
  - Raymon Anthony Doane, received 3.1% of the vote with 11,606 votes
- The winner of the election based on popular vote was:
  - Diana DeGette with 272,892 votes and 73.8% of the vote

## Summary

This python script is relatively flexible and can account for any number of candidates. When the analysis code is run, the results are output to the terminal (shown below) and to a text file (![Link](/Analysis/election_analysis.txt)).

![TerminalOutput.png](/Analysis/TerminalOutput.png)

These outputs are simple and this code could be modified to audit other elections. Without modifying the code at all, this could be used for gubernatorial elections in addition to congressional elections. By replacing all instances of "county" and replacing them with "state", this code could be used for auditing the popular vote of presidential elections. Alternatively, this code could be used to audit the results for a statewide referendum by replacing the names of candidates with their referendum choice (e.g. "Yes", "No", etc.). This code could even be used for school president with county being switched to school year/graduating class or for things outside voting like for a survey of popular opinions. The code can be easily manipulated to serve a wide variety of purposes.
