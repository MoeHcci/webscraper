#About:
#This is a web scraping script that scrapes the data from https://www.autoparkmississauga.ca/used/group/ of vehicles':
##Models, Manufacturer, year, color, km, price, body type, engine type Transmission type, Wheel configuration, #city

#Import the libraries
import requests  # https://docs.python-requests.org/en/latest/
#The requests library is used to generate requests from the web page
import bs4  # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#bs4 will allow the script to present the data in a nested data strcture(easily seperated/organized)
import lxml
#lxml is the parser chosen for this script, which allows bs4 to break down the html file
import pandas
#The dataFrame of Panada will be used to generate a 2D tabular data that can be exported to .csv file and .sql file
import sqlalchemy
#The sqlalchemy library will allow the script to connect with PostgreSQL
import time
#The time library is used to keep the time it takes to run the script

#Time counter begins
time_0 = time.time_ns()


def web_scraper():

    #Empty lists that are used to capture the scraped data
    l_model_all = []
    l_manufacturer_all = []
    l_relesedate_all = []
    l_color_all = []
    l_km_all = []
    l_prices_all = []
    l_bodytype_all = []
    l_engine_all = []
    l_vehicleTransmission_all = []
    l_driveWheelConfiguration_all = []
    l_city_all = []

    #The start page # You can keep the default at 1 or choose any other page number
    pg = 75

    # A while loops that continously loops until len(l_prices) == 0
    while True:

        #Using the requests library and its get method to connect to the web page
        response = requests.get(f'https://www.autoparkmississauga.ca/used/group/pg/{pg}')

        #Check the status of the request library. 200 meanns the script will be able to parse through
        #print(response.status_code)

        #Creating a soup using the BeautifulSoup method of bs4 & the "lxml" parser. Also, the .text method is used
        soup = bs4.BeautifulSoup(response.text, 'lxml')


        #Capturing the raw results using the soup.find_all varilable and attribute
        results_manufacturer = soup.find_all('span', itemprop='manufacturer')
        results_model = soup.find_all('span', itemprop='model')
        results_relesedate = soup.find_all('span', itemprop='releaseDate')
        results_color = soup.find_all('td', itemprop='color')
        results_km = soup.find_all('span', class_='mileage-used-list')
        results_prices = soup.find_all('span', class_='vehicle-price-2-new suggestedPrice-price')
        results_bodytype = soup.find_all('td', itemprop='bodyType')
        results_engine = soup.find_all('td', itemprop='vehicleEngine')
        results_vehicleTransmission = soup.find_all('td', itemprop='vehicleTransmission')
        results_driveWheelConfiguration = soup.find_all('td', itemprop='driveWheelConfiguration')
        results_city = soup.select('td > var')

        #Creating lists to store the data from each feature we are interested in
        l_prices = []
        for x in results_prices:
            l_prices.append(x.get_text().replace("\n", ""))
        l_prices_all = l_prices_all + l_prices

        l_manufacturer = []
        for x in results_manufacturer:
            l_manufacturer.append(x.get_text().replace(" ", ""))
        l_manufacturer_all = l_manufacturer_all + l_manufacturer

        l_relesedate = []
        for x in results_relesedate:
            l_relesedate.append(x.get_text().replace(" ", ""))
        l_relesedate_all = l_relesedate_all + l_relesedate

        l_model = []
        for x in results_model:
            l_model.append(x.get_text())
        l_model_all = l_model_all + l_model

        l_km = []
        for x in results_km:
            l_km.append(x.get_text().replace(" ", ""))
        l_km_all = l_km_all + l_km

        l_bodytype = []
        for x in results_bodytype:
            l_bodytype.append(x.get_text().replace(" ", ""))
        l_bodytype_all = l_bodytype_all + l_bodytype

        l_engine = []
        for x in results_engine:
            l_engine.append(x.get_text().replace(" ", ""))
        l_engine_all = l_engine_all + l_engine

        l_color = []
        for x in results_color:
            l_color.append(x.get_text().replace(" ", ""))
        l_color_all = l_color_all + l_color

        l_vehicleTransmission = []
        for x in results_vehicleTransmission:
            l_vehicleTransmission.append(x.get_text().replace(" ", ""))
        l_vehicleTransmission_all = l_vehicleTransmission_all + l_vehicleTransmission

        l_driveWheelConfiguration = []
        for x in results_driveWheelConfiguration:
            l_driveWheelConfiguration.append(x.get_text().replace(" ", ""))
        l_driveWheelConfiguration_all = l_driveWheelConfiguration_all + l_driveWheelConfiguration

        l_city = []
        for x in results_city:
            l_city.append(x.get_text().replace(" ", ""))
        l_city_all = l_city_all + l_city

        # The condition for the while loop
        if len(l_prices) == 0:
            break
        # Adding page number each time the while loop completes an iteration
        pg = pg + 1

    #Outside the while loop. Panda is used to present the data in table format using panda.DataFrome
    d = {'l_model': l_model_all, 'l_manufacturer': l_manufacturer_all, 'l_relesedate': l_relesedate_all,
         'l_color': l_color_all, 'l_km': l_km_all, 'l_prices': l_prices_all, 'l_bodytype': l_bodytype_all,
         'l_engine': l_engine_all,
         'l_vehicleTransmission': l_vehicleTransmission_all, 'l_driveWheelConfiguration': l_driveWheelConfiguration_all,
         'l_city': l_city_all}

    #The following code below is used to cover come the issue of empter rows.
    #Resource: stackoverflow.com/questions/40442014/python-pandas-valueerror-arrays-must-be-all-same-length
    df = pandas.DataFrame.from_dict(data=d,orient='index')
    df = df.transpose()
    print(df)

    #Present the data in an csv format. Therefore transfer frpm pd.dataframe work to csv
    pwd = '~/Desktop/scraped_data.csv'
    df.to_csv(pwd,sep=',')

    #The sqkalchemy library used to export the data into PostgreSQL
    #host="localhost",database="webscraping",user="postgres",password="password"
    #Note: The webscraping database must have already been created in PostgresSQL
    engine = sqlalchemy.create_engine('postgresql://postgres:password@localhost:5432/webscraping')
    df.to_sql('web_scraper', engine, if_exists='replace')


    #End of time counter
    time_1 = time.time_ns()
    total = time_1 - time_0
    print(
        f'The time it takes for the operation to run is: {(total * (10 ** (-9)))} seconds')


if __name__ == '__main__':
    web_scraper()