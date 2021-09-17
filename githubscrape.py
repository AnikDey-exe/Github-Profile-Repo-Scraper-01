from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import pandas as pd

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path="C:/Users/manas/Dropbox/My PC (LAPTOP-OEFAVRL0)/Downloads/chromedriver_win32/chromedriver.exe",options=options)
url = 'https://github.com/whitehatjr?tab=repositories'
browser.get(url)

# url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
# browser = webdriver.Chrome('C:/Users/manas/Dropbox/My PC (LAPTOP-OEFAVRL0)/Downloads/chromedriver_win32/chromedriver')
# browser.get(url)

time.sleep(10)

def scrape():
    headers = ["names", "description", "language", "last_update"]
    planet_data = []

    for i in range(0, 14):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for li_tag in soup.find_all("li", attrs={"class", "col-12 d-flex width-full py-4 border-bottom color-border-secondary public source"}):
            div_tags = li_tag.find_all("div", attrs={"class", "col-10 col-lg-9 d-inline-block"})
            # , attrs={"class", "col-10 col-lg-9 d-inline-block"}
            temp_list = []

            for index, div_tag in enumerate(div_tags):
                if index == 0:
                    temp_list.append(div_tag.find_all("a")[0].contents[0])
                    temp_list.append(div_tag.find_all("span")[0].contents[0])
                    temp_list.append(div_tag.find_all("p"))
                    temp_list.append(div_tag.find_all("span"))
                    temp_list.append(div_tag.find_all("relative-time")[0].contents[0])
                # else:
                #     try:
                #         # temp_list.append(div_tag.contents[0])
                #         # temp_list.append(div_tag.find_all("a")[0].contents[0])
                #         # # temp_list.append(div_tag.find_all("p", attrs={"class","col-9 d-inline-block color-text-secondary mb-2 pr-4"})[0].contents[0])
                #         # temp_list.append(div_tag.find_all("span")[0].contents[0])
                #         # temp_list.append(div_tag.find_all("relative-time")[0].contents[0])
                #     except:
                #         temp_list.append("")
                print(temp_list)

            planet_data.append(temp_list)
            
        print(i)

        if i < 2:
            browser.find_element_by_xpath('//*[@id="user-repositories-list"]/div/div/a'+'['+str(i+1)+']').click()
            time.sleep(10)
        # elif: 
        #     browser.find_element_by_xpath('//*[@id="user-repositories-list"]/div/div/a'+'['+str(i+1)+']').click()
        else:
            browser.find_element_by_xpath('//*[@id="user-repositories-list"]/div/div/a'+'[2]').click()
            time.sleep(10)

    with open("github4.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
        
scrape()