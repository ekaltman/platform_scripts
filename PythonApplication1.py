# This program retrieves data from a specific spreadsheet, places it in a CSV file, and prints out information on a specific platform
import gdata.docs.service
import gspread
import codecs
import sys
from getpass import getpass
from platform_class import Platformclass,MediaFormat
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
import csv
import os.path
from os.path import join as pjoin
import logging
import jinja2
logging.basicConfig()
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)+"/Templates")
)
template = JINJA_ENVIRONMENT.get_template( "platform.jinja" )
maintemplate = JINJA_ENVIRONMENT.get_template( "main.jinja" )
allPlatforms = []
response = ''
which = int(raw_input("Press 0 for platforms or 1 for media formats: "))
if which == 0 and os.path.isfile("platformlist.csv"):
    response = raw_input("A platform CSV file exists. Would you like to use it? (Y/N)")
if which == 1 and os.path.isfile("mediaplatformlist.csv"):
    response = raw_input("A media formats CSV file exists. Would you like to use it? (Y/N)")
if response == 'Y' or response == 'y':
    if which == 0:
        f = open('platformlist.csv')
    elif which == 1:
        f = open('mediaplatformlist.csv')
    readCSV = csv.reader(f)

    for x in readCSV:
        try:
            print x[0]
            if which == 0:
                allPlatforms.append(Platformclass(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
            elif which == 1:
                allPlatforms.append(MediaFormat(x[0],x[1],x[2],x[3],x[4],x[5]))
        except IndexError:
            break
elif (which == 0 and not os.path.isfile('platformlist.csv')) or (which == 1 and not os.path.isfile('mediaplatformlist.csv')) or response == 'n' or response == 'N':

    username = raw_input('Enter Google User Name: ')

    passwd = getpass('Enter password: ')
    print 'authenticating with google...'
# Authenticate using your Google Docs email address and password.
    client = gspread.login(username + '@gmail.com', passwd)
# Query the server for the spreadsheet and worksheet
    if which == 0:
        sh = client.open_by_url("https://docs.google.com/spreadsheets/d/1zTDX9LNb5yR88IdvMbauBvCZL_TQPkMzompQz5QrRec/edit#gid=0")
        worksheet = sh.get_worksheet(0)
    elif which == 1:
        sh = client.open_by_url("https://docs.google.com/spreadsheets/d/1zTDX9LNb5yR88IdvMbauBvCZL_TQPkMzompQz5QrRec/edit#gid=1492865306")
        worksheet = sh.get_worksheet(1)
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
    mediaplatform_sheet_headers = ['skos:Concept',
                              'skos:prefLabel',
                              'skos:altLabel',
                              'skos:definition',
                              'skos:related',
                              'skos:broader']
    for x in platformList:
        print x['skos:Concept']
        if which == 0:
            platformObj = Platformclass(which,*[x[header] for header in platform_sheet_headers])
        if which == 1:
            platformObj = Platformclass(which,*[x[header] for header in mediaplatform_sheet_headers])
        allPlatforms.append(platformObj)
# Print all info to csv file
    if which == 0:
        file = open("platformlist.csv", "wb")
    elif which == 1:
        file = open("mediaplatformlist.csv", "wb")
    wri = csv.writer(file, quoting=csv.QUOTE_ALL)
    wri.writerow(platform_sheet_headers)
    for x in allPlatforms:
        wri.writerow(x.toStringCSV())

#XML
    g = Graph()
    skos = Namespace('http://www.w3.org/2004/02/skos/core#')
    g.bind('skos', skos)
    gamecip = 'http://example.org/'
    skip = 0

    for x in allPlatforms:
        name = ''
        for b in x.concept.split(' '):
            name += b
        skip+=1
        if skip == 1:
            continue
        g.add((URIRef(gamecip+name), RDF.type, skos['Concept']))
        g.add((URIRef(gamecip+name), skos['prefLabel'], Literal(x.pref_label)))
        if x.broader is not '':
            broad = ''
            for v in x.broader.split(' '):
                broad += v
            g.add((URIRef(gamecip+name), skos['broader'], URIRef(gamecip+broad)))
        if x.alt_label == '':
            continue
        for a in x.alt_label.split(";"):
            g.add((URIRef(gamecip+name), skos['altLabel'], Literal(a)))
        g.add((URIRef(gamecip+name), skos['definition'], Literal(x.definition)))
    g.serialize(destination = 'text.xml',format="pretty-xml")
# Enter the name of the platform
allToHTML = raw_input('Make all platform html pages?(Y/N) ')
file_names = [] #for names of the html files
platform_names = [] #for the names of the platforms
if allToHTML == 'y' or allToHTML == 'Y':
    for x in allPlatforms:
        platformInfo = x.toHtml()
        templateVars = { "title" : x.concept,
                 "description" : "test",
                 "platformInfo" : platformInfo
               }
        outputText = template.render( templateVars )

        filenamesl = ''
        filenamecol = ''
        filename = ''
        for slash in x.concept.split("/"):
            filenamesl += slash

        for colon in filenamesl.split(":"):
            filenamecol += colon
        for space in filenamecol.split(' '):
            filename += space
        platform_names.append(filename)
        filename += '.html'
        if which == 0:
            folder = "platform_html"
        elif which == 1:
            folder = "media_format_html"
        file_names.append(filename)
        path_to_folder = pjoin("D:\\", "Python Projects", "github", "platform_scripts", folder)
        #make folder if it doesn't exist
        try:
            os.makedirs(path_to_folder)
        except OSError:
            if not os.path.isdir(path_to_folder):
                raise
        path_to_file = pjoin("D:\\", "Python Projects", "github", "platform_scripts", folder, filename)
        file = open(path_to_file, "w")
        file.write(outputText.encode('utf-8'))
        x.toFile()
elif allToHTML == 'n' or allToHTML == 'N':
    platformName = raw_input('Enter the name of a platform: ')
    # Put the information into a text file named the same as the platform
    platformindex = 0
    for x in allPlatforms:
        if x.concept == platformName:
            break
        else:
            platformindex += 1
    platformInfo = allPlatforms[platformindex].toHtml()
    templateVars = { "title" : platformName,
                 "description" : "test",
                 "platformInfo" : platformInfo
               }
    outputText = template.render( templateVars )
    filenamesl = ''
    filename = ''
    for slash in x.concept.split("/"):
        filenamesl += slash
    platform_names.append(filenamesl)
    for space in filenamesl.split(' '):
        filename += space
    filename += '.html'
    if which == 0:
        folder = "platform_html"
    elif which == 1:
        folder = "media_format_html"
    file_names.append(filename)
    path_to_file = pjoin("D:\\", "Python Projects", "github", "platform_scripts", folder, filename)
    file = open(path_to_file, "w")
    file.write(outputText.encode('utf-8'))
    allPlatforms[platformindex].toFile()
    print 'File created'

#the main menu
templateVars = { "title" : "Main menu",
                 "description" : "test",
                 "platformInfo" : file_names,
                 "platformNames" : platform_names
               }
outputText = maintemplate.render( templateVars )
if which == 0:
    folder = "platform_html"
elif which == 1:
    folder = "media_format_html"
path_to_file = pjoin("D:\\", "Python Projects", "github", "platform_scripts", folder, "main.html")
mainfile = open(path_to_file, "w")
mainfile.write(outputText.encode('utf-8'))