import requests
from bs4 import BeautifulSoup
from tkinter import *
window = Tk()
window.title('Latest News')
window.config(background='snow')
window.state('zoomed')
res = requests.get('https://www.indiatoday.in/news.html')
soup = BeautifulSoup(res.text, 'lxml')
news = soup.find_all('a', href=True)
res2 = requests.get('https://www.news18.com/')
soup2 = BeautifulSoup(res2.text, 'lxml')
res3 = requests.get('https://timesofindia.indiatimes.com/')
soup3 = BeautifulSoup(res3.text, 'lxml')
res4 = requests.get('https://www.ndtv.com/india')
soup4 = BeautifulSoup(res4.text, 'lxml')
a = soup2.find_all('a', href=True)
b = soup3.find_all('a', href=True)
c = soup4.find_all('a', href=True)
news2 = []
for i in range(0, len(a)):
	a[i] = a[i].text
for i in range(0, len(b)):
	b[i] = b[i].text
for i in range(0, len(c)):
	c[i] = c[i].text
for i in range(0, len(news)):
	news[i] = news[i].text
news3 = news[41:len(news)]
Label(window, text='TOP HEADLINES', font=('Arial Bold', 40), fg='slate grey',bg='snow').pack(padx=20, pady=20)
for i in range(1,4):
	Label(window, text=news3[i],  font=('Arial Bold', 25), fg='gray10',bg='snow').pack(padx=15, pady=15)

Label(window, text='Select the Topic you want more News about:',font=('Arial Bold', 20), fg='cornflower blue',bg='snow').pack(padx=20, pady=35)

def click():
	global news, a, b, c
	total_news = 0
	total = b + news + c+ a
	query = e.get()
	t = Toplevel()
	t.title(query.capitalize() + ' News')
	Label(t, text=query.capitalize(), font=('Arial Bold', 30), fg='snow', bg='firebrick4').pack(padx=15, pady=15, ipadx=10)
	for r in range(0, len(total)):
		if '.' in total[r]:
			total[r] = total[r][0 : total[r].index('.')]
	for i in range(0, len(total)):
		if query in total[i] or query.capitalize() in total[i]  :
			if '?' not in total[i] and total_news < 10 and total[i].count(' ', 0, len(total[i])) > 4 and len(total[i]) > 15:
				Label(t, text=total[i], font=('Arial Bold', 20), fg='gray17').pack(padx=12, pady=12)
				total_news += 1


def more():
	if India_state.get() == 1:
		India_state.set(0)
		t = Toplevel()
		t.focus()
		t.title('India')
		India = news3.index('India')
		Label(t, text='India',  font=('Arial Bold', 30), fg='snow', bg='firebrick4').pack(padx=15, pady=15, ipadx=10)
		for i in range(1,6):
			Label(t, text=news3[India+i],  font=('Arial Bold', 20), fg='gray17').pack(padx=12, pady=12)
	if Election_state.get() == 1:
		Election_state.set(0)
		t1 = Toplevel()
		t1.focus()
		t1.title('Election')
		Elections = news3.index('Elections')
		Label(t1, text='Elections',  font=('Arial Bold', 30), fg='snow', bg='firebrick4').pack(padx=15, pady=15, ipadx=10)
		for i in range(1,6):
			Label(t1, text=news3[Elections+i],  font=('Arial Bold', 20), fg='gray17').pack(padx=12, pady=12) 
	if Tech_state.get() == 1:
		Tech_state.set(0)
		t2 = Toplevel()
		t2.focus()
		t2.title('Technology')
		Tech = news3.index('Technology')
		Label(t2, text='Technology',  font=('Arial Bold', 30), fg='snow', bg='firebrick4').pack(padx=15, pady=15, ipadx=10)
		for i in range(1,6):
			Label(t2, text=news3[Tech+i],  font=('Arial Bold', 20), fg='gray17').pack(padx=12, pady=12)
	if Sport_state.get() == 1:
		Sport_state.set(0)
		t3 = Toplevel()
		t3.focus()
		t3.title('Sports')
		Sport = news3.index('Sports')
		Label(t3, text='Sports',  font=('Arial Bold', 30), fg='snow', bg='firebrick4').pack(padx=15, pady=15, ipadx=10)
		for i in range(1,6):
			Label(t3, text=news3[Sport+i],  font=('Arial Bold', 20), fg='gray17').pack(padx=12, pady=12)
	if Movie_state.get() == 1:
		Movie_state.set(0)
		t4 = Toplevel()
		t4.focus()
		t4.title('Movies')
		Movie = news3.index('Movies')
		Label(t4, text='Movies',  font=('Arial Bold', 30), fg='snow', bg='firebrick4').pack(padx=15, pady=15, ipadx=10)
		for i in range(1,6):
			Label(t4, text=news3[Movie+i],  font=('Arial Bold', 20), fg='gray17').pack(padx=12, pady=12)
	if Trending_state.get() == 1:
		Trending_state.set(0)
		t5 = Toplevel()
		t5.focus()
		t5.title('Trending News')
		Trend = news3.index('Trending News')
		Label(t5, text='Trending News',  font=('Arial Bold', 30), fg='snow', bg='firebrick4').pack(padx=15, pady=15, ipadx=10)
		for i in range(1,6):
			Label(t5, text=news3[Trend+i],  font=('Arial Bold', 20), fg='gray17').pack(padx=12, pady=12)


India_state = IntVar()
India_chk = Checkbutton(window, text='India', var=India_state,font=('Arial Bold', 20), fg='CadetBlue4',bg='snow')
India_chk.pack(padx=10, pady=3)	
Election_state = IntVar()
Election_chk = Checkbutton(window, text='Election', var=Election_state,font=('Arial Bold', 20), fg='CadetBlue4',bg='snow')
Election_chk.pack(padx=10, pady=3)	
Tech_state = IntVar()
Tech_chk = Checkbutton(window, text='Technology', var=Tech_state,font=('Arial Bold', 20), fg='CadetBlue4',bg='snow')
Tech_chk.pack(padx=10, pady=3)	
Sport_state = IntVar()
Sport_chk = Checkbutton(window, text='Sports', var=Sport_state,font=('Arial Bold', 20), fg='CadetBlue4',bg='snow')
Sport_chk.pack(padx=10, pady=3)	
Movie_state = IntVar()
Movie_chk = Checkbutton(window, text='Movies', var=Movie_state,font=('Arial Bold', 20), fg='CadetBlue4',bg='snow')
Movie_chk.pack(padx=10, pady=3)	
Trending_state = IntVar()
Trending_chk = Checkbutton(window, text='Trending', var=Trending_state,font=('Arial Bold', 20), fg='CadetBlue4',bg='snow')
Trending_chk.pack(padx=10, pady=3)	
Button(window, text='More News!',font=('Arial Bold', 23), fg='bisque4',command=more,bg='snow').pack(padx=20, pady=10)
Label(window, text='Find:', font=('Arial Bold', 20),bg='snow',fg='cornflower blue').pack(padx=20, pady=20)
e = Entry(window, width=50, borderwidth=5, font=('Arial Bold', 20),bg='snow',fg='steel blue')
e.pack( padx=20 , pady=20)
Button(window, text='Search', font=('Arial Bold', 20), command=click, bg='snow', fg='bisque4').pack(padx=10, pady=10)
window.mainloop()
