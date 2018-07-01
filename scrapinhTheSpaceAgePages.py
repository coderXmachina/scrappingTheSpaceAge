from lxml import html                     #html parser
from bs4 import BeautifulSoup as soup     #Beautiful Soup
import requests
import praw
from fake_useragent import UserAgent

ua = UserAgent()

uaHeader = {'User-agent': str(ua.chrome)}

myHeaders = {'User-agent': str(ua.chrome), 'Accept-Encoding': 'identity',
             'content-type': 'application/json', 'Retry-After': '3600',
             'Connection': 'keep-alive', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
             'Upgrade-Insecure-Requests':'1',
             'Accept-Encoding':' gzip, deflate, sdch',
             'Accept-Language':'en-US,en;q=0.8'}

#payload = {'inUserName': 'SonOfTerra92', 'inUserPass': '1qaz@WSX'}
Extension = 'Timeline_of_artificial_satellites_and_space_probes' #URL API extension
myURL ='https://en.wikipedia.org/wiki/' + Extension

try:
  page = requests.get(myURL, myHeaders , timeout=5) #keep doing this
  print("Requesting page: " + myURL)
except requests.exceptions.Timeout: #unless thiss
  print "Timeout occurred"

if str(page) == "<Response [429]>":
      pageSOUP = soup(page.content,"html.parser")
      waitTime = pageSOUP.find_all("p")
      errString = "Error Code: " + str(page)
      print(errString)
      print(waitTime[2])
else:
      print("200 OK\n\n")
      print(page.content) #prints content
      print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

pageSOUP = soup(page.content,"html.parser")
spaceTables = pageSOUP.find_all("table")

Html_file= open((Extension + ".html"),"w")

htmlPadding = "<p>-----------------------------------------------------------------</p>"
for f in range( 1 , (len(spaceTables) - 3)):
      print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
      print("\n****\n")
      print(spaceTables[f].text.encode("utf-8"))
      Html_file.write( "<p></p>" + "<p></p>" + str(spaceTables[f].encode("utf-8")) + "<p></p>" + htmlPadding + "<p></p>")
      print("\n****\n")

page.close()

print(str(len(spaceTables)) + " Elements found")

print("\nFile Written")
Html_file.close()