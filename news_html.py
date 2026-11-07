import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import os

CTX=ssl.create_default_context()
CTX.check_hostname=False
CTX.verify_mode=ssl.CERT_NONE

FOLDER='TV9_news'
os.makedirs(FOLDER,exist_ok=True)

URL= 'https://tv9telugu.com/telangana'
html=urllib.request.urlopen(URL,context=CTX)
soup=BeautifulSoup(html,'html.parser')
main_telagana_page=soup('a')
seen=set()
for newses in main_telagana_page:
    href=newses.get('href')
    if href and href.startswith('https://tv9telugu.com/telangana/'):
        seen.add(href)
        news_html=urllib.request.urlopen(href,context=CTX)
        news_soup=BeautifulSoup(news_html.read(),'html.parser',from_encoding='utf-8')
        h1=news_soup.find('h1')
        if h1:
            title=h1.get_text(strip=True)
            name="".join(c for c in title if c not in '\\/:*?"<>|\r\n\t')[:80].strip()
            paragraphs=[p.get_text(strip=True) for p in news_soup.find_all('p')]
            with open(os.path.join(FOLDER,name+'.txt'),'w',encoding='utf-8') as f:
                f.write(title+'\n\n')
                f.write('\n\n'.join( p for p in paragraphs if p))
            img=news_soup.find('img',id='main-img')
            if img:
                src=img.get('src') or img.get('data-src')
                if src and not src.startswith('data:'):
                    src=urllib.parse.urljoin(href,src)
                    try:
                        data=urllib.request.urlopen(src,context=CTX).read()
                        with open(os.path.join(FOLDER,name+'.jpg'),'wb') as f:
                            f.write(data)
                    except Exception as e:
                        print('image Failed:',src,e)
 

