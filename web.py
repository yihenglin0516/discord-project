import requests
from bs4 import BeautifulSoup
def show_info(url):
    html=requests.get(url)
    html.encoding='utf_8'
    soup = BeautifulSoup(html.content, 'html.parser')
    teacher=str(soup.find_all('a')[0].string).strip()
    if not teacher:
        teacher=''
    name=str(soup.find_all('td')[3].contents[0]).strip()
    when=str(soup.find_all('td')[23].string).strip()
    credit= str(soup.find_all('td')[17].string).strip()
    return name,teacher,when,credit

    