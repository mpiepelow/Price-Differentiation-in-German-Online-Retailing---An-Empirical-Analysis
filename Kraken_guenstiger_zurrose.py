

import numpy as np
import csv
import re
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open('datasample_zurrose.csv', 'r') as file:
    reader = csv.reader(file)

    # parsing of sample ids
    list_links_all = []
    for row in reader:
        entry = str(row)
        non_decimal = re.compile(r'[^\d.]+')
        p = non_decimal.sub('', entry)
        list_links_all.append(p)

    # print(list_links_all)
    file.close()

    # date for name
    date = (datetime.datetime.now())
    date1 = str(date).split(":")[0]
    print(str(date1))

    # create file
    output = open(date1 + " guenstigerde_zurrose.csv", "w+")
    #driver = webdriver.Chrome()
    now = datetime.datetime.now()
    print(now)
    output.write(str(now))
    output.write("\n")
    driver = webdriver.Chrome()
    driver.get("https://www.guenstiger.de")

    # search
    for product in list_links_all:
        output.write(str(product) + str(";"))
        try:

            searchlink = str("https://www.guenstiger.de/Katalog/Suche/") + str(product) + str(".html")
            print(product)
            page = driver.get(searchlink)



            temp_counter = [int("0")]
            temp_list = []
            for a, b in zip(driver.find_elements_by_xpath("//span[@class='PRICEVALUELEFT']"), driver.find_elements_by_xpath("//span[@class='PRICEVALUERIGHT']")):

                left = a.text
                leftb = left.split(",")[0]
                right = b.text
                leftright = (str(leftb) + str(".") + str(right))
                leftright2 = float(leftright)
                # print(leftright2)
                temp_list.append(leftright2)
                temp_number = int("1")
                temp_counter.append(temp_number)
            #print(temp_counter)
            #print(temp_list)




            if sum(temp_counter) > 1:
                # Anzahl Produkte
                number_products = sum(temp_counter)
                print(number_products)
                output.write(str(number_products))
                output.write(str(";"))
                ## Minumium Preis
                #min_price = min(temp_list)
                #output.write(str(min_price))
                #output.write(str(";"))

                # Maximum Preis
                #max_price = max(temp_list)
                #output.write(str(max_price))
                #output.write(str(";"))

                # Mittelwert Preis
                ean_price = np.mean(temp_list)
                output.write(str(temp_list))
                output.write(str(";"))

                # 0,25 Quantil
                #low_quantile = np.quantile(temp_list, 0.25)
                #output.write(str(low_quantile))
                #output.write(str(";"))
                ## Median
                #median_price = np.quantile(temp_list, 0.5)
                #output.write(str(median_price))
                #output.write(str(";"))
                ## 0,75 Quantil
                #high_quantile = np.quantile(temp_list, 0.75)
                #output.write(str(high_quantile))
                #output.write(str(";"))

            else:


                if sum(temp_counter) == 1:
                    try:
                        button = driver.find_element_by_xpath("//a[@class='stopBubbling']")
                        link = button.get_attribute("href")
                        product_page = driver.get(link)
                        for a, b in zip(driver.find_elements_by_xpath("//span[@class='PRICEVALUELEFT']"), driver.find_elements_by_xpath("//span[@class='PRICEVALUERIGHT']")):

                            left = a.text
                            leftb = left.split(",")[0]
                            right = b.text
                            leftright = (str(leftb) + str(".") + str(right))
                            leftright2 = float(leftright)
                            # print(leftright2)
                            temp_list.append(leftright2)
                            temp_number = int("1")
                            temp_counter.append(temp_number)

                        number_products = sum(temp_counter)
                        print(number_products)
                        output.write(str(number_products))
                        output.write(str(";"))


                        # Mittelwert Preis
                        mean_price = np.mean(temp_list)
                        output.write(str(temp_list))
                        output.write(str(";"))




                    except:
                        print("-9")
                        print("-9")
                        print("-9")
                        print("-9")
                        print("-9")
                        print("-9")
                        print("-9")
                        output.write(str("-9") + str(";"))
                        output.write(str("-9") + str(";"))
                        output.write(str("-9") + str(";"))
                        output.write(str("-9") + str(";"))
                        output.write(str("-9") + str(";"))
                        output.write(str("-9") + str(";"))
                        output.write(str("-9") + str(";"))

        except:
            print("-9")
            print("-9")
            print("-9")
            print("-9")
            print("-9")
            print("-9")
            print("-9")
            output.write(str("-9") + str(";"))
            output.write(str("-9") + str(";"))
            output.write(str("-9") + str(";"))
            output.write(str("-9") + str(";"))
            output.write(str("-9") + str(";"))
            output.write(str("-9") + str(";"))
            output.write(str("-9") + str(";"))



        output.write("\n")
        now = datetime.datetime.now()
        print(now)
        output.write(str(now))
    driver.close()