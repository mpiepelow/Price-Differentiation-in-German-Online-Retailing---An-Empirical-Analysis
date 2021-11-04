import csv
import re
import random
import datetime
from selenium import webdriver
import numpy as np
import time
import random
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
    output = open(date1 + " weltbild_buecherde.csv", "w+")
    driver = webdriver.Chrome()
    now = datetime.datetime.now()
    print(now)
    output.write(str(now))
    output.write("\n")
    # search

    driver.get("https://www.buecher.de/")
    time.sleep(5)

    button = driver.find_element_by_xpath("//a[@class='cm-link']")
    button.click()

    for a in list_links_all:
        try:
            output.write(str(a) + str(";"))

            searchbar = driver.find_element_by_xpath("//input[@id='qusearchfield_sm']")

            searchbar.clear()
            # time.sleep(2)
            searchbar.send_keys(a)

            searchbar.send_keys(Keys.ENTER)
            #time.sleep(random.randint(1,2))
            # linklist = str("https://www.weltbild.de/suche/") + str(a)
            # driver.get(linklist)

            ##price
            # script_text = driver.find_element_by_xpath("//script[contains(.,'mpr-graph')]").text
            product_pages = driver.find_elements_by_xpath("//script[contains(.,'window.dataLayer=window.dataLayer')]")
            value_list = []

            for value in product_pages:

                try:
                    ass = value.get_attribute("innerHTML")
                    asses = str(ass).split(",ecomm_pvalue:")[1]
                    assesa = str(asses).split("}")[0]
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
            #Kategories

            product_pages = driver.find_elements_by_xpath("//ul[@class = 'breadcrumb inline large-layout show-all']/li")
            value_list = []

            for value in product_pages:
                try:
                    ass = value.text
                    # asses = str(ass).split("\"price\":")[1]
                    # assesa = str(asses).split("\"")[1]
                    value_list.append(ass)

                except:
                    pass
            without_empty_strings = []
            for string in value_list:
                if (string != ""):
                    without_empty_strings.append(string)

            for category in without_empty_strings:
                print(category)
                output.write(str(category) +str(";"))

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
