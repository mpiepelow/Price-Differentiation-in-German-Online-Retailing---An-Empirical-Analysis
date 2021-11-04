import csv
import re
import random
import datetime
from selenium import webdriver
import numpy as np
import time
from selenium.webdriver.common.keys import Keys
    #open list

with open('datasample_weltbild_thalia.csv', 'r') as file:
    reader = csv.reader(file)

    # parsing of sample ids
    list_links_all = []
    for row in reader:
        entry= str(row)
        non_decimal = re.compile(r'[^\d.]+')
        p = non_decimal.sub('', entry)
        list_links_all.append(p)

    #print(list_links_all)
    file.close()



    # date for name
    date = (datetime.datetime.now())
    date1 = str(date).split(":")[0]
    print(str(date1))

    # create file
    output = open(date1 + " weltbild_thalia.csv", "w+")
    driver = webdriver.Chrome()
    now = datetime.datetime.now()
    print(now)
    output.write(str(now))
    output.write("\n")
    # search

    driver.get("https://www.thalia.de/")
    time.sleep(5)

    # click that shit
    button = driver.find_element_by_xpath("//button[@class='element-link-standard link-soft']")
    button.click()

    for a in list_links_all:
        try:
            output.write(str(a) + str(";"))

            linklist = str("https://www.thalia.de/suche?filterPATHROOT=&sq=") + str(a)

            print(linklist)
            driver.get(linklist)
            #time.sleep(1)
            ##price

            product_pages = driver.find_elements_by_xpath("//ul[@class = 'suchergebnis-liste no-bullets']")
            value_list = []
            for value in product_pages:
                try:
                    ass = value.get_attribute("innerHTML")
                    asses = str(ass).split("data-preis=")[1]
                    assesa = str(asses).split("data-preis-reduziert")[0]
                    value_list.append(assesa)
                    print(assesa)

                except:
                    pass
            without_empty_strings = []
            for string in value_list:
                if (string != ""):
                    without_empty_strings.append(string)
            try:
                price_split = str(without_empty_strings).split(".")
                # print(price_split)
                price_splita = price_split[0]
                non_decimal = re.compile(r'[^\d.]+')
                f = non_decimal.sub('', price_splita)
                price_splitb = price_split[1]
                non_decimal = re.compile(r'[^\d.]+')
                c = non_decimal.sub('', price_splitb)
                print(str(f) + str(",") + str(c) + str(";"))
                output.write(str(f) + str(",") + str(c) + str(";"))
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

