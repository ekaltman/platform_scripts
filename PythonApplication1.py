# This program retrieves data from a specific spreadsheet, places it in a CSV file, and prints out information on a specific platform
import gdata.docs.service
import gspread
import codecs
import sys
from getpass import getpass
from platform_class import Platformclass
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
import csv
import os.path
import logging
logging.basicConfig()
allPlatforms = []
response = ''
if os.path.isfile("platformlist.csv"):
    response = raw_input("A CSV file exists. Would you like to use it? (Y/N)")
if response == 'Y' or response == 'y':
    f = open('platformlist.csv')
    readCSV = csv.reader(f)

    for x in readCSV:
        try:
            print x[0]
            allPlatforms.append(Platformclass(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        except IndexError:
            break
elif not os.path.isfile('platformlist.csv') or response == 'n' or response == 'N':
    username = raw_input('Enter Google User Name: ')
    passwd = getpass('Enter password: ')
    print 'authenticating with google...'
# Authenticate using your Google Docs email address and password.
    client = gspread.login(username + '@gmail.com', passwd)
# Query the server for the spreadsheet and worksheet
    sh = client.open_by_url("https://docs.google.com/spreadsheets/d/1zTDX9LNb5yR88IdvMbauBvCZL_TQPkMzompQz5QrRec/edit#gid=0")
    worksheet = sh.get_worksheet(0)
    print 'organizing worksheet...'
# For the worksheet
    platformList = worksheet.get_all_records()
    platform_sheet_headers = ['skos:Concept',
                              'skos:prefLabel',
                              'skos:altLabel',
                              'skos:definition',
                              'skos:related',
                              'skos:broader',
                              'skos:note']
    for x in platformList:
        print x['skos:Concept']
        platformObj = Platformclass(*[x[header] for header in platform_sheet_headers])
        allPlatforms.append(platformObj)
# Print all info to csv file
    file = open("platformlist.csv", "wb")
    wri = csv.writer(file, quoting=csv.QUOTE_ALL)
    wri.writerow(platform_sheet_headers)
    for x in allPlatforms:
        wri.writerow(x.toStringCSV())

#XML
    g = Graph()
    skos = Namespace('http://www.w3.org/2004/02/skos/core#')
    g.bind('skos', skos)
    skip = 0

    for x in allPlatforms:
        y = 0
        morethanone = False
        skip+=1
        if skip == 1:
            continue
        g.add((URIRef(x.concept), RDF.type, skos['Concept']))
        g.add((URIRef(x.concept), skos['prefLabel'], Literal(x.pref_label)))
        if x.alt_label == '':
            continue
        if ';' in x.alt_label:
            morethanone = True
            count = 0
            lower = 0
            while y < len(x.alt_label):
                if x.alt_label[y] == ';':
                    count +=1
                    if count == 1:
                        g.add((URIRef(x.concept), skos['altLabel'], Literal(x.alt_label[0:y])))
                
                    if count > 1:
                        g.add((URIRef(x.concept), skos['altLabel'], Literal(x.alt_label[lower:y])))
                    lower = y+2
                y +=1
            g.add((URIRef(x.concept), skos['altLabel'], Literal(x.alt_label[lower:len(x.alt_label)])))
        if morethanone == False:
            g.add((URIRef(x.concept), skos['altLabel'], Literal(x.alt_label)))
    g.serialize(destination = 'text.xml',format="pretty-xml")
# Enter the name of the platform
platformName = raw_input('Enter the name of a platform: ')
# Put the information into a text file named the same as the platform
platformindex = 0
for x in allPlatforms:
    if x.concept == platformName:
        break
    else:
        platformindex += 1
allPlatforms[platformindex].toFile()
print 'File created'
