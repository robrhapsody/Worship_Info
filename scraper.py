import lxml
import lxml.html
import lxml.etree

url = ""
xpath = ""
listTextfull = []



# get the raw HTML
webSite = lxml.html.parse( url )

# get title nodes in the raw HTML and turn into list
things = webSite.xpath( xpath )
thingText   = [ thing.text   for thing   in things ]
thingText   = [ text.encode( 'utf-8', 'ignore' ) for text in thingText ]
#print thingText

listTextfull.extend(thingText)



# zip separate lists into a single list of tuples
tuples = zip( listTextfull )

print tuples

#write results to a tab-delimited TXT file
with open( "file.txt", "w" ) as tsvFile:
    for tuple in tuples:
        tsvFile.write( "%s \n" % tuple )
