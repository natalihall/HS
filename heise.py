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
	
		
	for page in range (0,3,1):
		#heise1_url = "https://www.heise.de/thema/https"
		heise_url = "https://www.heise.de/thema/https?seite="+str(page) 
		#heise_url = "https://www.heise.de/thema/https?seite="+str(page)
		#heise_url = "https://www.heise.de/thema/https?seite="+str(page)	
		
		
		content = getPage(heise_url).find("div", {"class":"keywordliste"})
		content = content.findAll("header")
	
		for wortliste in content:
			wortlisten = wortliste.text.encode('utf-8')
			txt = wortlisten.split()
		csvw.writerow(txt)
	
	
	heisefile.close()

	print("Done!")
	
if __name__ == '__main__':
	main() 
		
