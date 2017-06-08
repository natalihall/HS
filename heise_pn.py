import requests
from bs4 import BeautifulSoup
from collections import Counter, OrderedDict


def get_page(url):
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, "lxml")
    return soup

def main():
    words = []

    for page in range(0, 4, 1):
        heise_url = "https://www.heise.de/thema/https?seite=" + str(page)

        content = get_page(heise_url).find("div", {"class": "keywordliste"})
        content_header = content.findAll("header")
                
        #####
        l = []
        for i in content_header:
			l.append(i.text)
			print(len(l))
			print(i.text)
			
        for word_lists in content_header:
            word_lists = word_lists.text.encode('utf8')  
            txt = word_lists.split()
            words.append(txt)

    words = sum(words, [])
    
    a = Counter(words).most_common(3)
    
    print(a)
    #worddict = Counter(words)

    #worddict = OrderedDict(sorted(worddict.items(), key=lambda t: t[1]))
    #print(worddict)

if __name__ == '__main__':
	main()
    
    
		
