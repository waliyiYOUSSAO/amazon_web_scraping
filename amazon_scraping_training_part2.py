# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 22:59:54 2023

@author: HP
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd


titles_prices = []
liste_princip = []
titres_unique = set()
urls = ['https://www.amazon.com/s?k=iphone+charger+fast+charging&sprefix=ip%2Caps%2C301&ref=nb_sb_ss_ts-doa-p_1_2','https://www.amazon.com/s?k=iphone+charger+fast+charging&page=2&qid=1693430749&sprefix=ip%2Caps%2C301&ref=sr_pg_2','https://www.amazon.com/s?k=iphone+charger+fast+charging&page=3&qid=1693430777&sprefix=ip%2Caps%2C301&ref=sr_pg_3','https://www.amazon.com/s?k=iphone+charger+fast+charging&page=4&qid=1693430797&sprefix=ip%2Caps%2C301&ref=sr_pg_4','https://www.amazon.com/s?k=iphone+charger+fast+charging&page=5&qid=1693430925&sprefix=ip%2Caps%2C301&ref=sr_pg_5','https://www.amazon.com/s?k=iphone+charger+fast+charging&page=6&qid=1693430983&sprefix=ip%2Caps%2C301&ref=sr_pg_6','https://www.amazon.com/s?k=iphone+charger+fast+charging&page=7&qid=1693431032&sprefix=ip%2Caps%2C301&ref=sr_pg_7','https://www.amazon.com/s?k=iphone+charger+fast+charging&page=8&qid=1693431057&sprefix=ip%2Caps%2C301&ref=sr_pg_8','https://www.amazon.com/s?k=iphone+charger+fast+charging&page=9&qid=1693431074&sprefix=ip%2Caps%2C301&ref=sr_pg_9','https://www.amazon.com/s?k=iphone+charger+fast+charging&page=10&qid=1693431088&sprefix=ip%2Caps%2C301&ref=sr_pg_10']
for url in urls:
    
    
    driver = webdriver.Firefox()
    
    driver.get(url)
    
    divs = driver.find_elements('css selector','div.sg-col-inner')
    
    
    
    for div in divs:
        til_pri = {}
        try:
            # recovery of smalls tags inside of big tag (div)
            titre = div.find_element('css selector', 'span.a-size-medium.a-color-base.a-text-normal')
            price = div.find_element('css selector','span.a-offscreen')
            etoiles = div.find_element('css selector', 'span.a-icon-alt')
            
            # using of get_attribut method to extrate html values
            # here, title doesn't need get_attribute method
            prix = price.get_attribute('innerHTML')
            toiles = etoiles.get_attribute('innerHTML')
            
            # using of BeautifulSoup method of bs4 to extrate information from html or lxml documents
            # initialisation of BeautifulSoup
            price_soup = BeautifulSoup(prix,'lxml')
            toiles_soup = BeautifulSoup(toiles, 'lxml')
            
            # extration of text inside html tags
            titre = titre.text.strip()
            prix = price_soup.text.strip()
            toiles = toiles_soup.text.strip()
            
            #print(f"Title : {titre.text.strip()}\n Price: {price_soup.text.strip()}")
            #print("________")
            
            # adding information in list
            til_pri = {'Title':titre, 'Price':prix,'Stars':toiles}
            titles_prices.append(til_pri)
            
        except:                    
                          
            pass          
                          
                          
                          
                          
    for info in titles_prices:                        
                                                   
        if (info['Title'] not in titres_unique) and (info['Title'] != ""):
            titres_unique.add(info['Title'])
            liste_princip.append(info)
        else:
            pass
    
        
    
    #  each time scraping is complete, the browser closes
    driver.quit()
    
# using pandas and excel to store information in ''file.excel''
df = pd.DataFrame(liste_princip)   
path = r"C:\Users\HP\Documents\amazon_scrap.xlsx"
with pd.ExcelWriter(path, engine = 'openpyxl') as amaz:
    df.to_excel(amaz, sheet_name='Amazon_chargers')
    print("Request completed successfully")