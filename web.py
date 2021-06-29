import requests
from bs4 import BeautifulSoup
def show_info(url):
    html=requests.get(url)
    html.encoding='utf_8'
    soup = BeautifulSoup(html.content, 'html.parser')
    teacher=soup.find_all('a')[0].string
    name=soup.find_all('td')[3].contents[0]
    when=soup.find_all('td')[23].string
    return name,teacher,when
    