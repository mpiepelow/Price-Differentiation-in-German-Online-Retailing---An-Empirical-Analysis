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
        entry= str(row)
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
    output = open(date1 + " zurrose_vitalsana.csv", "w+")
    driver = webdriver.Chrome()
    now = datetime.datetime.now()
    print(now)
    output.write(str(now))
    output.write("\n")
    #search

    driver.get("https://www.vitalsana.com/")
    
    time.sleep(5)
    
    button = driver.find_element_by_xpath("//a[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
    button.click()

    for a in list_links_all:
        try:
            linklist = str("https://www.vitalsana.com/catalogsearch/result/?q=") + str(a)
            print(linklist)
            driver.get(linklist)
            #time.sleep(1)
            output.write(str(a) + str(";"))
            ##price

            product_pages = driver.find_elements_by_xpath("//meta[@itemprop='price']")

            for value in product_pages:
                try:
                    price_raw = value.get_attribute("content")
                    print(price_raw)
                    price_split = str(price_raw).split(".")

                    price_splita = price_split[0]
                    non_decimal = re.compile(r'[^\d.]+')
                    f = non_decimal.sub('', price_splita)
                    price_splitb = price_split[1]
                    non_decimal = re.compile(r'[^\d.]+')
                    c = non_decimal.sub('', price_splitb)
                    output.write(str(f) + str(",") + str(c) + str(";"))
                    print(str(f) + str(",") + str(c) + str(";"))

                except:
                    print("-9")
                    output.write(str("-9") + str(";"))
        except:
            print("-9")
            output.write(str("-9") + str(";"))


            # print(without_empty_strings)



        ##category


        output.write("\n")




now = datetime.datetime.now()
print(now)
output.write(str(now))
output.write("\n")
output.close()
driver.close()

