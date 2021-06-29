import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_class(name,teacher):
    chrome = webdriver.Chrome('./chromedriver', )
    chrome.get("https://www.ptt.cc/bbs/NTUcourse/index.html")
    search=chrome.find_element_by_xpath('//*[@id="search-bar"]/input')
    search.click()
    chrome.implicitly_wait(5)
    search.send_keys(name+' '+teacher)
    search.send_keys(Keys.ENTER)
    chrome.implicitly_wait(5)
    soup=BeautifulSoup(chrome.page_source,'html.parser')
    link='https://www.ptt.cc'+soup.find_all('a')[9].get('href')
    chrome.close()
    return link
    