# WebStoreManager

StoreManager is a python script that auto-refreshes items on a user's D3p0p account and then goes into an outreach part where it auto-interacts with items searched out of a randomized keyword set. Can interact with up to 750 posts a day.

This script is meant to be self-running. This means that a lot of the assumptions and parameters have already been set. If you would like to change up the keyword set, please see "Usage".

## Installation

 - Download the zip.
 - Extract to Desktop.
 - Set up batch file with file location of python.exe and file location of webstoremanager.py.
 - Make sure credentials.py and webstoremanager.py are in the same folder.
 - Run with batch file.

## Dependent Libraries

The script is not packaged with a software tool. 
You must have these dependencies:
 - python
 - selenium
 - chromedriver 

## Usage

Make sure you update the 'credentials.py' file with your proper username and password before running.

Search keywords are assigned by default; however, the keywords can be manually changed by going to 'webstoremanager.py' and changing the array in line 119.

## Contributing

This was a script I made to help me refresh the tons of items I put on the shop and then turned into a bigger project than that. 

Please message me before many any pull requests or contributing. Thanks <3
