import webbrowser
import time

count = 0
while count<3:
	webbrowser.open('http://google.com')
	time.sleep(5)
	count += 1