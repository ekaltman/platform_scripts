# This program retrieves data on a specific item and prints in in a .txt file

import gdata.docs.service
import gspread
import codecs
import sys
from getpass import getpass
from platform import Platform

username = raw_input('Enter Google User Name: ')
passwd = getpass('Enter password: ')

print 'authenticating with google...'
# Authenticate using your Google Docs email address and password.
client = gspread.login(username + '@gmail.com', passwd)

# Query the server for the spreadsheet and worksheet
worksheet = client.open("Untitled spreadsheet").sheet1

print 'organizing worksheet...'
# For the worksheet
countcategories = 1 

platformList = []
for x in worksheet.col_values(1):
    name = worksheet.cell(countcategories, 1).value
    altName = worksheet.cell(countcategories, 2).value
    altVersion = worksheet.cell(countcategories, 3).value
    mediaFormats = worksheet.cell(countcategories, 4).value
    OS = worksheet.cell(countcategories, 5).value
    periph = worksheet.cell(countcategories, 6).value
    source = worksheet.cell(countcategories, 7).value
    exclusion = worksheet.cell(countcategories, 8).value
    problem = worksheet.cell(countcategories, 9).value
    notes = worksheet.cell(countcategories, 10).value
    platformObj = Platform(name,altName,altVersion,mediaFormats,OS,periph,source,exclusion,problem,notes)
    platformList.append(platformObj)
    countcategories += 1

# Enter the name of the platform
platformName = raw_input('Enter the name of a platform: ')

# Put the information into a text file named the same as the platform
platformindex = 0;
for x in platformList:
    if x.platform_name == platformName:
        break
    platformindex += 1

file = open(platformName+".txt", "w")
platformList.index(platformindex).toString()

file.close()

sys.exit()
