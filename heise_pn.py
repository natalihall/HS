import requests
from bs4 import BeautifulSoup
from collections import Counter, OrderedDict


def get_page(url):
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, "lxml")
    return soup


if __name__ == '__main__':
    words = []

    for page in range(0, 3, 1):
        heise_url = "https://www.heise.de/thema/https?seite=" + str(page)

        content = get_page(heise_url).find("div", {"class": "keywordliste"})
        content_header = content.findAll("header")

        for word_lists in content_header:
            word_lists = word_lists.text.encode('utf-8')  
            txt = word_lists.split()
            words.append(txt)

    words = sum(words, [])
    
    a = Counter(words).most_common(3)
    
    print(a)
    #worddict = Counter(words)

    #worddict = OrderedDict(sorted(worddict.items(), key=lambda t: t[1]))
    #print(worddict)
    
    
		
