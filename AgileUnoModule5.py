""" 
Matthew Dawson
Agile UNO Module 5
Strings and Lists
102520
"""
#from sys library import exit module
from sys import exit
#import the requests library
import requests

#initialize site_data dict
site_data = {}

#with the "sites.csv" file open as the variable 'infile'...
with open("sites.csv", "r") as infile:
    #read the .csv file and store to the data variable
    data = infile.read()
    #store the sites data to a list (each item in data is seperated by a comma)
    sites = data.split(",")

#for each site in the sites list...
for site in sites:
    #store the site to the site_data dictionary and use the requests library to pull site response
    site_data[site] = requests.get(site)

#for each key and value pair in the site_data dictionary (key=site, value=response)...
for key, value in site_data.items():
    #print the key value pairs (each on a new line)
    print(f"\n{key} : {value}")


#[1]
###########################################
"""
Using string slicing, pring out each URL extension below: example
edu
com
edu
"""
#loop through all the sites in sites list
for site in sites:
    #pull the last three characters of the string, these are the extension
    #note: will not work for 2 character extension sites (i.e. .io or .co sites) could be modified to accomadate these
    extension = site[-3:]
    print(extension)



#[2]
##############################################
"""
print out any sites that end with .com below
"""
#loop through all the sites in the sites list
for site in sites:
    #if the last 3 characters are "com" print that site
    if site[-3:] == "com":
        print(site)




#[3]
#################################################
"""
convert all site names to upper case and print out each below
"""
#loop through all the sites in the sites list
for site in sites:
    #print the uppercase version of the site
    print(site.upper())

#[4]
#######################################################
"""
using the list of sites, add a new site to it..
using the input() method to get the name of the site from the user
then reverse the order of the list and print it out
"""
#request input from the user for a new site
new_site = str(input("What site would you like to add to the list?"))
#add the new site to the end of the site list
sites.append(new_site)
#reverse the list
sites.reverse()
#print the list
print(sites)

#[5]
#######################################################
"""
print out the 'Server' of the reponse of the URL request of the itemsfrom your list

example: print(f"{mySiteData.headers.get('Server')} \n")
"""
#for the site and responses in the site_data dictionary
for site,response in site_data.items():
    #print the response
    print(f"{response.headers.get('Server')} \n")



#[6]
#######################################################
"""
exit the program using the sys module's exit function
"""
#exit the program
exit()