from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen('https://www.truecaller.com/search/bd/1713001410').read()
print(text_from_html(html))


//*[@id="app"]/main/div/div[1]/div[2]/a[2]/div

//*[@id="app"]/main/div/div[1]/div[2]/a[3]/div