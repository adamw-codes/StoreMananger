# StoreManager

StoreManager is a python script that auto-refreshes items on a user's Depop account and then goes into an outreach part where it auto-likes items searched out of a randomized keyword set. Can like up to 750 posts a day.

This script is meant to be self-running. This means that a lot of the assumptions and parameters have already been set. If you would like to make adjustments to the run, please see "Usage".

## Installation

Download the zip.
Extract to Desktop.
Run through the batch file. (I have used this with a task scheduler that opens the batch file)

## Dependent Libraries

The script is not packaged with a software tool. 
You must have these dependencies:
 - python
 - selenium
 - chromedriver 

## Usage

Make sure you update the 'credentials.py' file with your proper username and password before running.

Search keywords are assigned by default; however, the keywords can be manually changed by going to 'depopmanager.py' and changing the array in line *****.
