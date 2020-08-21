# Python

## Background

In this homework assignment, I'll be using the concepts I've learned to complete the **two** Python Challenges, PyBank and PyPoll.

Both of these challenges encompasses a real-world situation where my newfound Python scripting skills can come in handy.

### Setup

* I created a new repository for this project called `python-challenge`.

* I clone the new repository to my computer.

* Inside my local git repository, create a directory for both of the Python Challenges. Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.

* Inside of each folder that I created, I added the following:

  * A new file called `main.py`. This will be the main script to run for each analysis.
  * A "Resources" folder that contains the CSV files you used. Make sure your script has the correct path to the CSV file.
  * An "analysis" folder that contains your text file that has the results from your analysis.

* I then pushed the above changes to GitHub or GitLab.

## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, I was tasked with creating a Python script for analyzing the financial records of a company. I was given a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`.

* My task was to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period


* My final script printed both the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, I was tasked with helping a small, rural town modernize its vote counting process.

* I was given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. My task was to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* My final script printed both the analysis to the terminal and export a text file with the results.
