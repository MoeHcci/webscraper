#This .py file covers the basics of webscraping
#Main Topics Covered:
##The required packagesThe packages to install which are
####requests, Allows us to make requests to websites and grab the info off the website
###lxml, It is an HTML parser. Therefore, it is able to allow bs4 to distinguish between between the scraped html datar
###bs4 "beautirful soup Version 4",

#Step 1 Import the libraries
import requests #https://docs.python-requests.org/en/latest/
import bs4 #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import lxml
import html5lib
import pandas as pd
import time

t0=time.time()


#Exp: Grab the page title of a www.leasebusters.com webpage. This is whaat is written on the actual tab

def title():
    #This function grabs the title of a webpage

    #Notes:
    #1. Use the .get method of requests to access a webpage
    ##The get() method sends a GET request to the specified url.
    #https://docs.python-requests.org/en/master/ -> The documentation of requests
    #The class:`Response <Response>` object, which contains a server's response to an HTTP request.
    #The <class'requests.models.Response'> has the following attributes:
    ##['_content', '_content_consumed', '_next', 'status_code', 'headers', 'raw', 'url', 'encoding', 'history', 'reason', 'cookies', 'elapsed', 'request', 'connection', '__module__', '__doc__', '__attrs__', '__init__', '__enter__', '__exit__', '__getstate__', '__setstate__', '__repr__', '__bool__', '__nonzero__', '__iter__', 'ok', 'is_redirect', 'is_permanent_redirect', 'next', 'apparent_encoding', 'iter_content', 'iter_lines', 'content', 'text', 'json', 'links', 'raise_for_status', 'close', '__dict__', '__weakref__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
    ###For example --> print(results._content)

    #2. Use bs4 to get specific data points. bs4 will use the lxml parser to parse through the web-page's results from requests
    #https://www.crummy.com/software/BeautifulSoup/bs4/doc/ -> The documentation of bs4

    results = requests.get("https://www.leasebusters.com/vehicle-search-result?gallery=1&categories=SUVs%20/%20Crossovers-7,4%20Door%20Sedans-1,Passenger%20Vans%20/%20Minivans-8,5%20Door%20Wagons-3&makes=Buick-5,Cadillac-6,Chevrolet-7,Chrysler-8,Dodge-10,Ford-13,GMC-14,Jeep-21&postalcode=L5N%204P6")
    #print (results.text) #This will produce a string of all the html text in the webpage as a string
    soup=bs4.BeautifulSoup(results.text,"lxml")
    #print(soup.select('title')) #using the select attribute can allows to grab any html we want to grab. For example title. If you type p it will grab all the paragraphs
    #print(soup.select('title')[0].getText()) #this will get only the text without the html tags



def classes_two():

    #Method 2:

    response = requests.get("https://www.autoparkmississauga.ca/used/group/pg/5")
    #Using the "request" library and the "get" method to connect and get all the info of a web page

    #print(response.status_code)
    #Checking the status by using the status_code method on the "response" varilable. If we get 200 then we are good. If we get 403 then we are blocked

    #print(response.text)
    #Reading the content of the server's response by using the "text" method on the "response" varrable. If this looks good then we do not need to modify the "encoding" property


    soup=BeautifulSoup(response.text,'lxml') #-> .text would be preferred for textual responses, such as an HTML or XML document. Used for Unicode
    #soup=BeautifulSoup(response.content,'html5lib') #-> .content would be preferred for "binary" filetypes, such as an image or PDF fil. Used for bytes
    ##Create a new variable "soup". It is a function of the BeautifulSoup method of the bs4 package and it is parsing through the decoded web page to present it as a nested data strcture(easily seperated/organized) using "html5lib" parser
    ##Few commands we can use to navigate through the data strcture: soup.title and many more checkout the docs

    #print(soup.prettify)
    ##The prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string

    #print(soup.title.string)
    ##this will print the string potion of the full title. The full title also include the <title> html elements


    #find_first_a =soup.a
    ##If the html element is used as an attribute then the results will give you only the first "a" tag

    #find_all_a =soup.find_all('a',"p")
    ##This will find all the <a> tags in the html document

    results_prices = soup.find_all('span', class_='vehicle-price-2-new suggestedPrice-price')
    ##This will find all the <span> tags in the html document.and those <span> tags must have 'vehicle-price-2-new suggestedPrice-price' class.
    ##Using class as a keyword argument will give you a syntax error. As of Beautiful Soup 4.1.2, you can search by CSS class using the keyword argument class_ (A new short cut)
    #For multiple classes we need to use the CSS classes selector
    results_relesedate = soup.find_all('span', itemprop='releaseDate')
    results_manufacturer= soup.find_all('span', itemprop='manufacturer')
    results_model= soup.find_all('span', itemprop='model')
    results_km = soup.find_all('span', class_='mileage-used-list')
    results_bodytype = soup.find_all('td', itemprop='bodyType')
    results_engine = soup.find_all('td', itemprop='vehicleEngine')
    results_color = soup.find_all('td', itemprop='color')
    results_vehicleTransmission = soup.find_all('td', itemprop='vehicleTransmission')
    results_driveWheelConfiguration = soup.find_all('td', itemprop='driveWheelConfiguration')
    results_city = soup.select('td > var') #This method means any element named var directly within a td element and nothing in between

    print((results_prices[0].getText().strip())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that. The strip() is added to remove the white spece
    print((results_manufacturer[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that
    print((results_relesedate[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that
    print((results_model[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that
    print((results_km[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that
    print((results_bodytype[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that
    print((results_engine[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that
    print((results_color[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that
    print((results_vehicleTransmission[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that
    print((results_driveWheelConfiguration[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that
    print((results_city[0].getText())) #->  ##The results will be shown in an html form you need to use the reuqests library to over come that









    l = []
    for x in results_prices:
        l.append(x.get_text().replace("\n",""))
        ##The .text is used from the Requests library or we can use the .get_text() which is from the bs4 library
        ##This will view all individual texts in the results
    #print(l)



t1 = time.time()
total =t1-t0
#print(total) -> Calculate the total time it takes to comples an opration
if __name__ == '__main__':
    #title()
    classes_two()


    #Notes:
    #The find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters.
    #.select() method which uses the SoupSieve package to run a CSS selector against a parsed document and return all the matching elements. Tag has a similar method which runs a CSS selector against the contents of a single tag.
    ##In simplier tersm .select() method is used to locate all elements of a particular CSS class