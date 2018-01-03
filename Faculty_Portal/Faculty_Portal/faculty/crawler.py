from bs4 import BeautifulSoup
import urllib.request
import requests
import re
def update(request,url):
	print(url)
	dic = {}
	res = []
	pro_res = []
	r  = requests.get(url)
	data = r.content
	# data = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(str(data),'lxml')
	main = soup.find("div",{ "id" : "fh5co-main" },{"style" : "text-align: left;"})
	ed = main.findAll("p")
	c=10
	for a in ed:
		if c>3 and c<7 :
			degree=a.text.split(',')[0].split('\n')
			sab = a.text.split(',')
			print(degree)
			print(sab)
		c=c-1
