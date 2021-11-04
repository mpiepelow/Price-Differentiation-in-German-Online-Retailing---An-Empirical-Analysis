import csv
import re
import random
import datetime
from selenium import webdriver
import numpy as np
import time
from selenium.webdriver.common.keys import Keys

    #open list

with open('datasample_zurrose.csv', 'r') as file:
    reader = csv.reader(file)

    # parsing of sample ids
    list_links_all = []
    for row in reader:
        entry = str(row)
        non_decimal = re.compile(r'[^\d.]+')
        p = non_decimal.sub('', entry)
        list_links_all.append(p)

    print(list_links_all)
    file.close()



    # date for name
    date = (datetime.datetime.now())
    date1 = str(date).split(":")[0]
    print(str(date1))

    # create file
    output = open(date1 + " zurrose_aporot.csv", "w+")
    driver = webdriver.Chrome()
    now = datetime.datetime.now()
    print(now)
    output.write(str(now))
    
    output.write("\n")
    #search

    driver.get("https://www.apo-rot.de/")

    time.sleep(5)
    
    # click that shit
    button = driver.find_element_by_xpath("//span[@id='cmpbntyestxt']")
    button.click()
    # get product link
    for a in list_links_all:
        try:
            #time.sleep(3)
            linklist = str("https://www.apo-rot.de/index_search.html?_formname=searchform&_errorpage=%2Findex.html&_command=SearchReroute&_validation=1209616344&_filtersmartsearch=x&_filteronlyInMenu=x&_filterwithTier=x&_filternolimits=x&_filterktext=") + str(a)
            print(linklist)
            output.write(str(a) + str(";"))
            #time.sleep(1)
            driver.get(linklist)


            ##price

            product_pages = driver.find_elements_by_xpath("//script[contains(.,'var dataLayer = dataLayer || [];')]")

            for value in product_pages:
                try:

                    ass = value.get_attribute("innerHTML")
                    asses = str(ass).split("price")[1]
                    assesa = str(asses).split("},")[0]
                    #value_list.append(assesa)
                    #print(assesa)
                    price_split = str(assesa).split(".")
                    price_splita = price_split[0]
                    non_decimal = re.compile(r'[^\d.]+')
                    f = non_decimal.sub('', price_splita)
                    price_splitb = price_split[1]
                    non_decimal = re.compile(r'[^\d.]+')
                    c = non_decimal.sub('', price_splitb)
                    price_final =str(f) + str(",") + str(c) + str(";")
                    print(price_final)
                    output.write(str(price_final) + str(";"))

                except:
                    pass
                    #print("-9")
                    #output.write(str("-9") + str(";"))
            if assesa == "":
                print("-9")
                output.write(str("-9") + str(";"))



            # print(without_empty_strings)



        ##category


            output.write("\n")

        except:
            output.write(str("-9") + str(";"))

now = datetime.datetime.now()
    
print(str(now))
output.write(str(now))
output.write("\n")
output.close()
driver.close()