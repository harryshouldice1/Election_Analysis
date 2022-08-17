# Election_Analysis

## Overview of Election Audit
We were given data from an election in Colorado through a csv file.  I created code to take the data from that file and find the total votes, which county had the highest turnout, how many votes each candidate received, and the winning candidate.  Looking at thousands of lines of data is nearly impossible.  With this code, that problem is eliminated by having the file read through Python.  All the data was read without having to personally go through it line by line.

## Election-Audit Results
### Total Votes in Colorado - 369,711

### County Votes
* Denver - 82.2% (306,055)
* Jefferson - 10.5% (38,855)
* Arapaheo - 6.7% (24,801)

### Highest Turnout- Denver (306,055 votes)

### Breakdown
* Diana DeGette - 73.8% (272,892)
* Charles Casper Stockham - 23.0% (85,213)
* Raymon Anthony Doane - 3.1% (11,606)

### The Winner
* Diana DeGette
* Vote Count - 272,892 votes
* Percentage of Votes - 73.8%

## Election-Audit Summary
Using this code, tallying the results of elections becomes easier than ever.  This code can be used for any county and any candidate.  All that is needed is the raw data from the election.  The code does need to be edited to fit the file name for the raw data from a given election. Specifically, line #9 needs to match the name of the csv file.  Depending on how the user wants the data to be stored in the new file, line 48 and line 51 can be changed to match the preferences of the user. 
![Screenshot (15)](https://user-images.githubusercontent.com/109995136/185250100-ea05faf4-7dcb-477c-b052-369a91a233bf.png)
