import csv
import re
import random
import datetime
from selenium import webdriver
import numpy as np
import time
from selenium.webdriver.common.keys import Keys
import random
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
    output = open(date1 + "  zurrose_eurapon.csv", "w+")
    driver = webdriver.Chrome()
    now = datetime.datetime.now()
    print(now)
    output.write(str(now))
    output.write("\n")
    #search

    driver.get("https://www.eurapon.de/")

    time.sleep(5)

    # click that shit
    button = driver.find_element_by_xpath("//div[@class='ccm__footer']/div")
    button.click()
    # get product link
    for a in list_links_all:
        try:
            #time.sleep(3)
            linklist = str("https://www.eurapon.de/search?sSearch=") + str(a)
            print(linklist)
            driver.get(linklist)
            #time.sleep(random.randint(0.5,1.5))
            output.write(str(a) + str(";"))

            ##price "//span[@class='normal-price']"
            # product_pages = driver.find_elements_by_xpath("//script[contains(.,'dataLayer.push({')]")
            product_pages = driver.find_elements_by_xpath("//meta[@itemprop='price']")
            price_list = []
            for value in product_pages:


                price_raw = value.get_attribute("content")

                price_list.append(price_raw)


            #print(price_list)
            price = price_list[0]
            print(price)
            #print(price)
            #price_split = str(price).split("price")[2]
            #price_splita = str(price_split).split(":")[1]
            #price_splitb = str(price_splita).replace(".",",").replace("\"","").replace(";","")
            #print(price_splitb)
            price_splitb = str(price).split(",")
            # print(price_split)
            price_splitc = price_splitb[0]
            non_decimal = re.compile(r'[^\d.]+')
            f = non_decimal.sub('', price_splitc)
            price_splitd = price_splitb[1]
            non_decimal = re.compile(r'[^\d.]+')
            c = non_decimal.sub('', price_splitd)
            print(str(f) + str(",") + str(c) + str(";"))
            output.write(str(f) + str(",") + str(c) + str(";"))



            #price_final = str(price_splitb) + str(";")
            #print(price_final)
            #output.write(str(price_final))
        except:
            #time.sleep(2)
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
