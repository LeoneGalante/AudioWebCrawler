from bs4 import BeautifulSoup
import wget
from mutagen.mp3 import MP3
import mad
from lxml import etree
import requests



query = input('What are you searching for:   ')
url ='http://www.google.com/search?q='
page = requests.get(url + query)
soup = BeautifulSoup(page.text, 'html.parser')
h3 = soup.find_all("h3",class_="r")
for elem in h3:
	elem=elem.contents[0]
	link=("https://www.google.com" + elem["href"])
	if link.find('music.yandex.ru') != -1:
		print('Его нельзя: ' + link)
	elif link.find('youtube') != -1:
		print('Его нельзя: ' + link)
	elif link.find('text-lyrics.ru') != -1:
		print('Яма: ' + link)
	else:
		print(link)
		response = requests.get(link)
		soup = BeautifulSoup(response.text, 'html.parser').find('div', class_='download')
		print(soup)
		if soup != None:
			soup = soup.__str__()
			for i in BeautifulSoup(soup, 'html.parser').find_all('a', href=True):
				wget.download(i['href'], 'Oxxymiron_where_test.mp3')
				audio = MP3("Oxxymiron_where_test.mp3")
				print("Track: " + audio.get("TIT2").text[0])

				#try:print("Text: " + audio.get("USLT"))
				#except AttributeError: print('Нет текста')
				print('Lenght: ' + str(audio.info.length))
				print('Info: ' + audio.info.pprint())

				audio2 = MP3("Oxxymiron_where.mp3")
				if audio2.get("TIT2") == audio.get("TIT2") and audio2.info.length == audio.info.length and audio2.info.pprint() == audio.info.pprint():
					print("Это подлинный")
				else:
					print('Пиратская копия')

				#print("Encoded By: " + audio.get("TENC").text[0])
				print(i['href'])