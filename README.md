# WebStoreManager

StoreManager is a python script that auto-refreshes items on a user's D3p0p account and then goes into an outreach part where it auto-interacts with items searched out of a randomized keyword set. Can interact with up to 750 posts a day.

This script is meant to be self-running. This means that a lot of the assumptions and parameters have already been set. If you would like to change up the keyword set, please see "Usage".

## Installation

Download the zip.
Extract to Desktop.
Run with the batch file (store_manager_run.py). (I have used this with a task scheduler that opens the batch file)

## Dependent Libraries

The script is not packaged with a software tool. 
You must have these dependencies:
 - python
 - selenium
 - chromedriver 

## Usage

Make sure you update the 'credentials.py' file with your proper username and password before running.

Search keywords are assigned by default; however, the keywords can be manually changed by going to 'webstoremanager.py' and changing the array in line 119.
