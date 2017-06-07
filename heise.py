import requests
from bs4 import BeautifulSoup
import csv

def getPage(url):
	r = requests.get(url)
	inhalt = r.text
	soup = BeautifulSoup(inhalt, "lxml")
	return soup

def main():
	
	heisefile = open('heise-ueberschriften.csv', 'w')
	csvw = csv.writer(heisefile, delimiter = ';')
	
		
	for page in range (1,4,1):
		heise1_url = "https://www.heise.de/thema/https"+str(page) 
		heise2_url = "https://www.heise.de/thema/https?"+str(page)+"seite=1" 
		heies3_url = "https://www.heise.de/thema/https?"+str(page)+"seite=2"
		heise4_url = "https://www.heise.de/thema/https?"+str(page)+"seite=3"	
		
		
		content = getPage(heise_url).find("div", {"class":"keywordliste"})
		content = content.findALL("header")
	
		#for wortliste in content:
		#	wortlisten = wortliste.text.encode('utf-8')
		#	txt = wortlisten.split()
		
			for t in txt:
				txt.append(t.text.encode('utf-8'))
				txt = t.split()
            csvw.writerow(txt)
				
	
	
	heisefile.close()

	print("Done!")
		
#a = soup.find_all("keywordliste")

#for link in a:
#	print link

#print a
