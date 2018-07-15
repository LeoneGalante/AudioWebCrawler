from bs4 import BeautifulSoup
import time
import requests
import wget
from mutagen.mp3 import MP3
from tkinter import *
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile


# Создание рабочего окна
root = Tk()
root.title('WEB CRAWLER')
root.geometry('600x200')
root.protocol('WM_DELETE_WINDOW') # обработчик закрытия окна
root.resizable(False, False)

pb = ttk.Progressbar(root, mode="determinate")
pb.pack()

label = Label(font=(None, 36))
label.location(30, 365)
label.pack()


#Actions
def audio():
    act1 = askopenfile(initialdir="/", title="Select file", filetypes=(("Audio files", "*.mp3"), ("All Files", "*.*")))
    handler_audio(act1)


def photo():
    act2 = askopenfile(initialdir="/", title="Select file",
    filetypes=(("Photo files", "*.jpeg", "*.jpg", "*.bmp", "*.png"), ("All Files", "*.*")))

def video():
    act3 = askopenfile(initialdir="/", title="Select file",
    filetypes=(("Video files", "*.mp4, *.mpg, *.mpeg, *.webm, *.wmv"), ("All Files", "*.*")))


def handler_audio(act1):
	#query = input('What are you searching for:   ')
	url ='http://www.google.com/search?q='
	page = requests.get(url + str(act1.name))
	soup = BeautifulSoup(page.text, 'html.parser')
	h3 = soup.find_all("h3",class_="r")
	for elem in h3:
		pb['value'] = 100
		time.sleep(1.5)
		elem=elem.contents[0]
		link=("https://www.google.com" + elem["href"])
		if link.find('music.yandex.ru') != -1:
			print('Его нельзя: ' + link)
		elif link.find('youtube') != -1:
			print('Его нельзя: ' + link)
		elif link.find('text-lyrics.ru') != -1 or link.find('genius.com') != -1:
			f = open('pir.txt', 'a')
			f.write(link + '\n')
			f.close()
			print('Яма: ' + link)
		else:
			print(link)
			response = requests.get(link)
			soup = BeautifulSoup(response.text, 'html.parser').find('div', class_='download')
			print(soup)
			if soup != None:
				soup = soup.__str__()
				for i in BeautifulSoup(soup, 'html.parser').find_all('a', href=True):
					wget.download(i['href'], act1.name + '_test.mp3')
					audio = MP3(act1.name)
					print("Track: " + audio.get("TIT2").text[0])

					print('Lenght: ' + str(audio.info.length))
					print('Info: ' + audio.info.pprint())

					audio2 = MP3(act1.name + "_test.mp3")
					print('Info: ' + audio2.info.pprint())
					if audio2.get("TIT2") == audio.get("TIT2") and audio2.info.length == audio.info.length and audio2.info.pprint() == audio.info.pprint():
						print("Это подлинный")
						label['text'] = "Это подлинный"
					else:
						print('Пиратская копия')
						label['text'] = 'Пиратская копия'
						f = open('pir.txt', 'a')
						f.write(link + '\n')
						f.close()
					print(i['href'])
	window = Tk()
	window.title("СПИСОК САЙТОВ С ПИРАТСКИМ КОНТЕНТОМ")
	window.geometry("600x150")
	window.resizable(False, False)
	f = open('pir.txt', 'r')
	for line in f.readlines():
		print(line)
	f.close()
	window.mainloop()
#Дизайн интерфейса
img_i = PhotoImage(file="spider.png")
img_o = Label(root, image=img_i)



button1=Button(root, text="Аудио", width=19,height=2,bg='#199ed2',fg='#fff',font='arial 14', command=audio)
button2=Button(root, text="Фото", width=17,height=2,bg='#199ed2',fg='#fff',font='arial 14', command=photo)
button3=Button(root, text="Видео", width=16,height=2,bg='#199ed2',fg='#fff',font='arial 14',command=video)


#Упаковщики
img_o.place(x=0,y=0)
button1.place(x=5,y=120)
button2.place(x=220,y=120)
button3.place(x=410,y=120)



#Create window
root.mainloop()

