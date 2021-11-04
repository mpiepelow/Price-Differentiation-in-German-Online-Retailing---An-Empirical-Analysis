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

try:

    # date for name
    date = (datetime.datetime.now())
    date1 = str(date).split(":")[0]
    print(str(date1))

    # create file
    output = open(date1 + " zurrose_medpex.csv", "w+")
    driver = webdriver.Chrome()
    now = datetime.datetime.now()
    print(now)
    output.write(str(now))
    output.write("\n")
    #search

    driver.get("https://www.medpex.de/")

    time.sleep(5)
    # click that shit
    #button = driver.find_element_by_xpath("//span[@id='cmpbntyestxt']")
    #button.click()

    for a in list_links_all:
        try:

            try:
            # click that shit
                button = driver.find_element_by_xpath("//span[@id='cmpbntyestxt']")
                button.click()
            except:
                pass

            output.write(str(a) + str(";"))
            linklist = str("https://www.medpex.de/search.do?q=") + str(a)
            print(linklist)
            driver.get(linklist)
            #time.sleep(1)
            ##price
            #button = driver.find_element_by_xpath("//span[@class='product-name']/b/a")
            #button.click()
            product_pages = driver.find_elements_by_xpath("//span[@class='normal-price']")
            #product_pages = driver.find_elements_by_xpath("//script[contains(.,'dataLayer.push({')]")
            #time.sleep(1)
            for value in product_pages:
                try:
                    # click that shit



                        ass = value.text
                        #asses = str(ass).split("price")[1]
                        #assesa = str(asses).split(",")[0]

                        print(ass)
                        price_split = str(ass).split(",")

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

except:
    output.write(str("-9") + str(";"))

now = datetime.datetime.now()
print(now)
output.write(str(now))
output.write("\n")
output.close()
driver.close()



