import csv
import re
import random
import datetime
from selenium import webdriver
import numpy as np
import time
from selenium.webdriver.common.keys import Keys


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
    output = open(date1 + " zurrose_docmorris_cat.csv", "w+")
    driver = webdriver.Chrome()
    now = datetime.datetime.now()
    print(now)
    output.write(str(now))
    output.write("\n")
    #search

    driver.get("https://www.docmorris.de/")

    time.sleep(5)
    # click that shit
    button = driver.find_element_by_xpath("//span[@id='cmpwelcomebtnyes']")
    button.click()

    for a in list_links_all:
        try:
            linklist = str("https://www.docmorris.de/search?query=") + str(a)
            output.write(str(a) + str(";"))
            driver.get(linklist)
            #time.sleep(1)
            ##price


            product_pages = driver.find_elements_by_xpath("//script[contains(.,'exactag.maincategory')]")

            value_list = []
            for value in product_pages:
                ass = value.get_attribute("innerHTML")
                print(ass)
                asses = str(ass).split("exactag.maincategory = ")[1]
                print(asses)
                assesa = str(asses).split(";")[0]
                print(assesa)
                value_list.append(assesa)
            print(value_list)

            output.write(str(value_list))
            #price = value_list[0]
            #price_split = str(price).split(".")
            ## print(price_split)
            #price_splita = price_split[0]
            #non_decimal = re.compile(r'[^\d.]+')
            #f = non_decimal.sub('', price_splita)
            #price_splitb = price_split[1]
            #non_decimal = re.compile(r'[^\d.]+')
            #c = non_decimal.sub('', price_splitb)
            #print(str(f) + str(",") + str(c) + str(";"))
            #output.write(str(f) + str(",") + str(c) + str(";"))
        except:
            time.sleep(1)
            print("-9")
            output.write(str("-9")+str(";"))


        output.write("\n")



now = datetime.datetime.now()
print(now)
output.write(str(now))
output.close()
driver.close()


