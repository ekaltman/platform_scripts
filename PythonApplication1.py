# This program retrieves data from a specific spreadsheet, places it in a CSV file, and prints out information on a specific platform
import gdata.docs.service
import gspread
import codecs
import sys
from getpass import getpass
from platform import Platform
import rdflib
import csv
import os.path

allPlatforms = []
response = ''
if os.path.isfile("platformlist.csv"):
    response = raw_input("A CSV file exists. Would you like to use it? (Y/N)")

if response == 'Y' or response == 'y':
    f = open('platformlist.csv')
    readCSV = csv.reader(f)
    for x in readCSV:
        print x[0]
        allPlatforms.append(Platform(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]))

elif not os.path.isfile('platformlist.csv') or response == 'n' or response == 'N':    
    username = raw_input('Enter Google User Name: ')
    passwd = getpass('Enter password: ')
    print 'authenticating with google...'

    # Authenticate using your Google Docs email address and password.

    client = gspread.login(username + '@gmail.com', passwd)

    # Query the server for the spreadsheet and worksheet
    worksheet = client.open("Platform and Media Format Spreadsheet").get_worksheet(4)
    print 'organizing worksheet...'

    # For the worksheet
    platformList = worksheet.get_all_records()
    platform_sheet_headers = ['Platform Name',
                              'Alternate Name',
                              'Alternate Version',
                              'Media Formats',
                              'Operating System (if applicable)',
                              'Peripherals',
                              'Sources',
                              'Exclusion Rational',
                              'Problematic',
                              'Notes']
    
    for x in platformList:
        print x['Platform Name']
        platformObj = Platform(*[x[header] for header in platform_sheet_headers])
        allPlatforms.append(platformObj)

    # Print all info to csv file
    file = open("platformlist.csv", "wb")
    wri = csv.writer(file, quoting=csv.QUOTE_ALL)
    wri.writerow(platform_sheet_headers)
    for x in allPlatforms:
        wri.writerow(x.toStringCSV())
        
# Create RDF
    for x in allPlatforms:
        g.add((URIRef(x.platform_name), RDF['type'], skos['Concept']))
        g.add((URIRef('URI'), skos['prefLabel'], Literal(x.platform_name, lang='en')))
        lower = 0
        morethanone = false
        for y in x.alternate_name:
            if x.alternate_name[y] == ';':
                morethanone = true
                lower = y+1
                g.add((URIRef('URI'), skos['altLable'], URIRef(x.alternate_name[lower:y-1])))
        if morethanone == false:
            g.add((URIRef('URI'), skos['altLable'], URIRef(x.alternate_name)))
    g.serialize('text.xml',format="pretty-xml")
    


# Enter the name of the platform
platformName = raw_input('Enter the name of a platform: ')


# Put the information into a text file named the same as the platform
platformindex = 0
for x in allPlatforms:
    if x.platform_name == platformName:
        break
    else:
        platformindex += 1


allPlatforms[platformindex].toFile()
print 'File created'
