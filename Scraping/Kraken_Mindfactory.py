import csv
import re
import random
import datetime
from selenium import webdriver
import numpy as np
import time
from selenium.webdriver.common.keys import Keys

# open list

with open('datasample_Mindfactory.csv', 'r') as file:
    reader = csv.reader(file)

    # parsing of sample ids
    idlist_all = []
    for row in reader:
        entry = str(row)
        non_decimal = re.compile(r'[^\d.]+')
        p = non_decimal.sub('', entry)
        idlist_all.append(p)

    # print(list_links_all)
    file.close()

with open('linkliste_sample Mindfactory.csv', 'r') as file:
    reader = csv.reader(file)

    # parsing of sample ids
    linklist_all = []
    for row in reader:
        entry = str(row)

        linklist_all.append(entry)

        print(linklist_all)
    file.close()


    # date for name
    date = (datetime.datetime.now())
    date1 = str(date).split(":")[0]
    print(str(date1))



    # create file/ define webdriver

    output = open(date1 + " Mindfactory_MF.csv", "w+")
    driver = webdriver.Chrome()
    now = datetime.datetime.now()
    print(now)
    output.write(str(now))
    output.write("\n")
    # search

    driver.get("https://www.mindfactory.de/")
    time.sleep(4)

    # click that shit
    # click that shit
    button = driver.find_element_by_xpath("//a[@id='justneededcookie']")
    button.click()
    #for f, b in zip(foo, bar):for f, b in zip(foo, bar):
    for a in linklist_all:
        try:

            link_product = str(a).replace("https://www.mindfactory.de/","https://www.mindfactory.de/")
            link = str(link_product).replace("[","").replace("]","").replace("\'","")
            print(link)

            #time.sleep(0.5)
            # open page
            driver.get(link)

            Ean = driver.find_elements_by_xpath("//script[contains(.,'Cliplister.player({')]")
            for number in Ean:
                try:
                    ass = number.get_attribute("innerHTML")
                    asses = str(ass).split("requestkey")[1]
                    assesa = str(asses).split("\"")[1]
                    print(assesa)
                    output.write(str(assesa) + str(";"))
            ##price
                except:
                    output.write(str("-9")+str(";"))

            product_pages = driver.find_elements_by_xpath("//script[contains(.,'dataLayer = [{')]")

            for value in product_pages:
                try:
                    ass = value.get_attribute("innerHTML")
                    asses = str(ass).split("Artikelpreis")[1]
                    assesa = str(asses).split(",")[0]

                    #print(assesa)
                    price_split = str(assesa).split(".")
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
                    output.write(str("-9")+str(";"))





            #category
            #product_pages = driver.find_elements_by_xpath("//ol[@class='breadcrumb']/li/a")

            #for value in product_pages:
            #    try:
             #       ass = value.get_attribute("title")
              #      output.write(str(ass) + str(";"))
               #     print(ass)

                #except:
                #    print("-9")
                 #   output.write(str("-9") + str(";"))
                  #  output.write(str("-9") + str(";"))
                   # output.write(str("-9") + str(";"))
                    #output.write(str("-9") + str(";"))
            # print(without_empty_strings)

            ##category

            output.write("\n")

        except:
            output.write(str("-9") + str(";"))
            output.write("\n")
now = datetime.datetime.now()
print(now)
output.write(str(now))
output.write("\n")
output.close()
driver.close()
