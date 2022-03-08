import os
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# import csv_utils as cu
import datetime as dt
import json
import pdfkit
import time
import requests
import re

class PlayMain():
    def __init__(self):
        self.url='https://practice.geeksforgeeks.org/courses/dsa-self-paced/'
        self.folder_path='temp'
        self.current_path = os.getcwd()
        '''div snippet-box
        div class addtoany_share_save_container addtoany_content addtoany_content_bottom
        all iframe
        '''
        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(self.url).text

        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")
        print(type(soup))
        self.list_links(soup)
    def list_links(self,soup):
        try:
            os.mkdir(os.path.join(self.current_path,self.folder_path))
        except:
            pass
        titles=soup.title.text
        print(titles)
        liks=[]
        
        mydivs = soup.find_all("div", {"class": "panel-body"})
        for x in mydivs:
            dd=x.find_all("li")
            for tag in dd:
                tagd=tag.find('p')
                liks.append(tagd)
        print(liks)
        #links=json.dumps(liks)
        titles=re.sub('[^A-Za-z0-9 '']+','',titles)
        titles=titles+".html"
        titles=os.path.join(self.current_path,self.folder_path,titles)
        links=open(titles,"w")
        links.write(str(liks))
        links.close()  
        #print(mydivs.find_all('a',href=True))
        pass
        #print(li_tag)
    def page_load(self,uid,pwd):

        self.driver.get(self.url)
        time.sleep(3)
        try:
            login_pop = self.driver.find_elements_by_class_name('register')
            # Here .click function use to tap on desire elements of webpage
            login_pop.click()
            print('for user '+uid,flush=True)
            #self.driver=self.driver.switch_to().alert();
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/form/a[1]').click() 
            print('Login Clicked',flush=True)
            email_feed=self.driver.find_element_by_xpath('//*[@id="user_register"]/div/form/input[1]')
            self.driver.implicitly_wait(2)
            email_feed.send_keys(Keys.NULL)
            email_feed.send_keys(uid)
            print('email entered',flush=True)
            pass_word=self.driver.find_element_by_xpath('//*[@id="user_register"]/div/form/input[2]')
            self.driver.implicitly_wait(2)
            pass_word.send_keys(Keys.NULL)
            pass_word.send_keys(pwd)
            # print('password entered')
            # self.driver.implicitly_wait(2)
            # self.driver.find_element_by_xpath('//*[@id="user_register"]/div/form/a').click()
            # print('registered Clicked')
            # self.driver.implicitly_wait(5)
            # self.driver.find_element_by_class_name('orange-button button2 ng-binding').click()
            #self.driver.implicitly_wait(5)
            
            
            #self.driver.quit()
        except Exception as ex:
                print(ex)
    def print_page(self,uri):
        title=time.time()
        file_name_d=str(title)+".pdf"
        try:
            os.mkdir(os.path.join(self.current_path,self.folder_path))
        except:
            pass
        path=os.path.join(self.current_path,self.folder_path,file_name_d)
        print(str(path))
        path=path
        path_wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_url(uri,str(path),configuration=config) 
        # chrome_options = webdriver.ChromeOptions()
        # settings = {
        #     "appState": {
        #         "recentDestinations": [{
        #             "id": "Save as PDF",
        #             "origin": "local",
        #             "account": "",
        #         }],
        #         "selectedDestinationId": "Save as PDF",
        #         "version": 2
        #     }
        # }
        # prefs = {'printing.print_preview_sticky_settings': json.dumps(settings)}
        # chrome_options.add_experimental_option('prefs', prefs)
        # chrome_options.add_argument('--kiosk-printing')
        # CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
        # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROMEDRIVER_PATH)
        # driver.get(uri)
        # driver.execute_script('window.print();')
        # #driver.quit()
        # pass

if __name__ == "__main__":

    Flipkart = PlayMain()