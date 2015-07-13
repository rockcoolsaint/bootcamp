import webbrowser
import time

urls = ['google.com','sellinno.com','ogbincop.com']

def url_opener(urls):
	count = 0
	t = 3
	for x in urls:
		if count < 2:
			webbrowser.open(x)
			time.sleep(t)
			t += 3
			count+=1
		else:
			webbrowser.open(x)
			time.sleep(0)
			count+=1
url_opener(urls)