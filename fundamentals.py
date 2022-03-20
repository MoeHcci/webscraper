#This .py file covers the basics of webscraping
#Main Topics Covered:
##The required packagesThe packages to install which are
####requests, Allows us to make requests to websites and grab the info off the website
###lxml, It is an HTML parser. Therefore, it is able to allow bs4 to distinguish between between the scraped html datar
###bs4 "beautirful soup Version 4",

#Step 1 Import the libraries
import requests
import bs4
import lxml
import html5lib
import pandas as pd


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



def classes():

    #results = requests.get("https://www.meadowvalehonda.ca/en/used-inventory")
    #print(results.status_code)
    #soup=bs4.BeautifulSoup(results.text,"lxml")
    #print((soup.select('.price')))
    #print(type((soup.select('.msrp-price')[0].text)))

    response = requests.get("https://www.autoparkmississauga.ca/used/")
    print(response.status_code)
    soup=bs4.BeautifulSoup(response.content,'html.parser')
    #print(soup)
    results = soup.find_all('span', {'class':'vehicle-price-2-new suggestedPrice-price'})
    print(len(results))
    print(results)






if __name__ == '__main__':
    #title()
    classes()