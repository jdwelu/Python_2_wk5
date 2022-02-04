#! /usr/bin/env python3

import xml.etree.ElementTree as et

tree = et.parse('cd_catalog.xml')
#print(tree)
root = tree.getroot()
#print(root)

for child in root:
    print("Artist: " + child.find('ARTIST').text + ", ",
            "Title: " + child.find('TITLE').text + ", ",
            # "Year: " + child.find('YEAR').text + ", ",
            "Decade: " + child.attrib['decade'])


## Original solution, but the assignment can be done with less code. 
## Year was added and taken out to make sure the decade was correct.
    
##for child in root.findall('CD'):
##    print("Artist: " + child.find('ARTIST').text + ", ",
##            "Title: " + child.find('TITLE').text + ", ",
##            # "Year: " + child.find('YEAR').text + ", ",
##            "Decade: " + child.attrib['decade'])




